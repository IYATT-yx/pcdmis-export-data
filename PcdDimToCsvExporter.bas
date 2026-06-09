' file: PcdDimToCsvExporter.bas
' Description: Reads PC-DMIS measurement data and exports it to a CSV file.
'              Prioritizes reading data from an active online measurement routine; 
'              otherwise, defaults to the foreground measurement routine.
' author: IYATT-yx
' repository: https://github.com/IYATT-yx/NX-batch-PDF-exporter
' copyright:  Copyright (c) 2026 IYATT-yx.
'             Licensed under the MIT License. See LICENSE file in the project root for full license information.
Option Explicit

Sub Main
    Dim part As Object
    Dim pcdmisVersion As String
    If Not connect(part, pcdmisVersion) Then
        MsgBox "Error: Failed to connect to PC-DMIS.", 16, "Connection Error"
        Exit Sub
    End If

    Dim dataLineList() As String
    Dim lineCount As Long
    Dim fields(0 To 11) As String

    ' Routine Metadata Initialization
    ' ==============================================================================
    fields(0) = pcdmisVersion
    fields(1) = part.Name
    fields(2) = part.FullName
    fields(3) = part.SerialNumber
    fields(4) = part.GetVariableValue("SN").StringValue
    If fields(4) <> "0" Then
        part.SerialNumber = fields(4)
    End If
    fields(5) = CStr(part.PartProgramSettings.MinusTolerancesShowNegative)

    lineCount = 0
    ReDim Preserve dataLineList(0 To lineCount)
    dataLineList(lineCount) = joinCsvRowFields(fields, "")

    ' CSV Layout Header Serialization
    ' ==============================================================================
    Erase fields
    fields(0) = "ID"
    fields(1) = "Feature1"
    fields(2) = "Feature2"
    fields(3) = "Feature3"
    fields(4) = "AxisLetter"
    fields(5) = "Unit"
    fields(6) = "Nominal"
    fields(7) = "Plus"
    fields(8) = "Minus"
    fields(9) = "Measured"
    fields(10) = "Bonus"
    fields(11) = "Type"
    lineCount = lineCount + 1
    ReDim Preserve dataLineList(0 To lineCount)
    dataLineList(lineCount) = joinCsvRowFields(fields, "")

    ' Dynamic Feature Telemetry Iteration Loop
    ' ==============================================================================
    Dim cmds As Object
    Set cmds = part.Commands
    Dim cmd As Object
    For Each cmd In cmds
        If readDimension(cmd, fields) Then
            lineCount = lineCount + 1
            ReDim Preserve dataLineList(0 To lineCount)
            dataLineList(lineCount) = joinCsvRowFields(fields, "")  
        End If
    Next cmd

    ' ==============================================================================
    If lineCount > 1 Then
        If Not saveCsv("C:\Temp\PC-DMIS-TEMP.csv", dataLineList, False) Then
            MsgBox "Error: Failed to save production data to the local CSV repository.", 16, "I/O Storage Error"
        End If
    Else
        MsgBox "Error: No production data was found.", 16, "Data Error"
    End If

    Set part = Nothing
End Sub

' =============================================================================
' CONSTANTS: PC-DMIS Dimension Type
' =============================================================================
Const DATA_TYPE_DIMENSION     = "D"
Const DATA_TYPE_FCF           = "F"
Const DATA_TYPE_FCFDIM        = "FD"
Const DATA_TYPE_UNKNOWN       = "U"
' ==============================================================================

Function readDimension(ByRef cmd As Object, ByRef fields() as String) As Boolean
    If cmd.IsDimension Then
        readDimension = True

        Dim dimObj As Object
        Set dimObj = cmd.DimensionCommand
        Erase fields

        fields(0) = dimObj.ID
        fields(1) = dimObj.Feat1
        fields(2) = dimObj.Feat2
        fields(3) = dimObj.Feat3
        fields(4) = dimObj.AxisLetter
        fields(5) = cmd.GetFieldValue(UNIT_TYPE, 0)
        fields(6) = dimObj.NOMINAL
        fields(7) = dimObj.Plus
        fields(8) = dimObj.Minus
        fields(9) = dimObj.Measured
        fields(10) = dimObj.Bonus
        fields(11) = DATA_TYPE_DIMENSION
    Else
        readDimension = False
    End If
End Function


' MachineConnectionStatus Enumeration
' ==============================================================================
Const MCS_NotAvailable         = -1
Const MCS_MachineNotConnected  = 0
Const MCS_MachineConnecting    = 1
Const MCS_MachineConnected       = 2
Const MCS_MachineDisconnecting = 3
Const MCS_MachineHoming        = 4
' ==============================================================================

' =============================================================================
' Purpose: Establishes a runtime binding context with an active PC-DMIS 
'          measurement routine and retrieves the current software version.
'          
' Execution Priority Strategy:
'   - Priority 1: Traverses all loaded routines to bind to an active online 
'                 execution context (where the machine is physically connected).
'   - Priority 2: Falls back to the current active foreground routine 
'                 if no active online hardware connection is detected.
'
' Parameters:
'   - part:          [Out] [ByRef] An object reference to be bound to the resolved
'                    PartProgram instance. Returns Nothing if resolution fails.
'   - pcdmisVersion: [Out] [ByRef] A string buffer to receive the raw application
'                    version string (e.g., "2023.2", "2018 R1").
'
' Returns: True if a valid PartProgram object is successfully resolved and bound; 
'          False if no routine is active or an interface error occurs.
' =============================================================================
Function connect(ByRef part As Object, ByRef pcdmisVersion As String) As Boolean
    connect = False
    Set part = Nothing

    Dim app As Object
    Set app = CreateObject("PCDLRN.Application")
    pcdmisVersion = app.VersionString

    Dim parts As Object
    Set parts = app.PartPrograms

    If parts.Count = 0 Then
        connect = False
        Set parts = Nothing
        Set app = Nothing
        Exit Function
    End If

    Dim p As Object
    For Each p In parts
        If Not p.ActiveMachine Is Nothing Then
            If p.ActiveMachine.ConnectionStatus = MCS_MachineConnected Then
                Set part = p
                connect = True
                Set p = Nothing
                Set parts = Nothing
                Set app = Nothing
                Exit Function
            End If
        End If
    Next p

    Dim activePart As Object
    Set activePart = app.ActivePartProgram
    If Not activePart Is Nothing Then
        Set part = activePart
        connect = True
    End If

    Set activePart = Nothing
    Set parts = Nothing
    Set app = Nothing
End Function

' =============================================================================
' Purpose: Saves an array of CSV row strings to a physical file with UTF-8 encoding.
'          Handles automated multi-level directory creation and optional file appending.
' Parameters:
'   - filePath:     The absolute target disk path where the CSV file will be saved.
'   - dataLines:    A reference to a 1D string array containing pre-formatted CSV rows.
'   - isAppendMode: Boolean flag. True to append to an existing file; False to overwrite.
' Returns: True if the file persistence succeeds; False if an I/O error occurs.
' =============================================================================
Function saveCsv(ByVal filePath As String, ByRef dataLines() As String, ByVal isAppendMode As Boolean) As Boolean
    On Error GoTo ErrorHandler
    SaveCsv = False

    Dim fso As Object
    Set fso = CreateObject("Scripting.FileSystemObject")
    Dim parentFolder As String
    parentFolder = fso.GetParentFolderName(filePath)

    If Not fso.FolderExists(parentFolder) Then
        Dim wsh As Object
        Set wsh = CreateObject("WScript.Shell")

        If Not wsh Is Nothing Then
            Dim cmdString As String
            cmdString = "cmd.exe /c mkdir """ & parentFolder & """"
            wsh.Run cmdString, 0, True
        End If

        Set wsh = Nothing
    End If

    Dim stream As Object
    Set stream = CreateObject("ADODB.Stream")
    stream.Type = 2
    stream.Charset = "utf-8"
    stream.Open

    If isAppendMode And fso.FileExists(filePath) Then
        stream.LoadFromFile filePath
        stream.Position = stream.Size
    End If

    Dim i As Long
    For i = LBound(dataLines) To UBound(dataLines)
        stream.WriteText dataLines(i) & Chr(13) & Chr(10)
    Next i

    stream.SaveToFile filePath, 2

    stream.Close
    Set stream = Nothing
    Set fso = Nothing
    SaveCsv = True
    Exit Function

ErrorHandler:
    MsgBox "文件持久化发生异常: " & Err.Description, 16, "I/O 模块错误"
    If Not stream Is Nothing Then
        ' 确保流处于打开状态时才执行关闭，防止二次崩溃
        On Error Resume Next
        stream.Close
        Set stream = Nothing
    End If
    Set fso = Nothing
End Function

' =============================================================================
' Purpose: Joins an array of strings into a single RFC 4180-compliant CSV row.
'          Automatically handles character escaping for quotes, delimiters, and line breaks.
' Parameters:
'   - fields:    A reference to the 1D string array containing the row data.
'   - delimiter: The character used to separate fields. Defaults to a comma (,) if empty.
'                Fails if the delimiter itself contains a double quote.
' Returns: A fully escaped and concatenated CSV row string, or an empty string if 
'          an error or invalid parameter is encountered.
' =============================================================================
Function joinCsvRowFields(ByRef fields() As String, ByVal delimiter As String) As String
    If delimiter = "" Then
        delimiter = ","
    ElseIf InStr(1, delimiter, """") > 0 Then
        joinCsvRowFields = ""
        Exit Function
    End If

    On Error Resume Next
    Dim lowerBound As Long
    Dim upperBound As Long
    lowerBound = LBound(fields)
    upperBound = UBound(fields)

    If Err.Number <> 0 Or upperBound < lowerBound Then
        Err.Clear
        joinCsvRowFields = ""
        Exit Function
    End If
    On Error GoTo 0 

    Dim i As Long
    Dim resultBuffer As String
    Dim field As String

    Dim strCr As String
    Dim strLf As String
    strCr = Chr(13)
    strLf = Chr(10)

    For i = lowerBound To upperBound
        field = fields(i)

        If InStr(1, field, delimiter) > 0 Or _
           InStr(1, field, """") > 0 Or _
           InStr(1, field, strCr) > 0 Or _
           InStr(1, field, strLf) > 0 Then

            field = myReplace(field, """", """""")
            field = """" & field & """"
        End If

        If i = lowerBound Then
            resultBuffer = field
        Else
            resultBuffer = resultBuffer & delimiter & field
        End If
    Next i

    joinCsvRowFields = resultBuffer
End Function

' =============================================================================
' BASIC String Comparison Mode Constants Definition
' =============================================================================
Const vbBinaryCompare          = 0 ' Binary comparison (Case-sensitive)
Const vbTextCompare            = 1 ' Text comparison (Case-insensitive)
' =============================================================================

' =============================================================================
' Purpose: Replaces all occurrences of a specified substring within a source 
'          string with another specified substring using binary comparison.
' Parameters:
'   - sourceStr:  The original string to be searched.
'   - findStr:    The substring to search for. If empty, the original string 
'                 is returned unmodified.
'   - replaceStr: The substring to replace the found occurrences with.
' Returns: A new string with the specified replacements made.
' =============================================================================
Function myReplace(ByVal sourceStr As String, ByVal findStr As String, ByVal replaceStr As String) As String
    If findStr = "" Then
        MyReplace = sourceStr
        Exit Function
    End If

    Dim pos As Long
    Dim startPos As Long
    Dim result As String
    startPos = 1
    result = "" 
    Do
        pos = InStr(startPos, sourceStr, findStr, vbBinaryCompare)
        If pos = 0 Then
            result = result & Mid(sourceStr, startPos)
            Exit Do
        Else
            result = result & Mid(sourceStr, startPos, pos - startPos) & replaceStr
            startPos = pos + Len(findStr)
        End If
    Loop

    myReplace = result
End Function