# -*- coding: utf-8 -*-
# Created by makepy.py version 0.5.01
# By python version 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)]
# From type library 'Pcdlrn.tlb'
# On Sat Dec  7 22:08:46 2024
'PC-DMIS 2019 R2 Object Library'
makepy_version = '0.5.01'
python_version = 0x30d01f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{10C96EB9-ED97-492D-BC67-700C7F18E394}')
MajorVersion = 14
MinorVersion = 2
LibraryFlags = 8
LCID = 0x0

class constants:
	PCD_ANGLE_VECTOR              =6          # from enum AUTOVECTORTYPES
	PCD_EDGE_REPORT_VECTOR        =8          # from enum AUTOVECTORTYPES
	PCD_MEASURE_VECTOR            =10         # from enum AUTOVECTORTYPES
	PCD_PIN_VECTOR                =5          # from enum AUTOVECTORTYPES
	PCD_PUNCH_VECTOR              =4          # from enum AUTOVECTORTYPES
	PCD_REPORT_VECTOR             =7          # from enum AUTOVECTORTYPES
	PCD_SURF_REPORT_VECTOR        =9          # from enum AUTOVECTORTYPES
	PCD_UPDATE_VECTOR             =11         # from enum AUTOVECTORTYPES
	PCD_VECTOR1                   =1          # from enum AUTOVECTORTYPES
	PCD_VECTOR2                   =2          # from enum AUTOVECTORTYPES
	PCD_VECTOR3                   =3          # from enum AUTOVECTORTYPES
	BSBOUNDCOND_CONE              =600050     # from enum BSBOUNDCOND_ENUM
	BSBOUNDCOND_CYLINDER          =600040     # from enum BSBOUNDCOND_ENUM
	BSBOUNDCOND_PLANECROSS        =600030     # from enum BSBOUNDCOND_ENUM
	BSBOUNDCOND_SPHERE            =600010     # from enum BSBOUNDCOND_ENUM
	BSCANHIT_BASIC                =700090     # from enum BSCANHIT_ENUM
	BSCANHIT_EDGE                 =700030     # from enum BSCANHIT_ENUM
	BSCANHIT_SURFACE              =700020     # from enum BSCANHIT_ENUM
	BSCANHIT_VECTOR               =700010     # from enum BSCANHIT_ENUM
	BSCANMETH_ANGLE               =100075     # from enum BSCANMETH_ENUM
	BSCANMETH_CENTER              =100140     # from enum BSCANMETH_ENUM
	BSCANMETH_CIRCLE              =100125     # from enum BSCANMETH_ENUM
	BSCANMETH_CLOSE               =100510     # from enum BSCANMETH_ENUM
	BSCANMETH_CYLINDER            =100130     # from enum BSCANMETH_ENUM
	BSCANMETH_EDGE                =100050     # from enum BSCANMETH_ENUM
	BSCANMETH_FREEFORM            =100555     # from enum BSCANMETH_ENUM
	BSCANMETH_GRID                =100560     # from enum BSCANMETH_ENUM
	BSCANMETH_LINEAR              =100010     # from enum BSCANMETH_ENUM
	BSCANMETH_MANUAL_FIXED_PROBE  =100610     # from enum BSCANMETH_ENUM
	BSCANMETH_MANUAL_TTP          =100600     # from enum BSCANMETH_ENUM
	BSCANMETH_OPEN                =100500     # from enum BSCANMETH_ENUM
	BSCANMETH_PATCH               =100520     # from enum BSCANMETH_ENUM
	BSCANMETH_PERIMETER           =100100     # from enum BSCANMETH_ENUM
	BSCANMETH_ROTARY              =100545     # from enum BSCANMETH_ENUM
	BSCANMETH_STRAIGHTLINE        =100135     # from enum BSCANMETH_ENUM
	BSCANMETH_UV                  =100530     # from enum BSCANMETH_ENUM
	BSCANNMODE_FINDCADNOMINAL     =400001     # from enum BSCANNMODE_ENUM
	BSCANNMODE_FINDCADNOMSMULTIROW=400003     # from enum BSCANNMODE_ENUM
	BSCANNMODE_MASTERDATA         =400002     # from enum BSCANNMODE_ENUM
	BSCANOPMODE_DEFINEPATHFROMHITS=500021     # from enum BSCANOPMODE_ENUM
	BSCANOPMODE_HIGHSPEEDFEATUREBASED=500022     # from enum BSCANOPMODE_ENUM
	BSCANOPMODE_NORMALEXECUTION   =500201     # from enum BSCANOPMODE_ENUM
	BSCANOPMODE_REGULARLEARN      =500011     # from enum BSCANOPMODE_ENUM
	BSCTRLPT_CONE                 =800040     # from enum BSCTRLPT_ENUM
	BSCTRLPT_CYLINDER             =800030     # from enum BSCTRLPT_ENUM
	BSCTRLPT_PLANE                =800020     # from enum BSCTRLPT_ENUM
	BSCTRLPT_SPHERE               =800010     # from enum BSCTRLPT_ENUM
	BSF_BODYAXISDISTANCE          =200015     # from enum BSF_ENUM
	BSF_DISTANCE                  =200010     # from enum BSF_ENUM
	BSF_NULL                      =200060     # from enum BSF_ENUM
	BSF_TIME_DELTA                =200030     # from enum BSF_ENUM
	BSF_VARIABLEDISTANCE          =200020     # from enum BSF_ENUM
	Bottom                        =1          # from enum BringToZPositionMode
	NotTopMost                    =-2         # from enum BringToZPositionMode
	Top                           =0          # from enum BringToZPositionMode
	TopMost                       =-1         # from enum BringToZPositionMode
	PCD_CATCH_IN_INTEGER          =1          # from enum CATCHTYPE
	PCD_TRIGGER_ERROR             =2          # from enum CATCHTYPE
	PCD__OFF                      =0          # from enum CATCHTYPE
	AUTO_ANGLE_HIT                =605        # from enum CREATEIDTYPE
	AUTO_CORNER_HIT               =606        # from enum CREATEIDTYPE
	AUTO_EDGE_HIT                 =604        # from enum CREATEIDTYPE
	AUTO_SURFACE_HIT              =603        # from enum CREATEIDTYPE
	AUTO_VECTOR_HIT               =602        # from enum CREATEIDTYPE
	AUTO___CIRCLE                 =612        # from enum CREATEIDTYPE
	AUTO___CYLINDER               =616        # from enum CREATEIDTYPE
	AUTO___ELLIPSE                =621        # from enum CREATEIDTYPE
	AUTO___ROUND_SLOT             =618        # from enum CREATEIDTYPE
	AUTO___SPHERE                 =613        # from enum CREATEIDTYPE
	AUTO___SQUARE_SLOT            =619        # from enum CREATEIDTYPE
	CONST___ALN_LINE              =548        # from enum CREATEIDTYPE
	CONST___ALN_PLANE             =576        # from enum CREATEIDTYPE
	CONST___BFRE_CIRCLE           =520        # from enum CREATEIDTYPE
	CONST___BFRE_CONE             =551        # from enum CREATEIDTYPE
	CONST___BFRE_CYLINDER         =560        # from enum CREATEIDTYPE
	CONST___BFRE_ELLIPSE          =580        # from enum CREATEIDTYPE
	CONST___BFRE_LINE             =540        # from enum CREATEIDTYPE
	CONST___BFRE_PLANE            =570        # from enum CREATEIDTYPE
	CONST___BFRE_SPHERE           =530        # from enum CREATEIDTYPE
	CONST___BF_CIRCLE             =521        # from enum CREATEIDTYPE
	CONST___BF_CONE               =552        # from enum CREATEIDTYPE
	CONST___BF_CYLINDER           =561        # from enum CREATEIDTYPE
	CONST___BF_ELLIPSE            =581        # from enum CREATEIDTYPE
	CONST___BF_LINE               =541        # from enum CREATEIDTYPE
	CONST___BF_PLANE              =571        # from enum CREATEIDTYPE
	CONST___BF_SPHERE             =531        # from enum CREATEIDTYPE
	CONST___CAST_CIRCLE           =525        # from enum CREATEIDTYPE
	CONST___CAST_CONE             =555        # from enum CREATEIDTYPE
	CONST___CAST_CYLINDER         =564        # from enum CREATEIDTYPE
	CONST___CAST_ELLIPSE          =584        # from enum CREATEIDTYPE
	CONST___CAST_LINE             =545        # from enum CREATEIDTYPE
	CONST___CAST_PLANE            =574        # from enum CREATEIDTYPE
	CONST___CAST_POINT            =517        # from enum CREATEIDTYPE
	CONST___CAST_SPHERE           =534        # from enum CREATEIDTYPE
	CONST___CONE_CIRCLE           =524        # from enum CREATEIDTYPE
	CONST___CORNER_POINT          =518        # from enum CREATEIDTYPE
	CONST___DROP_POINT            =514        # from enum CREATEIDTYPE
	CONST___HIPNT_PLANE           =579        # from enum CREATEIDTYPE
	CONST___INT_CIRCLE            =526        # from enum CREATEIDTYPE
	CONST___INT_ELLIPSE           =585        # from enum CREATEIDTYPE
	CONST___INT_LINE              =546        # from enum CREATEIDTYPE
	CONST___INT_POINT             =516        # from enum CREATEIDTYPE
	CONST___MID_LINE              =544        # from enum CREATEIDTYPE
	CONST___MID_PLANE             =573        # from enum CREATEIDTYPE
	CONST___MID_POINT             =513        # from enum CREATEIDTYPE
	CONST___OFF_LINE              =547        # from enum CREATEIDTYPE
	CONST___OFF_PLANE             =575        # from enum CREATEIDTYPE
	CONST___OFF_POINT             =511        # from enum CREATEIDTYPE
	CONST___ORIG_POINT            =510        # from enum CREATEIDTYPE
	CONST___PIERCE_POINT          =515        # from enum CREATEIDTYPE
	CONST___PLTO_LINE             =550        # from enum CREATEIDTYPE
	CONST___PLTO_PLANE            =578        # from enum CREATEIDTYPE
	CONST___PROJ_CIRCLE           =522        # from enum CREATEIDTYPE
	CONST___PROJ_CONE             =553        # from enum CREATEIDTYPE
	CONST___PROJ_CYLINDER         =562        # from enum CREATEIDTYPE
	CONST___PROJ_ELLIPSE          =582        # from enum CREATEIDTYPE
	CONST___PROJ_LINE             =542        # from enum CREATEIDTYPE
	CONST___PROJ_POINT            =512        # from enum CREATEIDTYPE
	CONST___PROJ_SPHERE           =532        # from enum CREATEIDTYPE
	CONST___PRTO_LINE             =549        # from enum CREATEIDTYPE
	CONST___PRTO_PLANE            =577        # from enum CREATEIDTYPE
	CONST___REV_CIRCLE            =523        # from enum CREATEIDTYPE
	CONST___REV_CONE              =554        # from enum CREATEIDTYPE
	CONST___REV_CYLINDER          =563        # from enum CREATEIDTYPE
	CONST___REV_ELLIPSE           =583        # from enum CREATEIDTYPE
	CONST___REV_LINE              =543        # from enum CREATEIDTYPE
	CONST___REV_PLANE             =572        # from enum CREATEIDTYPE
	CONST___REV_SPHERE            =533        # from enum CREATEIDTYPE
	CONST___SET                   =596        # from enum CREATEIDTYPE
	DIM_2D_ANGLE                  =1109       # from enum CREATEIDTYPE
	DIM_2D_DISTANCE               =1107       # from enum CREATEIDTYPE
	DIM_3D_ANGLE                  =1108       # from enum CREATEIDTYPE
	DIM_3D_DISTANCE               =1106       # from enum CREATEIDTYPE
	DIM_ANGULARITY                =1112       # from enum CREATEIDTYPE
	DIM_CONCENTRICITY             =1111       # from enum CREATEIDTYPE
	DIM_FLATNESS                  =1102       # from enum CREATEIDTYPE
	DIM_KEYIN                     =1113       # from enum CREATEIDTYPE
	DIM_LOCATION                  =1000       # from enum CREATEIDTYPE
	DIM_PARALLELISM               =1104       # from enum CREATEIDTYPE
	DIM_PERPENDICULARITY          =1103       # from enum CREATEIDTYPE
	DIM_PROFILE                   =1105       # from enum CREATEIDTYPE
	DIM_ROUNDNESS                 =1101       # from enum CREATEIDTYPE
	DIM_RUNOUT                    =1110       # from enum CREATEIDTYPE
	DIM_STRAIGHTNESS              =1100       # from enum CREATEIDTYPE
	DIM_TRUE_POSITION             =1200       # from enum CREATEIDTYPE
	MEASURED___CIRCLE             =202        # from enum CREATEIDTYPE
	MEASURED___CONE               =205        # from enum CREATEIDTYPE
	MEASURED___CYLINDER           =206        # from enum CREATEIDTYPE
	MEASURED___LINE               =204        # from enum CREATEIDTYPE
	MEASURED___PLANE              =207        # from enum CREATEIDTYPE
	MEASURED___POINT              =201        # from enum CREATEIDTYPE
	MEASURED___SET                =210        # from enum CREATEIDTYPE
	MEASURED___SPHERE             =203        # from enum CREATEIDTYPE
	PCD_ALIGNMENT                 =1          # from enum CREATEIDTYPE
	PCD_CURVE                     =38         # from enum CREATEIDTYPE
	READ___POINT                  =192        # from enum CREATEIDTYPE
	DATATYPE_ALPHANUMERIC         =3          # from enum DATA_TYPE_TYPES
	DATATYPE_CALCULATED_CONSTANT  =2          # from enum DATA_TYPE_TYPES
	DATATYPE_ERROR                =0          # from enum DATA_TYPE_TYPES
	DATATYPE_EXPRESSION           =6          # from enum DATA_TYPE_TYPES
	DATATYPE_MEASURED_CONSTANT    =1          # from enum DATA_TYPE_TYPES
	DATATYPE_NUMERIC              =4          # from enum DATA_TYPE_TYPES
	DATATYPE_TOGGLE               =5          # from enum DATA_TYPE_TYPES
	PCD_DCC                       =100        # from enum DCCMODE
	PCD_MANUAL                    =101        # from enum DCCMODE
	PCD_A                         =505        # from enum DIMAXISTYPE
	PCD_D                         =503        # from enum DIMAXISTYPE
	PCD_DD                        =511        # from enum DIMAXISTYPE
	PCD_DF                        =512        # from enum DIMAXISTYPE
	PCD_L                         =510        # from enum DIMAXISTYPE
	PCD_M                         =518        # from enum DIMAXISTYPE
	PCD_PA                        =507        # from enum DIMAXISTYPE
	PCD_PD                        =517        # from enum DIMAXISTYPE
	PCD_PR                        =508        # from enum DIMAXISTYPE
	PCD_R                         =504        # from enum DIMAXISTYPE
	PCD_RS                        =515        # from enum DIMAXISTYPE
	PCD_RT                        =516        # from enum DIMAXISTYPE
	PCD_S                         =514        # from enum DIMAXISTYPE
	PCD_T                         =506        # from enum DIMAXISTYPE
	PCD_TP                        =513        # from enum DIMAXISTYPE
	PCD_V                         =509        # from enum DIMAXISTYPE
	PCD_X                         =500        # from enum DIMAXISTYPE
	PCD_Y                         =501        # from enum DIMAXISTYPE
	PCD_Z                         =502        # from enum DIMAXISTYPE
	PCD_HEADINGS                  =1          # from enum DIMFORMATFLAG
	PCD_SYMBOLS                   =2          # from enum DIMFORMATFLAG
	PCD_DEV                       =5          # from enum DIMFORMATTYPE
	PCD_DEVANG                    =7          # from enum DIMFORMATTYPE
	PCD_MAXMIN                    =4          # from enum DIMFORMATTYPE
	PCD_MEAS                      =3          # from enum DIMFORMATTYPE
	PCD_NOM                       =1          # from enum DIMFORMATTYPE
	PCD_NOT_USED                  =0          # from enum DIMFORMATTYPE
	PCD_OUTTOL                    =6          # from enum DIMFORMATTYPE
	PCD_TOL                       =2          # from enum DIMFORMATTYPE
	AdjustFilterDialog            =5          # from enum DialogTypes
	AngleDimensionDialog          =200        # from enum DialogTypes
	AngularityDimensionDialog     =205        # from enum DialogTypes
	BestFitAlignmentDialog        =100        # from enum DialogTypes
	CircularityDimensionDialog    =202        # from enum DialogTypes
	CoaxialityDimensionDialog     =209        # from enum DialogTypes
	CollisionListDialog           =14         # from enum DialogTypes
	CommentDialog                 =8          # from enum DialogTypes
	ConcentricityDimensionDialog  =210        # from enum DialogTypes
	ConstructedCircleDialog       =42         # from enum DialogTypes
	ConstructedConeDialog         =43         # from enum DialogTypes
	ConstructedCurveDialog        =44         # from enum DialogTypes
	ConstructedCylinderDialog     =45         # from enum DialogTypes
	ConstructedEllipseDialog      =46         # from enum DialogTypes
	ConstructedFeatureDialog      =40         # from enum DialogTypes
	ConstructedFilterFeature      =56         # from enum DialogTypes
	ConstructedGageDialog         =55         # from enum DialogTypes
	ConstructedGenericFeature     =57         # from enum DialogTypes
	ConstructedLineDialog         =47         # from enum DialogTypes
	ConstructedParentDialog       =41         # from enum DialogTypes
	ConstructedPlaneDialog        =48         # from enum DialogTypes
	ConstructedPointDialog        =49         # from enum DialogTypes
	ConstructedRoundSlotDialog    =50         # from enum DialogTypes
	ConstructedSphereDialog       =52         # from enum DialogTypes
	ConstructedSquareSlotDialog   =51         # from enum DialogTypes
	ConstructedSurfaceDialog      =53         # from enum DialogTypes
	ConstructedWidthDialog        =54         # from enum DialogTypes
	DMISImportExportResultsDialog =12         # from enum DialogTypes
	DatumDefinitionDialog         =215        # from enum DialogTypes
	DeleteFeaturesDialog          =7          # from enum DialogTypes
	DimensionalKeyinDialog        =216        # from enum DialogTypes
	DistanceDimensionDialog       =201        # from enum DialogTypes
	EditFeatureAppearanceDialog   =6          # from enum DialogTypes
	ExpressionBuilderDialog       =11         # from enum DialogTypes
	FileOpenDialog                =3          # from enum DialogTypes
	FileSaveAsDialog              =4          # from enum DialogTypes
	FlatnessDimensionDialog       =203        # from enum DialogTypes
	GenericDialog                 =0          # from enum DialogTypes
	GoToDialog                    =10         # from enum DialogTypes
	LeapFrogAlignmentDialog       =101        # from enum DialogTypes
	LocationDimensionDialog       =213        # from enum DialogTypes
	MeasuredCircleDialog          =20         # from enum DialogTypes
	MeasuredConeDialog            =21         # from enum DialogTypes
	MeasuredCylinderDialog        =22         # from enum DialogTypes
	MeasuredLineDialog            =23         # from enum DialogTypes
	MeasuredPlaneDialog           =24         # from enum DialogTypes
	MeasuredPointDialog           =25         # from enum DialogTypes
	MeasuredRoundSlotDialog       =26         # from enum DialogTypes
	MeasuredSetDialog             =28         # from enum DialogTypes
	MeasuredSphereDialog          =29         # from enum DialogTypes
	MeasuredSquareSlotDialog      =27         # from enum DialogTypes
	MeasuredTorusDialog           =30         # from enum DialogTypes
	ParallelismDimensionDialog    =206        # from enum DialogTypes
	PerpendicularityDimensionDialog=207        # from enum DialogTypes
	PointCloudAlignmentDialog     =105        # from enum DialogTypes
	PointCloudDataCollection      =123        # from enum DialogTypes
	PointCloudDialog              =120        # from enum DialogTypes
	PointCloudMeshDialog          =121        # from enum DialogTypes
	PointCloudOperatorDialog      =122        # from enum DialogTypes
	PositionDimensionDialog       =214        # from enum DialogTypes
	ProbesDialog                  =1          # from enum DialogTypes
	ProfileDimensionDialog        =208        # from enum DialogTypes
	RunoutDimensionDialog         =211        # from enum DialogTypes
	SelectCNCMachineDialog        =9          # from enum DialogTypes
	SelectProbeFileDialog         =13         # from enum DialogTypes
	StraightnessDimensionDialog   =204        # from enum DialogTypes
	SymmetryDimensionDialog       =212        # from enum DialogTypes
	TraceFieldDialog              =15         # from enum DialogTypes
	TutorBarIterativeAlignmentDialog=104        # from enum DialogTypes
	UtilityAlignmentDialog        =102        # from enum DialogTypes
	UtilityIterativeAlignmentDialog=103        # from enum DialogTypes
	EDGE_BOTH                     =2          # from enum EDGE_MEASURE_TYPES
	EDGE_EDGE_FIRST               =1          # from enum EDGE_MEASURE_TYPES
	EDGE_SURFACE_FIRST            =0          # from enum EDGE_MEASURE_TYPES
	ALIGN_CURRENT_WORKPLANE       =6          # from enum ENUM_ALIGN_WORKPLANE
	ALIGN_XMINUS                  =3          # from enum ENUM_ALIGN_WORKPLANE
	ALIGN_XPLUS                   =2          # from enum ENUM_ALIGN_WORKPLANE
	ALIGN_YMINUS                  =5          # from enum ENUM_ALIGN_WORKPLANE
	ALIGN_YPLUS                   =4          # from enum ENUM_ALIGN_WORKPLANE
	ALIGN_ZMINUS                  =1          # from enum ENUM_ALIGN_WORKPLANE
	ALIGN_ZPLUS                   =0          # from enum ENUM_ALIGN_WORKPLANE
	AXIS_XMINUS                   =4          # from enum ENUM_AXIS_TYPE
	AXIS_XPLUS                    =1          # from enum ENUM_AXIS_TYPE
	AXIS_YMINUS                   =5          # from enum ENUM_AXIS_TYPE
	AXIS_YPLUS                    =2          # from enum ENUM_AXIS_TYPE
	AXIS_ZMINUS                   =3          # from enum ENUM_AXIS_TYPE
	AXIS_ZPLUS                    =0          # from enum ENUM_AXIS_TYPE
	BF_MATH_FIXED_RADIUS          =4          # from enum ENUM_BEST_FIT_MATH_TYPES
	BF_MATH_LEAST_SQUARES         =0          # from enum ENUM_BEST_FIT_MATH_TYPES
	BF_MATH_MAX_INSCRIBED         =2          # from enum ENUM_BEST_FIT_MATH_TYPES
	BF_MATH_MIN_CIRCUMSCRIBED     =3          # from enum ENUM_BEST_FIT_MATH_TYPES
	BF_MATH_MIN_SEPARATION        =1          # from enum ENUM_BEST_FIT_MATH_TYPES
	BITMAP_LAYOUT_CENTER          =6          # from enum ENUM_BITMAP_LAYOUT
	BITMAP_LAYOUT_LEFT            =0          # from enum ENUM_BITMAP_LAYOUT
	BITMAP_LAYOUT_RIGHT           =2          # from enum ENUM_BITMAP_LAYOUT
	BITMAP_LAYOUT_SIZE_TO_FIT     =255        # from enum ENUM_BITMAP_LAYOUT
	BITMAP_LAYOUT_VCENTER         =8          # from enum ENUM_BITMAP_LAYOUT
	BUTTON_TYPE_ABORT             =3          # from enum ENUM_BUTTON_TYPE
	BUTTON_TYPE_CANCEL            =2          # from enum ENUM_BUTTON_TYPE
	BUTTON_TYPE_CONTINUE          =11         # from enum ENUM_BUTTON_TYPE
	BUTTON_TYPE_HELP              =9          # from enum ENUM_BUTTON_TYPE
	BUTTON_TYPE_IGNORE            =5          # from enum ENUM_BUTTON_TYPE
	BUTTON_TYPE_NO                =7          # from enum ENUM_BUTTON_TYPE
	BUTTON_TYPE_OK                =1          # from enum ENUM_BUTTON_TYPE
	BUTTON_TYPE_RETRY             =4          # from enum ENUM_BUTTON_TYPE
	BUTTON_TYPE_YES               =6          # from enum ENUM_BUTTON_TYPE
	CADPRINT_ENTIRCURSCALE        =3          # from enum ENUM_CADPRINTOPTIONS
	CADPRINT_ENTIREVIEW           =2          # from enum ENUM_CADPRINTOPTIONS
	CADPRINT_ONEPAGESCALE         =0          # from enum ENUM_CADPRINTOPTIONS
	CADPRINT_VISIBLEAREA          =1          # from enum ENUM_CADPRINTOPTIONS
	HCAD_ALL_LISTS                =-1         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM1CMM                  =19         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM1CMM1                 =20         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM1CMM2                 =21         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM1CMM3                 =22         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM1CMM4                 =23         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM1CMM5                 =24         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM1CMM6                 =25         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM1PROBE                =26         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM1PROBE1               =27         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM1PROBE2               =28         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM1PROBE3               =29         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM2CMM                  =8          # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM2CMM1                 =9          # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM2CMM2                 =10         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM2CMM3                 =11         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM2CMM4                 =12         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM2CMM5                 =13         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM2CMM6                 =14         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM2PROBE                =15         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM2PROBE1               =16         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM2PROBE2               =17         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM2PROBE3               =18         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM3CMM                  =63         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM3CMM1                 =64         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM3CMM2                 =65         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM3CMM3                 =66         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM3CMM4                 =67         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM3CMM5                 =68         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM3CMM6                 =69         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM3PROBE                =77         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM3PROBE1               =78         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM3PROBE2               =79         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM3PROBE3               =80         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM4CMM                  =70         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM4CMM1                 =71         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM4CMM2                 =72         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM4CMM3                 =73         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM4CMM4                 =74         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM4CMM5                 =75         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM4CMM6                 =76         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM4PROBE                =81         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM4PROBE1               =82         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM4PROBE2               =83         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARM4PROBE3               =84         # from enum ENUM_CAD_COLLECTIONS
	HCAD_ARROWS                   =5          # from enum ENUM_CAD_COLLECTIONS
	HCAD_CAD                      =0          # from enum ENUM_CAD_COLLECTIONS
	HCAD_CLEARFETS                =-2         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE               =30         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE1              =31         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE10             =40         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE11             =41         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE12             =42         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE13             =43         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE14             =44         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE15             =45         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE16             =46         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE17             =47         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE18             =48         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE19             =49         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE2              =32         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE20             =50         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE21             =51         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE22             =52         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE23             =53         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE24             =54         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE25             =55         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE3              =33         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE4              =34         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE5              =35         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE6              =36         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE7              =37         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE8              =38         # from enum ENUM_CAD_COLLECTIONS
	HCAD_CMMFIXTURE9              =39         # from enum ENUM_CAD_COLLECTIONS
	HCAD_EDITPATH                 =4          # from enum ENUM_CAD_COLLECTIONS
	HCAD_FOV                      =57         # from enum ENUM_CAD_COLLECTIONS
	HCAD_HITS                     =7          # from enum ENUM_CAD_COLLECTIONS
	HCAD_INSPECTP                 =2          # from enum ENUM_CAD_COLLECTIONS
	HCAD_MARKERS                  =56         # from enum ENUM_CAD_COLLECTIONS
	HCAD_MEASURED                 =3          # from enum ENUM_CAD_COLLECTIONS
	HCAD_PROBECHANGER1            =59         # from enum ENUM_CAD_COLLECTIONS
	HCAD_PROBECHANGER2            =60         # from enum ENUM_CAD_COLLECTIONS
	HCAD_PROBECHANGER3            =61         # from enum ENUM_CAD_COLLECTIONS
	HCAD_PROBECHANGER4            =62         # from enum ENUM_CAD_COLLECTIONS
	HCAD_SCAN                     =6          # from enum ENUM_CAD_COLLECTIONS
	HCAD_SURF                     =1          # from enum ENUM_CAD_COLLECTIONS
	HCAD_TARGET                   =58         # from enum ENUM_CAD_COLLECTIONS
	CAD_ALL_GEOMETRY              =7          # from enum ENUM_CAD_GEOMETRY_FILTER_FLAGS
	CAD_CURVE_GEOMETRY            =2          # from enum ENUM_CAD_GEOMETRY_FILTER_FLAGS
	CAD_POINT_GEOMETRY            =1          # from enum ENUM_CAD_GEOMETRY_FILTER_FLAGS
	CAD_SURFACE_GEOMETRY          =4          # from enum ENUM_CAD_GEOMETRY_FILTER_FLAGS
	CAD_INTERSECT_CLOSEST_ORIGIN  =1          # from enum ENUM_CAD_LINE_INTERSECT_FLAGS
	CAD_POSITIVE_PARAMETER_INTERSECTIONS_ONLY=2          # from enum ENUM_CAD_LINE_INTERSECT_FLAGS
	CAD_ACCESS_FAIL               =-1         # from enum ENUM_CAD_RESULT
	CAD_GEOMETRY_FAIL             =0          # from enum ENUM_CAD_RESULT
	CAD_GEOMETRY_HIT              =2          # from enum ENUM_CAD_RESULT
	CAD_GEOMETRY_MISS             =1          # from enum ENUM_CAD_RESULT
	CAD_SURFACE_BOUNDARIES        =1          # from enum ENUM_CAD_SURFACE_BOUNDARY_OPTION
	CAD_SURFACE_DEFAULT           =0          # from enum ENUM_CAD_SURFACE_BOUNDARY_OPTION
	CAD_SURFACE_OUTER_BOUNDARIES  =2          # from enum ENUM_CAD_SURFACE_BOUNDARY_OPTION
	CAD_RETURN_NORMAL_TO_CURVES   =1          # from enum ENUM_CAD_VECTOR_OPTION
	CAD_RETURN_TANGENT_TO_CURVES  =0          # from enum ENUM_CAD_VECTOR_OPTION
	CALIBRATE_NC100_ARTIFACT      =5          # from enum ENUM_CALIBRATION_EXECUTE_MODE
	CALIBRATE_TIPS                =0          # from enum ENUM_CALIBRATION_EXECUTE_MODE
	CALIBRATE_UNIT                =1          # from enum ENUM_CALIBRATION_EXECUTE_MODE
	HOME_UNIT                     =4          # from enum ENUM_CALIBRATION_EXECUTE_MODE
	QUALIFICATION_CHECK           =3          # from enum ENUM_CALIBRATION_EXECUTE_MODE
	COLOR_SECTION_ALIGNMENT       =10002      # from enum ENUM_COLOR_SECTION
	COLOR_SECTION_AUTO            =10015      # from enum ENUM_COLOR_SECTION
	COLOR_SECTION_CONSTRUCTED     =10008      # from enum ENUM_COLOR_SECTION
	COLOR_SECTION_DEFAULT         =10001      # from enum ENUM_COLOR_SECTION
	COLOR_SECTION_DIMENSIONS      =10010      # from enum ENUM_COLOR_SECTION
	COLOR_SECTION_FEATURES        =10003      # from enum ENUM_COLOR_SECTION
	COLOR_SECTION_FLOW            =10012      # from enum ENUM_COLOR_SECTION
	COLOR_SECTION_GENERIC         =10009      # from enum ENUM_COLOR_SECTION
	COLOR_SECTION_HITS            =10004      # from enum ENUM_COLOR_SECTION
	COLOR_SECTION_LASER           =10007      # from enum ENUM_COLOR_SECTION
	COLOR_SECTION_MEASURED        =10005      # from enum ENUM_COLOR_SECTION
	COLOR_SECTION_MISC            =10014      # from enum ENUM_COLOR_SECTION
	COLOR_SECTION_MOVE            =10011      # from enum ENUM_COLOR_SECTION
	COLOR_SECTION_PARAMETERS      =10013      # from enum ENUM_COLOR_SECTION
	COLOR_SECTION_VISION          =10006      # from enum ENUM_COLOR_SECTION
	CMD_ROT_HEAD                  =80         # from enum ENUM_COMMANDNUMBER
	CMM_SN                        =60         # from enum ENUM_COMMANDNUMBER
	DISCONNECT                    =52         # from enum ENUM_COMMANDNUMBER
	GET_PART_TEMP                 =71         # from enum ENUM_COMMANDNUMBER
	MODE_AUTO                     =1          # from enum ENUM_COMMANDNUMBER
	MODE_MAN                      =0          # from enum ENUM_COMMANDNUMBER
	PARK                          =50         # from enum ENUM_COMMANDNUMBER
	READIOBITS                    =30         # from enum ENUM_COMMANDNUMBER
	RECONNECT                     =53         # from enum ENUM_COMMANDNUMBER
	SETIOBITS                     =40         # from enum ENUM_COMMANDNUMBER
	SET_PART_TEMP                 =70         # from enum ENUM_COMMANDNUMBER
	SET_VISUAL                    =62         # from enum ENUM_COMMANDNUMBER
	UNPARK                        =51         # from enum ENUM_COMMANDNUMBER
	USE_PARAMETER_SET             =61         # from enum ENUM_COMMANDNUMBER
	DIMAXIS_NONE                  =0          # from enum ENUM_DIM_AXISTYPE
	DIMAXIS_XAXIS                 =1          # from enum ENUM_DIM_AXISTYPE
	DIMAXIS_YAXIS                 =2          # from enum ENUM_DIM_AXISTYPE
	DIMAXIS_ZAXIS                 =3          # from enum ENUM_DIM_AXISTYPE
	DIMOUTPUT_BOTH                =2          # from enum ENUM_DIM_OUTPUTTYPE
	DIMOUTPUT_NONE                =3          # from enum ENUM_DIM_OUTPUTTYPE
	DIMOUTPUT_REPORT              =1          # from enum ENUM_DIM_OUTPUTTYPE
	DIMOUTPUT_STATS               =0          # from enum ENUM_DIM_OUTPUTTYPE
	DIM_PARALLEL                  =1          # from enum ENUM_DIM_PERP_PARALLEL
	DIM_PERPENDICULAR             =0          # from enum ENUM_DIM_PERP_PARALLEL
	DIM_PROF_FORM_AND_LOCATION    =1          # from enum ENUM_DIM_PROF_TYPE
	DIM_PROF_FORM_ONLY            =0          # from enum ENUM_DIM_PROF_TYPE
	DIM_ADD_RADIUS                =1          # from enum ENUM_DIM_RADIUS_TYPE
	DIM_NO_RADIUS                 =0          # from enum ENUM_DIM_RADIUS_TYPE
	DIM_SUB_RADIUS                =2          # from enum ENUM_DIM_RADIUS_TYPE
	DIM_LMC_CONDITION             =2          # from enum ENUM_DIM_TP_MATERIAL_CONDITION
	DIM_MMC_CONDITION             =0          # from enum ENUM_DIM_TP_MATERIAL_CONDITION
	DIM_RFS_CONDITION             =1          # from enum ENUM_DIM_TP_MATERIAL_CONDITION
	DIM_LMC_LMC                   =8          # from enum ENUM_DIM_TP_MODIFIER
	DIM_LMC_MMC                   =7          # from enum ENUM_DIM_TP_MODIFIER
	DIM_LMC_RFS                   =6          # from enum ENUM_DIM_TP_MODIFIER
	DIM_MMC_LMC                   =5          # from enum ENUM_DIM_TP_MODIFIER
	DIM_MMC_MMC                   =4          # from enum ENUM_DIM_TP_MODIFIER
	DIM_MMC_RFS                   =3          # from enum ENUM_DIM_TP_MODIFIER
	DIM_RFS_LMC                   =2          # from enum ENUM_DIM_TP_MODIFIER
	DIM_RFS_MMC                   =1          # from enum ENUM_DIM_TP_MODIFIER
	DIM_RFS_RFS                   =0          # from enum ENUM_DIM_TP_MODIFIER
	DIM_AXIS_AVERAGE              =0          # from enum ENUM_DIM_TP_USE_AXIS
	DIM_AXIS_END_POINT            =2          # from enum ENUM_DIM_TP_USE_AXIS
	DIM_AXIS_START_POINT          =1          # from enum ENUM_DIM_TP_USE_AXIS
	DINFO_DEV                     =4          # from enum ENUM_DINFO_FIELD_TYPES
	DINFO_MAXMIN                  =5          # from enum ENUM_DINFO_FIELD_TYPES
	DINFO_MEAN                    =7          # from enum ENUM_DINFO_FIELD_TYPES
	DINFO_MEAS                    =1          # from enum ENUM_DINFO_FIELD_TYPES
	DINFO_NOM                     =2          # from enum ENUM_DINFO_FIELD_TYPES
	DINFO_NOT_USED                =0          # from enum ENUM_DINFO_FIELD_TYPES
	DINFO_NUMPOINTS               =9          # from enum ENUM_DINFO_FIELD_TYPES
	DINFO_OUTTOL                  =6          # from enum ENUM_DINFO_FIELD_TYPES
	DINFO_STDDEV                  =8          # from enum ENUM_DINFO_FIELD_TYPES
	DINFO_TOL                     =3          # from enum ENUM_DINFO_FIELD_TYPES
	DINFO_LOC_A                   =7          # from enum ENUM_DINFO_LOC_AXES
	DINFO_LOC_D                   =4          # from enum ENUM_DINFO_LOC_AXES
	DINFO_LOC_H                   =9          # from enum ENUM_DINFO_LOC_AXES
	DINFO_LOC_L                   =8          # from enum ENUM_DINFO_LOC_AXES
	DINFO_LOC_NOT_USED            =0          # from enum ENUM_DINFO_LOC_AXES
	DINFO_LOC_PA                  =11         # from enum ENUM_DINFO_LOC_AXES
	DINFO_LOC_PD                  =16         # from enum ENUM_DINFO_LOC_AXES
	DINFO_LOC_PR                  =10         # from enum ENUM_DINFO_LOC_AXES
	DINFO_LOC_R                   =5          # from enum ENUM_DINFO_LOC_AXES
	DINFO_LOC_RS                  =15         # from enum ENUM_DINFO_LOC_AXES
	DINFO_LOC_RT                  =13         # from enum ENUM_DINFO_LOC_AXES
	DINFO_LOC_S                   =14         # from enum ENUM_DINFO_LOC_AXES
	DINFO_LOC_T                   =12         # from enum ENUM_DINFO_LOC_AXES
	DINFO_LOC_USE_DIM_AXES        =-2         # from enum ENUM_DINFO_LOC_AXES
	DINFO_LOC_V                   =6          # from enum ENUM_DINFO_LOC_AXES
	DINFO_LOC_WORST               =-1         # from enum ENUM_DINFO_LOC_AXES
	DINFO_LOC_X                   =1          # from enum ENUM_DINFO_LOC_AXES
	DINFO_LOC_Y                   =2          # from enum ENUM_DINFO_LOC_AXES
	DINFO_LOC_Z                   =3          # from enum ENUM_DINFO_LOC_AXES
	DINFO_TP_DD                   =6          # from enum ENUM_DINFO_TP_AXES
	DINFO_TP_DF                   =9          # from enum ENUM_DINFO_TP_AXES
	DINFO_TP_LD                   =7          # from enum ENUM_DINFO_TP_AXES
	DINFO_TP_LF                   =10         # from enum ENUM_DINFO_TP_AXES
	DINFO_TP_NOT_USED             =0          # from enum ENUM_DINFO_TP_AXES
	DINFO_TP_PA                   =5          # from enum ENUM_DINFO_TP_AXES
	DINFO_TP_PR                   =4          # from enum ENUM_DINFO_TP_AXES
	DINFO_TP_TP                   =12         # from enum ENUM_DINFO_TP_AXES
	DINFO_TP_USE_DIM_AXES         =-2         # from enum ENUM_DINFO_TP_AXES
	DINFO_TP_WD                   =8          # from enum ENUM_DINFO_TP_AXES
	DINFO_TP_WF                   =11         # from enum ENUM_DINFO_TP_AXES
	DINFO_TP_WORST                =-1         # from enum ENUM_DINFO_TP_AXES
	DINFO_TP_X                    =1          # from enum ENUM_DINFO_TP_AXES
	DINFO_TP_Y                    =2          # from enum ENUM_DINFO_TP_AXES
	DINFO_TP_Z                    =3          # from enum ENUM_DINFO_TP_AXES
	PCD_DMIS_OUTPUT_THEOS_ALL     =1          # from enum ENUM_DMIS_OUTPUT_THEOS
	PCD_DMIS_OUTPUT_THEOS_NONE    =0          # from enum ENUM_DMIS_OUTPUT_THEOS
	PCD_DMIS_OUTPUT_THEOS_USE_IMPORTED_SETTING=2          # from enum ENUM_DMIS_OUTPUT_THEOS
	PCD_DMIS_FILE_ADD_INDEX       =0          # from enum ENUM_DMIS_OVERWRITE
	PCD_DMIS_FILE_APPEND          =2          # from enum ENUM_DMIS_OVERWRITE
	PCD_DMIS_FILE_OVERWRITE       =1          # from enum ENUM_DMIS_OVERWRITE
	DTYPE_DO_NOT_STORE            =0          # from enum ENUM_DTYPE_GETDBTYPE
	DTYPE_DYNAMIC_DATA            =1          # from enum ENUM_DTYPE_GETDBTYPE
	DTYPE_GETDBTYPE_ERROR         =-1         # from enum ENUM_DTYPE_GETDBTYPE
	DTYPE_STATIC_DATA             =2          # from enum ENUM_DTYPE_GETDBTYPE
	DTYPE_DOUBLE                  =2          # from enum ENUM_DTYPE_GETVARIABLETYPE
	DTYPE_GETVARIABLETYPE_ERROR   =-1         # from enum ENUM_DTYPE_GETVARIABLETYPE
	DTYPE_LONG                    =1          # from enum ENUM_DTYPE_GETVARIABLETYPE
	DTYPE_TEXT                    =0          # from enum ENUM_DTYPE_GETVARIABLETYPE
	ERROR_MODE_GOTO_LABEL         =1          # from enum ENUM_ERROR_MODES
	ERROR_MODE_LASER_SKIP         =1          # from enum ENUM_ERROR_MODES
	ERROR_MODE_OFF                =0          # from enum ENUM_ERROR_MODES
	ERROR_MODE_SET_VARIABLE       =2          # from enum ENUM_ERROR_MODES
	ERROR_MODE_SKIP               =3          # from enum ENUM_ERROR_MODES
	ERROR_TYPE_EDGE_NOT_DETECTED  =3          # from enum ENUM_ERROR_TYPES
	ERROR_TYPE_FOCUS_NOT_DETECTED =4          # from enum ENUM_ERROR_TYPES
	ERROR_TYPE_LASER_ERROR        =5          # from enum ENUM_ERROR_TYPES
	ERROR_TYPE_MISSED_HIT         =1          # from enum ENUM_ERROR_TYPES
	ERROR_TYPE_REFLECTOR_NOT_FOUND=2          # from enum ENUM_ERROR_TYPES
	ERROR_TYPE_UNEXPECTED_HIT     =0          # from enum ENUM_ERROR_TYPES
	FEATREF_3D                    =-2         # from enum ENUM_FEATREF_TYPES
	FEATREF_CURRENT_WORKPLANE     =-1         # from enum ENUM_FEATREF_TYPES
	FEATREF_FEATURE               =-3         # from enum ENUM_FEATREF_TYPES
	FEATREF_XMINUS                =4          # from enum ENUM_FEATREF_TYPES
	FEATREF_XPLUS                 =1          # from enum ENUM_FEATREF_TYPES
	FEATREF_YMINUS                =5          # from enum ENUM_FEATREF_TYPES
	FEATREF_YPLUS                 =2          # from enum ENUM_FEATREF_TYPES
	FEATREF_ZMINUS                =3          # from enum ENUM_FEATREF_TYPES
	FEATREF_ZPLUS                 =0          # from enum ENUM_FEATREF_TYPES
	F_CIRCLE                      =2          # from enum ENUM_FEATURE_TYPES
	F_CONE                        =5          # from enum ENUM_FEATURE_TYPES
	F_CURVE                       =8          # from enum ENUM_FEATURE_TYPES
	F_CYLINDER                    =6          # from enum ENUM_FEATURE_TYPES
	F_ELLIPSE                     =11         # from enum ENUM_FEATURE_TYPES
	F_LINE                        =4          # from enum ENUM_FEATURE_TYPES
	F_NONE                        =0          # from enum ENUM_FEATURE_TYPES
	F_PLANE                       =7          # from enum ENUM_FEATURE_TYPES
	F_POINT                       =1          # from enum ENUM_FEATURE_TYPES
	F_SET                         =10         # from enum ENUM_FEATURE_TYPES
	F_SLOT                        =9          # from enum ENUM_FEATURE_TYPES
	F_SPHERE                      =3          # from enum ENUM_FEATURE_TYPES
	F_SURFACE                     =12         # from enum ENUM_FEATURE_TYPES
	F_WIDTH2D                     =22         # from enum ENUM_FEATURE_TYPES
	F_WIDTH3D                     =21         # from enum ENUM_FEATURE_TYPES
	FIELD_DATA_DOUBLE             =2          # from enum ENUM_FIELD_DATA_TYPES
	FIELD_DATA_LONG               =1          # from enum ENUM_FIELD_DATA_TYPES
	FIELD_DATA_NOTDEFINED         =-1         # from enum ENUM_FIELD_DATA_TYPES
	FIELD_DATA_TEXT               =0          # from enum ENUM_FIELD_DATA_TYPES
	ABBE                          =1112       # from enum ENUM_FIELD_TYPES
	ABOVEBELOW_CONFIG             =481        # from enum ENUM_FIELD_TYPES
	ADDITIONAL_CHART              =409        # from enum ENUM_FIELD_TYPES
	ALIGN_LIST                    =153        # from enum ENUM_FIELD_TYPES
	ANGLE_COMP_TOGGLE             =300        # from enum ENUM_FIELD_TYPES
	ANGLE_OFFSET                  =149        # from enum ENUM_FIELD_TYPES
	ANGLE_OFFSET_2                =597        # from enum ENUM_FIELD_TYPES
	ANGULARITY_NOM_ANGLE          =373        # from enum ENUM_FIELD_TYPES
	ANGVEC_I                      =103        # from enum ENUM_FIELD_TYPES
	ANGVEC_J                      =104        # from enum ENUM_FIELD_TYPES
	ANGVEC_K                      =105        # from enum ENUM_FIELD_TYPES
	ARROW_DENSITY                 =886        # from enum ENUM_FIELD_TYPES
	ARROW_MULTIPLIER              =164        # from enum ENUM_FIELD_TYPES
	ARTICULATEDARM_TYPE           =479        # from enum ENUM_FIELD_TYPES
	AUTOBEEPING                   =295        # from enum ENUM_FIELD_TYPES
	AUTOFIT_CONSTRAINT            =52         # from enum ENUM_FIELD_TYPES
	AUTOTOLZONE                   =298        # from enum ENUM_FIELD_TYPES
	AUTOTRIGGERONOFF              =294        # from enum ENUM_FIELD_TYPES
	AUTO_CLEAR_PLANE              =234        # from enum ENUM_FIELD_TYPES
	AUTO_DEV_DIRECTION            =792        # from enum ENUM_FIELD_TYPES
	AUTO_EXPOSURE                 =1120       # from enum ENUM_FIELD_TYPES
	AUTO_INTENSITY                =1121       # from enum ENUM_FIELD_TYPES
	AUTO_ONERROR_TYPE             =461        # from enum ENUM_FIELD_TYPES
	AUTO_PH9                      =533        # from enum ENUM_FIELD_TYPES
	AUTO_PRINT                    =219        # from enum ENUM_FIELD_TYPES
	AUTO_ROTARY                   =831        # from enum ENUM_FIELD_TYPES
	AVERAGE_ERROR                 =140        # from enum ENUM_FIELD_TYPES
	AXIS                          =132        # from enum ENUM_FIELD_TYPES
	AXIS_DESCRIPTION              =749        # from enum ENUM_FIELD_TYPES
	AXIS_MINUS_TOL                =747        # from enum ENUM_FIELD_TYPES
	AXIS_NOMINAL                  =748        # from enum ENUM_FIELD_TYPES
	AXIS_PLUS_TOL                 =746        # from enum ENUM_FIELD_TYPES
	BA_FEATURE                    =814        # from enum ENUM_FIELD_TYPES
	BA_FEAT_APEX_ANGLE            =818        # from enum ENUM_FIELD_TYPES
	BA_FEAT_DEV3D                 =825        # from enum ENUM_FIELD_TYPES
	BA_FEAT_DEV_X                 =822        # from enum ENUM_FIELD_TYPES
	BA_FEAT_DEV_Y                 =823        # from enum ENUM_FIELD_TYPES
	BA_FEAT_DEV_Z                 =824        # from enum ENUM_FIELD_TYPES
	BA_FEAT_POINTING_ERR          =817        # from enum ENUM_FIELD_TYPES
	BA_FEAT_RMS                   =816        # from enum ENUM_FIELD_TYPES
	BA_FEAT_SOURCE                =815        # from enum ENUM_FIELD_TYPES
	BA_FEAT_X                     =819        # from enum ENUM_FIELD_TYPES
	BA_FEAT_Y                     =820        # from enum ENUM_FIELD_TYPES
	BA_FEAT_Z                     =821        # from enum ENUM_FIELD_TYPES
	BA_RMS                        =803        # from enum ENUM_FIELD_TYPES
	BA_SOLUTION_OPTIONS           =800        # from enum ENUM_FIELD_TYPES
	BA_SOLUTION_STATUS            =801        # from enum ENUM_FIELD_TYPES
	BA_SOLUTION_TYPE              =799        # from enum ENUM_FIELD_TYPES
	BA_STATION                    =805        # from enum ENUM_FIELD_TYPES
	BA_STATION_LOCKED             =813        # from enum ENUM_FIELD_TYPES
	BA_STATION_ORIENTED           =812        # from enum ENUM_FIELD_TYPES
	BA_STATION_ROTX               =809        # from enum ENUM_FIELD_TYPES
	BA_STATION_ROTY               =810        # from enum ENUM_FIELD_TYPES
	BA_STATION_ROTZ               =811        # from enum ENUM_FIELD_TYPES
	BA_STATION_X                  =806        # from enum ENUM_FIELD_TYPES
	BA_STATION_Y                  =807        # from enum ENUM_FIELD_TYPES
	BA_STATION_Z                  =808        # from enum ENUM_FIELD_TYPES
	BA_VARIANCE                   =802        # from enum ENUM_FIELD_TYPES
	BA_WARNINGS                   =804        # from enum ENUM_FIELD_TYPES
	BF_MATH_TYPE                  =51         # from enum ENUM_FIELD_TYPES
	BOUNDARY_OFFSET               =967        # from enum ENUM_FIELD_TYPES
	BOUNDARY_POINT_X              =360        # from enum ENUM_FIELD_TYPES
	BOUNDARY_POINT_Y              =361        # from enum ENUM_FIELD_TYPES
	BOUNDARY_POINT_Z              =362        # from enum ENUM_FIELD_TYPES
	BOUND_TYPE                    =50         # from enum ENUM_FIELD_TYPES
	BSMETHOD_TYPE                 =476        # from enum ENUM_FIELD_TYPES
	BUFFER_SIZE_TYPE              =207        # from enum ENUM_FIELD_TYPES
	CAD_COMP                      =492        # from enum ENUM_FIELD_TYPES
	CAD_GRAPH_ANALYSIS            =1063       # from enum ENUM_FIELD_TYPES
	CAD_PLANAR_SEGREGATION_OFFSET =925        # from enum ENUM_FIELD_TYPES
	CAD_TOLERANCE                 =237        # from enum ENUM_FIELD_TYPES
	CALC_STYLE_FILE               =471        # from enum ENUM_FIELD_TYPES
	CENTER_POINT                  =413        # from enum ENUM_FIELD_TYPES
	CENTER_ROTATION_MEAS          =478        # from enum ENUM_FIELD_TYPES
	CENTER_ROTATION_THEO          =477        # from enum ENUM_FIELD_TYPES
	CHART_SUB_TYPE                =445        # from enum ENUM_FIELD_TYPES
	CHART_TYPE                    =388        # from enum ENUM_FIELD_TYPES
	CHECK_COLLISION               =1124       # from enum ENUM_FIELD_TYPES
	CIRC_TYPE                     =42         # from enum ENUM_FIELD_TYPES
	CLEARANCE_DISTANCE            =1082       # from enum ENUM_FIELD_TYPES
	CLOCK_WISE                    =1023       # from enum ENUM_FIELD_TYPES
	COL132_TYPE                   =244        # from enum ENUM_FIELD_TYPES
	COLUMN_ID                     =296        # from enum ENUM_FIELD_TYPES
	COMMAND_STRING                =245        # from enum ENUM_FIELD_TYPES
	COMMAND_TYPE                  =790        # from enum ENUM_FIELD_TYPES
	COMMENT_FIELD                 =189        # from enum ENUM_FIELD_TYPES
	COMMENT_INPUT                 =709        # from enum ENUM_FIELD_TYPES
	COMMENT_TYPE                  =190        # from enum ENUM_FIELD_TYPES
	COMPOSITE                     =724        # from enum ENUM_FIELD_TYPES
	CONE_CONVEX_TYPE              =468        # from enum ENUM_FIELD_TYPES
	CONE_LENGTH_ANGLE_TYPE        =60         # from enum ENUM_FIELD_TYPES
	CONICAL_CONTROL_ELEMENT       =926        # from enum ENUM_FIELD_TYPES
	CONICITY_CIRCULARITY          =1069       # from enum ENUM_FIELD_TYPES
	CONICITY_CIRCULARITY_TOGGLE   =1070       # from enum ENUM_FIELD_TYPES
	CONSTRAINT_TYPE               =1031       # from enum ENUM_FIELD_TYPES
	CONTROL_ELEMENT               =1007       # from enum ENUM_FIELD_TYPES
	COORD_TYPE                    =39         # from enum ENUM_FIELD_TYPES
	COP_BOOLEANTYPE               =621        # from enum ENUM_FIELD_TYPES
	COP_COLORMAP                  =618        # from enum ENUM_FIELD_TYPES
	COP_COPLEMENT                 =619        # from enum ENUM_FIELD_TYPES
	COP_EXPORTFILETYPE            =616        # from enum ENUM_FIELD_TYPES
	COP_FILTER                    =543        # from enum ENUM_FIELD_TYPES
	COP_IMPORTFILETYPE            =622        # from enum ENUM_FIELD_TYPES
	COP_SELECTIONTYPE             =617        # from enum ENUM_FIELD_TYPES
	COP_SIZE                      =544        # from enum ENUM_FIELD_TYPES
	COP_TYPE                      =545        # from enum ENUM_FIELD_TYPES
	CPOINT_DIAM                   =425        # from enum ENUM_FIELD_TYPES
	CPOINT_F_SCANSPEED            =428        # from enum ENUM_FIELD_TYPES
	CPOINT_I                      =422        # from enum ENUM_FIELD_TYPES
	CPOINT_J                      =423        # from enum ENUM_FIELD_TYPES
	CPOINT_K                      =424        # from enum ENUM_FIELD_TYPES
	CPOINT_SCAN_CROSS_TOTAL       =426        # from enum ENUM_FIELD_TYPES
	CPOINT_SCAN_DENSITY           =427        # from enum ENUM_FIELD_TYPES
	CPOINT_TYPE                   =430        # from enum ENUM_FIELD_TYPES
	CPOINT_X                      =419        # from enum ENUM_FIELD_TYPES
	CPOINT_Y                      =420        # from enum ENUM_FIELD_TYPES
	CPOINT_Z                      =421        # from enum ENUM_FIELD_TYPES
	CREATE_WEIGHTS                =433        # from enum ENUM_FIELD_TYPES
	CURVE_TYPE                    =65         # from enum ENUM_FIELD_TYPES
	CUSTOMIZED_DRF                =907        # from enum ENUM_FIELD_TYPES
	CYLINDER_STUD_TYPE            =914        # from enum ENUM_FIELD_TYPES
	DATA_MEM_PAGES                =252        # from enum ENUM_FIELD_TYPES
	DATA_READ_LOCK                =250        # from enum ENUM_FIELD_TYPES
	DATA_WRITE_LOCK               =251        # from enum ENUM_FIELD_TYPES
	DATUM1_MMB_SIZE               =892        # from enum ENUM_FIELD_TYPES
	DATUM1_MMB_SIZE2              =895        # from enum ENUM_FIELD_TYPES
	DATUM1_MODIFIER               =731        # from enum ENUM_FIELD_TYPES
	DATUM1_MODIFIER2              =734        # from enum ENUM_FIELD_TYPES
	DATUM2                        =725        # from enum ENUM_FIELD_TYPES
	DATUM2_MMB_SIZE               =893        # from enum ENUM_FIELD_TYPES
	DATUM2_MMB_SIZE2              =896        # from enum ENUM_FIELD_TYPES
	DATUM2_MODIFIER               =732        # from enum ENUM_FIELD_TYPES
	DATUM2_MODIFIER2              =735        # from enum ENUM_FIELD_TYPES
	DATUM3_MMB_SIZE               =894        # from enum ENUM_FIELD_TYPES
	DATUM3_MMB_SIZE2              =897        # from enum ENUM_FIELD_TYPES
	DATUM3_MODIFIER               =733        # from enum ENUM_FIELD_TYPES
	DATUM3_MODIFIER2              =736        # from enum ENUM_FIELD_TYPES
	DATUM_FEATURE                 =1115       # from enum ENUM_FIELD_TYPES
	DATUM_FOS_DEV                 =1150       # from enum ENUM_FIELD_TYPES
	DATUM_FOS_DEVPERCENT          =1151       # from enum ENUM_FIELD_TYPES
	DATUM_FOS_DEVPERCENT_NOM      =1155       # from enum ENUM_FIELD_TYPES
	DATUM_FOS_FEATNAME            =1145       # from enum ENUM_FIELD_TYPES
	DATUM_FOS_ISBILATERAL         =1153       # from enum ENUM_FIELD_TYPES
	DATUM_FOS_MEAS                =1149       # from enum ENUM_FIELD_TYPES
	DATUM_FOS_MINUSTOL            =1148       # from enum ENUM_FIELD_TYPES
	DATUM_FOS_NOMINAL             =1146       # from enum ENUM_FIELD_TYPES
	DATUM_FOS_OUTTOL              =1152       # from enum ENUM_FIELD_TYPES
	DATUM_FOS_PLUSTOL             =1147       # from enum ENUM_FIELD_TYPES
	DATUM_FOS_USE2DEVIATIONS      =1154       # from enum ENUM_FIELD_TYPES
	DATUM_ID                      =1126       # from enum ENUM_FIELD_TYPES
	DATUM_TYPE                    =1114       # from enum ENUM_FIELD_TYPES
	DATUM_WORKPLANE               =1116       # from enum ENUM_FIELD_TYPES
	DB_CHART_NAME                 =389        # from enum ENUM_FIELD_TYPES
	DB_QUERY_OP                   =386        # from enum ENUM_FIELD_TYPES
	DB_SOURCE_NAME                =387        # from enum ENUM_FIELD_TYPES
	DB_SOURCE_TYPE                =459        # from enum ENUM_FIELD_TYPES
	DEFAULT_PATH_TYPE             =1010       # from enum ENUM_FIELD_TYPES
	DELETE_TYPE                   =539        # from enum ENUM_FIELD_TYPES
	DESCRIPTION                   =203        # from enum ENUM_FIELD_TYPES
	DESCRIPTION2                  =727        # from enum ENUM_FIELD_TYPES
	DEST_EXPR                     =133        # from enum ENUM_FIELD_TYPES
	DEVIATION_ANGLE               =390        # from enum ENUM_FIELD_TYPES
	DEVIATION_SYMBOLS             =180        # from enum ENUM_FIELD_TYPES
	DEV_DIAM                      =353        # from enum ENUM_FIELD_TYPES
	DEV_MAX                       =791        # from enum ENUM_FIELD_TYPES
	DEV_PERPEN_CENTERLINE         =280        # from enum ENUM_FIELD_TYPES
	DEV_THRESHOLD                 =946        # from enum ENUM_FIELD_TYPES
	DEV_X                         =350        # from enum ENUM_FIELD_TYPES
	DEV_Y                         =351        # from enum ENUM_FIELD_TYPES
	DEV_Z                         =352        # from enum ENUM_FIELD_TYPES
	DIAGNOSTICS_TYPE              =536        # from enum ENUM_FIELD_TYPES
	DIGIT_COUNT                   =199        # from enum ENUM_FIELD_TYPES
	DIM_AXIS_ITEM_NUMBER          =786        # from enum ENUM_FIELD_TYPES
	DIM_BONUS                     =324        # from enum ENUM_FIELD_TYPES
	DIM_BOTTOM                    =972        # from enum ENUM_FIELD_TYPES
	DIM_DEVIATION                 =340        # from enum ENUM_FIELD_TYPES
	DIM_HALF_ANGLE                =880        # from enum ENUM_FIELD_TYPES
	DIM_HEADING                   =182        # from enum ENUM_FIELD_TYPES
	DIM_ID                        =304        # from enum ENUM_FIELD_TYPES
	DIM_INFO_LOC                  =160        # from enum ENUM_FIELD_TYPES
	DIM_INFO_ORDER                =159        # from enum ENUM_FIELD_TYPES
	DIM_INFO_TP_LOC               =161        # from enum ENUM_FIELD_TYPES
	DIM_ITEM_NUMBER               =788        # from enum ENUM_FIELD_TYPES
	DIM_LENGTH                    =173        # from enum ENUM_FIELD_TYPES
	DIM_LENGTH2                   =754        # from enum ENUM_FIELD_TYPES
	DIM_MAX                       =332        # from enum ENUM_FIELD_TYPES
	DIM_MEASURED                  =328        # from enum ENUM_FIELD_TYPES
	DIM_MIN                       =336        # from enum ENUM_FIELD_TYPES
	DIM_OUTTOL                    =344        # from enum ENUM_FIELD_TYPES
	DIM_PLANE_PROJECTION_LENGTH   =860        # from enum ENUM_FIELD_TYPES
	DIM_PLANE_PROJECTION_LENGTH2  =861        # from enum ENUM_FIELD_TYPES
	DIM_PLANE_PROJECTION_TYPE     =858        # from enum ENUM_FIELD_TYPES
	DIM_PLANE_PROJECTION_TYPE2    =859        # from enum ENUM_FIELD_TYPES
	DIM_PLANE_PROJECTION_WIDTH    =862        # from enum ENUM_FIELD_TYPES
	DIM_PLANE_PROJECTION_WIDTH2   =863        # from enum ENUM_FIELD_TYPES
	DIM_RPT_COLUMN_HDR            =701        # from enum ENUM_FIELD_TYPES
	DIM_RPT_DATUM                 =703        # from enum ENUM_FIELD_TYPES
	DIM_RPT_DEVPERCENT            =705        # from enum ENUM_FIELD_TYPES
	DIM_RPT_DEVPERCENT2           =739        # from enum ENUM_FIELD_TYPES
	DIM_RPT_DEVPERCENT_NOM        =737        # from enum ENUM_FIELD_TYPES
	DIM_RPT_GRAPHIC               =704        # from enum ENUM_FIELD_TYPES
	DIM_RPT_ISBILATERAL           =706        # from enum ENUM_FIELD_TYPES
	DIM_RPT_ISDATUM               =702        # from enum ENUM_FIELD_TYPES
	DIM_RPT_NUMZONES              =707        # from enum ENUM_FIELD_TYPES
	DIM_RPT_TOLERANCECOLOR1       =917        # from enum ENUM_FIELD_TYPES
	DIM_RPT_TOLERANCECOLOR2       =918        # from enum ENUM_FIELD_TYPES
	DIM_RPT_USETWODEVIATIONS      =738        # from enum ENUM_FIELD_TYPES
	DIM_TEXT                      =177        # from enum ENUM_FIELD_TYPES
	DIM_TEXT_OPTIONS              =178        # from enum ENUM_FIELD_TYPES
	DIM_TOP                       =971        # from enum ENUM_FIELD_TYPES
	DISPLAY_ADVANCED_PARAMETERS   =510        # from enum ENUM_FIELD_TYPES
	DISPLAY_HITS                  =236        # from enum ENUM_FIELD_TYPES
	DISPLAY_ID                    =184        # from enum ENUM_FIELD_TYPES
	DISPLAY_PROBE_PARAMETERS      =607        # from enum ENUM_FIELD_TYPES
	DISPLAY_TRACE                 =256        # from enum ENUM_FIELD_TYPES
	DISPLAY_TRACKER_PARAMETERS    =840        # from enum ENUM_FIELD_TYPES
	DISPLAY_TYPE                  =185        # from enum ENUM_FIELD_TYPES
	DISTANCE                      =155        # from enum ENUM_FIELD_TYPES
	DRF_COLUMN_HDR                =676        # from enum ENUM_FIELD_TYPES
	DRF_ROTATIONX                 =681        # from enum ENUM_FIELD_TYPES
	DRF_ROTATIONY                 =682        # from enum ENUM_FIELD_TYPES
	DRF_ROTATIONZ                 =683        # from enum ENUM_FIELD_TYPES
	DRF_SEGNAME                   =677        # from enum ENUM_FIELD_TYPES
	DRF_SHIFTX                    =678        # from enum ENUM_FIELD_TYPES
	DRF_SHIFTY                    =679        # from enum ENUM_FIELD_TYPES
	DRF_SHIFTZ                    =680        # from enum ENUM_FIELD_TYPES
	DRF_TBLHDR                    =641        # from enum ENUM_FIELD_TYPES
	DTYPE_LEAPFROGFULLPARTIAL     =291        # from enum ENUM_FIELD_TYPES
	DTYPE_LEAPFROGNUMHITS         =290        # from enum ENUM_FIELD_TYPES
	DTYPE_LEAPFROGTYPE            =289        # from enum ENUM_FIELD_TYPES
	ECOND_HUMIDITY                =838        # from enum ENUM_FIELD_TYPES
	ECOND_PRESSURE                =837        # from enum ENUM_FIELD_TYPES
	ECOND_PRESSURE_UNIT           =856        # from enum ENUM_FIELD_TYPES
	ECOND_TEMP                    =836        # from enum ENUM_FIELD_TYPES
	EDGEVEC_MEAS_I                =341        # from enum ENUM_FIELD_TYPES
	EDGEVEC_MEAS_J                =342        # from enum ENUM_FIELD_TYPES
	EDGEVEC_MEAS_K                =343        # from enum ENUM_FIELD_TYPES
	EDGEVEC_TARG_I                =333        # from enum ENUM_FIELD_TYPES
	EDGEVEC_TARG_J                =334        # from enum ENUM_FIELD_TYPES
	EDGEVEC_TARG_K                =335        # from enum ENUM_FIELD_TYPES
	EDGEVEC_THEO_I                =337        # from enum ENUM_FIELD_TYPES
	EDGEVEC_THEO_J                =338        # from enum ENUM_FIELD_TYPES
	EDGEVEC_THEO_K                =339        # from enum ENUM_FIELD_TYPES
	END_ANG                       =99         # from enum ENUM_FIELD_TYPES
	END_NUM                       =144        # from enum ENUM_FIELD_TYPES
	ERROR_LABEL                   =467        # from enum ENUM_FIELD_TYPES
	ERROR_MODE                    =202        # from enum ENUM_FIELD_TYPES
	ERROR_TYPE                    =201        # from enum ENUM_FIELD_TYPES
	EXCLUSION_ZONE                =292        # from enum ENUM_FIELD_TYPES
	EXECUTE                       =293        # from enum ENUM_FIELD_TYPES
	EXPORT_CAD_DEV                =922        # from enum ENUM_FIELD_TYPES
	EXTRUSION                     =852        # from enum ENUM_FIELD_TYPES
	FAIL_ON_EXIST                 =208        # from enum ENUM_FIELD_TYPES
	FASTPROBEMODE                 =908        # from enum ENUM_FIELD_TYPES
	FCF_RUNOUT_TYPE               =867        # from enum ENUM_FIELD_TYPES
	FCF_STANDARD_TYPE             =945        # from enum ENUM_FIELD_TYPES
	FCF_TOL_ZONE_TYPE             =949        # from enum ENUM_FIELD_TYPES
	FEAT_ITEM_NUMBER              =789        # from enum ENUM_FIELD_TYPES
	FEAT_TYPE                     =303        # from enum ENUM_FIELD_TYPES
	FIELD_WIDTH                   =198        # from enum ENUM_FIELD_TYPES
	FILE_COMMAND_TYPE             =206        # from enum ENUM_FIELD_TYPES
	FILE_NAME                     =152        # from enum ENUM_FIELD_TYPES
	FILE_POINTER                  =197        # from enum ENUM_FIELD_TYPES
	FILTER_LINES_TOGGLE           =857        # from enum ENUM_FIELD_TYPES
	FILTER_TYPE                   =472        # from enum ENUM_FIELD_TYPES
	FINDHOLE_TYPE                 =47         # from enum ENUM_FIELD_TYPES
	FINDNOMS_BESTFIT              =527        # from enum ENUM_FIELD_TYPES
	FINDNOMS_ONLYSELECTED         =528        # from enum ENUM_FIELD_TYPES
	FIND_HOLE_PERCENT             =460        # from enum ENUM_FIELD_TYPES
	FIND_NADIR                    =1019       # from enum ENUM_FIELD_TYPES
	FIND_NOMS_TYPE                =233        # from enum ENUM_FIELD_TYPES
	FIND_NOM_AXIS_TYPE            =54         # from enum ENUM_FIELD_TYPES
	FIRST_DIAMETER                =1102       # from enum ENUM_FIELD_TYPES
	FIRST_DIAMETER_OFFSET         =1103       # from enum ENUM_FIELD_TYPES
	FIT                           =452        # from enum ENUM_FIELD_TYPES
	FIXTURE_TOL                   =465        # from enum ENUM_FIELD_TYPES
	FIXTURE_TYPE                  =226        # from enum ENUM_FIELD_TYPES
	FLY_MODE_TYPE                 =246        # from enum ENUM_FIELD_TYPES
	FORM_TOLERANCE                =997        # from enum ENUM_FIELD_TYPES
	FOUR_AXIS_SCANNING            =1098       # from enum ENUM_FIELD_TYPES
	F_AUTOMOVE                    =79         # from enum ENUM_FIELD_TYPES
	F_BOXLENGTH                   =85         # from enum ENUM_FIELD_TYPES
	F_BOXWIDTH                    =84         # from enum ENUM_FIELD_TYPES
	F_CHECK                       =88         # from enum ENUM_FIELD_TYPES
	F_CHECKDISTANCE               =1053       # from enum ENUM_FIELD_TYPES
	F_CIRCRADIN                   =87         # from enum ENUM_FIELD_TYPES
	F_CIRCRADOUT                  =86         # from enum ENUM_FIELD_TYPES
	F_CORNER_RADIUS               =81         # from enum ENUM_FIELD_TYPES
	F_DEPTH                       =78         # from enum ENUM_FIELD_TYPES
	F_ENDING_DEPTH                =787        # from enum ENUM_FIELD_TYPES
	F_END_OFFSET                  =787        # from enum ENUM_FIELD_TYPES
	F_INCREMENT                   =82         # from enum ENUM_FIELD_TYPES
	F_INDENT                      =80         # from enum ENUM_FIELD_TYPES
	F_LOCATION                    =243        # from enum ENUM_FIELD_TYPES
	F_MAXACCELX                   =89         # from enum ENUM_FIELD_TYPES
	F_MAXACCELY                   =90         # from enum ENUM_FIELD_TYPES
	F_MAXACCELZ                   =91         # from enum ENUM_FIELD_TYPES
	F_MINUS_TOL                   =168        # from enum ENUM_FIELD_TYPES
	F_MOVESPEED                   =95         # from enum ENUM_FIELD_TYPES
	F_OFFSET                      =74         # from enum ENUM_FIELD_TYPES
	F_PITCH                       =76         # from enum ENUM_FIELD_TYPES
	F_PLUS_TOL                    =167        # from enum ENUM_FIELD_TYPES
	F_PREHIT                      =1051       # from enum ENUM_FIELD_TYPES
	F_RETRACT                     =1052       # from enum ENUM_FIELD_TYPES
	F_SCANSPEED                   =97         # from enum ENUM_FIELD_TYPES
	F_SIZE                        =434        # from enum ENUM_FIELD_TYPES
	F_SPACER                      =75         # from enum ENUM_FIELD_TYPES
	F_THICKNESS                   =77         # from enum ENUM_FIELD_TYPES
	F_THICKNESS_EDGE              =593        # from enum ENUM_FIELD_TYPES
	F_TOLERANCE                   =83         # from enum ENUM_FIELD_TYPES
	F_TOUCHSPEED                  =96         # from enum ENUM_FIELD_TYPES
	GAGE_SEARCH_ZONE              =1035       # from enum ENUM_FIELD_TYPES
	GAGE_TIP2_HEIGHT              =1059       # from enum ENUM_FIELD_TYPES
	GAGE_TIP2_WIDTH               =1058       # from enum ENUM_FIELD_TYPES
	GAGE_TIP_HEIGHT               =1034       # from enum ENUM_FIELD_TYPES
	GAGE_TIP_SHAPE                =1032       # from enum ENUM_FIELD_TYPES
	GAGE_TIP_WIDTH                =1033       # from enum ENUM_FIELD_TYPES
	GAP_ONLY_TYPE                 =183        # from enum ENUM_FIELD_TYPES
	GDT_SYMBOL                    =708        # from enum ENUM_FIELD_TYPES
	GDT_SYMBOL2                   =730        # from enum ENUM_FIELD_TYPES
	GEN_ALIGN_TYPE                =64         # from enum ENUM_FIELD_TYPES
	GEN_FEAT_TYPE                 =63         # from enum ENUM_FIELD_TYPES
	GRAPH_ANALYSIS                =162        # from enum ENUM_FIELD_TYPES
	GRAPH_ANALYSIS_MINUS_TOL      =785        # from enum ENUM_FIELD_TYPES
	GRAPH_ANALYSIS_PLUS_TOL       =784        # from enum ENUM_FIELD_TYPES
	GRAPH_ANALYSIS_POINT_SIZE     =783        # from enum ENUM_FIELD_TYPES
	GRAPH_OPTION                  =458        # from enum ENUM_FIELD_TYPES
	GRID                          =408        # from enum ENUM_FIELD_TYPES
	HIGH_ACCURACY                 =483        # from enum ENUM_FIELD_TYPES
	HIGH_THRESHOLD                =223        # from enum ENUM_FIELD_TYPES
	HISTOGRAM                     =407        # from enum ENUM_FIELD_TYPES
	HITINT_TYPE                   =68         # from enum ENUM_FIELD_TYPES
	HIT_RMS                       =839        # from enum ENUM_FIELD_TYPES
	HIT_TIMESTAMP                 =854        # from enum ENUM_FIELD_TYPES
	HIT_TYPE                      =359        # from enum ENUM_FIELD_TYPES
	HORIZONTAL_CLIPPING           =899        # from enum ENUM_FIELD_TYPES
	ID                            =2          # from enum ENUM_FIELD_TYPES
	IGNOREMOTIONERRORS_TYPE       =392        # from enum ENUM_FIELD_TYPES
	ILLUM_BULB_INTENSITY_EDGE     =875        # from enum ENUM_FIELD_TYPES
	ILLUM_BULB_INTENSITY_SURFACE  =878        # from enum ENUM_FIELD_TYPES
	ILLUM_CALOVERRIDE_TOGGLE_EDGE =876        # from enum ENUM_FIELD_TYPES
	ILLUM_CALOVERRIDE_TOGGLE_SURFACE=879        # from enum ENUM_FIELD_TYPES
	ILLUM_OFFON_TOGGLE_EDGE       =874        # from enum ENUM_FIELD_TYPES
	ILLUM_OFFON_TOGGLE_SURFACE    =877        # from enum ENUM_FIELD_TYPES
	INCIDENCE_ANGLE               =1039       # from enum ENUM_FIELD_TYPES
	INDEX_END                     =205        # from enum ENUM_FIELD_TYPES
	INDEX_START                   =204        # from enum ENUM_FIELD_TYPES
	INIT_HITS                     =72         # from enum ENUM_FIELD_TYPES
	INLINE_LEGACY_REPORT          =848        # from enum ENUM_FIELD_TYPES
	INNER_SPACER                  =850        # from enum ENUM_FIELD_TYPES
	INOUT_TYPE                    =40         # from enum ENUM_FIELD_TYPES
	INTERNAL_EXTERNAL             =150        # from enum ENUM_FIELD_TYPES
	IOCHANNEL_NUMBER              =454        # from enum ENUM_FIELD_TYPES
	IOCHANNEL_PULSE_DURATION      =457        # from enum ENUM_FIELD_TYPES
	IOCHANNEL_PULSE_INTERVAL      =456        # from enum ENUM_FIELD_TYPES
	IOCHANNEL_PULSE_WIDTH         =455        # from enum ENUM_FIELD_TYPES
	ISLAND_AI                     =634        # from enum ENUM_FIELD_TYPES
	ISLAND_AJ                     =635        # from enum ENUM_FIELD_TYPES
	ISLAND_AK                     =636        # from enum ENUM_FIELD_TYPES
	ISLAND_CLEARANCEDIST          =638        # from enum ENUM_FIELD_TYPES
	ISLAND_DIAM                   =625        # from enum ENUM_FIELD_TYPES
	ISLAND_I                      =631        # from enum ENUM_FIELD_TYPES
	ISLAND_J                      =632        # from enum ENUM_FIELD_TYPES
	ISLAND_K                      =633        # from enum ENUM_FIELD_TYPES
	ISLAND_LENGTH                 =626        # from enum ENUM_FIELD_TYPES
	ISLAND_TYPE                   =637        # from enum ENUM_FIELD_TYPES
	ISLAND_WIDTH                  =627        # from enum ENUM_FIELD_TYPES
	ISLAND_X                      =628        # from enum ENUM_FIELD_TYPES
	ISLAND_Y                      =629        # from enum ENUM_FIELD_TYPES
	ISLAND_Z                      =630        # from enum ENUM_FIELD_TYPES
	ITEM_USED                     =138        # from enum ENUM_FIELD_TYPES
	ITERATE_COLUMNS               =354        # from enum ENUM_FIELD_TYPES
	JUMP_HOLE                     =1013       # from enum ENUM_FIELD_TYPES
	JUMP_HOLE_FLAG                =1012       # from enum ENUM_FIELD_TYPES
	LABEL_ID                      =200        # from enum ENUM_FIELD_TYPES
	LASER_CLIP_LEFT_DIST          =614        # from enum ENUM_FIELD_TYPES
	LASER_CLIP_LOW_DIST           =604        # from enum ENUM_FIELD_TYPES
	LASER_CLIP_RIGHT_DIST         =615        # from enum ENUM_FIELD_TYPES
	LASER_CLIP_UP_DIST            =603        # from enum ENUM_FIELD_TYPES
	LASER_EXPOSURE                =595        # from enum ENUM_FIELD_TYPES
	LASER_FILTER_NEIGHBOR_NUM     =598        # from enum ENUM_FIELD_TYPES
	LASER_FILTER_TOGGLE           =606        # from enum ENUM_FIELD_TYPES
	LASER_FILTER_TOL_ABOVE        =600        # from enum ENUM_FIELD_TYPES
	LASER_FILTER_TOL_BELOW        =601        # from enum ENUM_FIELD_TYPES
	LASER_FILTER_TOL_RIGHT        =602        # from enum ENUM_FIELD_TYPES
	LASER_FREQUENCY               =560        # from enum ENUM_FIELD_TYPES
	LASER_INTENSITY               =596        # from enum ENUM_FIELD_TYPES
	LASER_PIXEL_TOGGLE            =605        # from enum ENUM_FIELD_TYPES
	LASER_STRIPE_OVERLAP          =558        # from enum ENUM_FIELD_TYPES
	LASER_STRIPE_OVERSCAN         =559        # from enum ENUM_FIELD_TYPES
	LEADER_LINE_ID                =729        # from enum ENUM_FIELD_TYPES
	LEFTYRIGHTY_CONFIG            =480        # from enum ENUM_FIELD_TYPES
	LEVEL_REF_ID                  =4          # from enum ENUM_FIELD_TYPES
	LINE1_BONUS                   =782        # from enum ENUM_FIELD_TYPES
	LINE1_CALLOUT                 =643        # from enum ENUM_FIELD_TYPES
	LINE1_COLUMN_HDR              =644        # from enum ENUM_FIELD_TYPES
	LINE1_DEV                     =650        # from enum ENUM_FIELD_TYPES
	LINE1_DEVPERCENT              =651        # from enum ENUM_FIELD_TYPES
	LINE1_DEVPERCENT2             =752        # from enum ENUM_FIELD_TYPES
	LINE1_DEVPERCENT_NOM          =750        # from enum ENUM_FIELD_TYPES
	LINE1_FEATNAME                =645        # from enum ENUM_FIELD_TYPES
	LINE1_ISBILATERAL             =652        # from enum ENUM_FIELD_TYPES
	LINE1_MAX                     =768        # from enum ENUM_FIELD_TYPES
	LINE1_MEAS                    =647        # from enum ENUM_FIELD_TYPES
	LINE1_MIN                     =769        # from enum ENUM_FIELD_TYPES
	LINE1_MINUSTOL                =649        # from enum ENUM_FIELD_TYPES
	LINE1_NOMINAL                 =646        # from enum ENUM_FIELD_TYPES
	LINE1_NUMZONES                =653        # from enum ENUM_FIELD_TYPES
	LINE1_OUTTOL                  =765        # from enum ENUM_FIELD_TYPES
	LINE1_PLUSTOL                 =648        # from enum ENUM_FIELD_TYPES
	LINE1_TBLHDR                  =642        # from enum ENUM_FIELD_TYPES
	LINE1_USE2DEVIATIONS          =751        # from enum ENUM_FIELD_TYPES
	LINE2_AXIS                    =686        # from enum ENUM_FIELD_TYPES
	LINE2_BONUS                   =658        # from enum ENUM_FIELD_TYPES
	LINE2_CALLOUT                 =655        # from enum ENUM_FIELD_TYPES
	LINE2_COLUMN_HDR              =656        # from enum ENUM_FIELD_TYPES
	LINE2_DATUMA_DOF              =901        # from enum ENUM_FIELD_TYPES
	LINE2_DATUMB_DOF              =902        # from enum ENUM_FIELD_TYPES
	LINE2_DATUMC_DOF              =903        # from enum ENUM_FIELD_TYPES
	LINE2_DATUMSHFT               =660        # from enum ENUM_FIELD_TYPES
	LINE2_DEV                     =662        # from enum ENUM_FIELD_TYPES
	LINE2_DEVANG                  =663        # from enum ENUM_FIELD_TYPES
	LINE2_DEVPERCENT              =664        # from enum ENUM_FIELD_TYPES
	LINE2_DEVPERCENT2             =742        # from enum ENUM_FIELD_TYPES
	LINE2_DEVPERCENT_NOM          =740        # from enum ENUM_FIELD_TYPES
	LINE2_FEATNAME                =657        # from enum ENUM_FIELD_TYPES
	LINE2_FEATNAME_PROFILE        =910        # from enum ENUM_FIELD_TYPES
	LINE2_ISBILATERAL             =697        # from enum ENUM_FIELD_TYPES
	LINE2_ISPLANAR                =435        # from enum ENUM_FIELD_TYPES
	LINE2_MAX                     =695        # from enum ENUM_FIELD_TYPES
	LINE2_MEAS                    =688        # from enum ENUM_FIELD_TYPES
	LINE2_MIN                     =696        # from enum ENUM_FIELD_TYPES
	LINE2_MINUSTOL                =694        # from enum ENUM_FIELD_TYPES
	LINE2_NOMINAL                 =687        # from enum ENUM_FIELD_TYPES
	LINE2_NUMZONES                =698        # from enum ENUM_FIELD_TYPES
	LINE2_OUTTOL                  =766        # from enum ENUM_FIELD_TYPES
	LINE2_PLANAR_OPEN_IN_X        =410        # from enum ENUM_FIELD_TYPES
	LINE2_PLANAR_XDEV             =438        # from enum ENUM_FIELD_TYPES
	LINE2_PLANAR_XTOL             =436        # from enum ENUM_FIELD_TYPES
	LINE2_PLANAR_YDEV             =439        # from enum ENUM_FIELD_TYPES
	LINE2_PLANAR_YTOL             =437        # from enum ENUM_FIELD_TYPES
	LINE2_PLUSTOL                 =693        # from enum ENUM_FIELD_TYPES
	LINE2_TBLHDR                  =654        # from enum ENUM_FIELD_TYPES
	LINE2_TOL                     =659        # from enum ENUM_FIELD_TYPES
	LINE2_UNUSEDZONE              =661        # from enum ENUM_FIELD_TYPES
	LINE2_USE2DEVIATIONS          =741        # from enum ENUM_FIELD_TYPES
	LINE3_BONUS                   =669        # from enum ENUM_FIELD_TYPES
	LINE3_CALLOUT                 =666        # from enum ENUM_FIELD_TYPES
	LINE3_COLUMN_HDR              =667        # from enum ENUM_FIELD_TYPES
	LINE3_DATUMA_DOF              =904        # from enum ENUM_FIELD_TYPES
	LINE3_DATUMB_DOF              =905        # from enum ENUM_FIELD_TYPES
	LINE3_DATUMC_DOF              =906        # from enum ENUM_FIELD_TYPES
	LINE3_DATUMSHFT               =671        # from enum ENUM_FIELD_TYPES
	LINE3_DEV                     =673        # from enum ENUM_FIELD_TYPES
	LINE3_DEVANG                  =674        # from enum ENUM_FIELD_TYPES
	LINE3_DEVPERCENT              =675        # from enum ENUM_FIELD_TYPES
	LINE3_DEVPERCENT2             =745        # from enum ENUM_FIELD_TYPES
	LINE3_DEVPERCENT_NOM          =743        # from enum ENUM_FIELD_TYPES
	LINE3_FEATNAME                =668        # from enum ENUM_FIELD_TYPES
	LINE3_ISBILATERAL             =699        # from enum ENUM_FIELD_TYPES
	LINE3_ISPLANAR                =440        # from enum ENUM_FIELD_TYPES
	LINE3_MAX                     =774        # from enum ENUM_FIELD_TYPES
	LINE3_MEAS                    =771        # from enum ENUM_FIELD_TYPES
	LINE3_MIN                     =775        # from enum ENUM_FIELD_TYPES
	LINE3_MINUSTOL                =773        # from enum ENUM_FIELD_TYPES
	LINE3_NOMINAL                 =770        # from enum ENUM_FIELD_TYPES
	LINE3_NUMZONES                =700        # from enum ENUM_FIELD_TYPES
	LINE3_OUTTOL                  =767        # from enum ENUM_FIELD_TYPES
	LINE3_PLANAR_OPEN_IN_X        =411        # from enum ENUM_FIELD_TYPES
	LINE3_PLANAR_XDEV             =443        # from enum ENUM_FIELD_TYPES
	LINE3_PLANAR_XTOL             =441        # from enum ENUM_FIELD_TYPES
	LINE3_PLANAR_YDEV             =444        # from enum ENUM_FIELD_TYPES
	LINE3_PLANAR_YTOL             =442        # from enum ENUM_FIELD_TYPES
	LINE3_PLUSTOL                 =772        # from enum ENUM_FIELD_TYPES
	LINE3_TBLHDR                  =665        # from enum ENUM_FIELD_TYPES
	LINE3_TOL                     =670        # from enum ENUM_FIELD_TYPES
	LINE3_UNUSEDZONE              =672        # from enum ENUM_FIELD_TYPES
	LINE3_USE2DEVIATIONS          =744        # from enum ENUM_FIELD_TYPES
	LIN_POL_FILT_TYPE             =62         # from enum ENUM_FIELD_TYPES
	LOAD_TYPE                     =355        # from enum ENUM_FIELD_TYPES
	LOCAL_SIZE_OPTION             =1122       # from enum ENUM_FIELD_TYPES
	LOCATION_TOLERANCE            =1004       # from enum ENUM_FIELD_TYPES
	LOCATOR_BMP                   =287        # from enum ENUM_FIELD_TYPES
	LOCATOR_WAV                   =288        # from enum ENUM_FIELD_TYPES
	LOWER_BOUNDARY                =1130       # from enum ENUM_FIELD_TYPES
	LOWER_MODIFIER                =1046       # from enum ENUM_FIELD_TYPES
	LOWER_SIZE                    =1050       # from enum ENUM_FIELD_TYPES
	LOWER_TOLERANCE               =1044       # from enum ENUM_FIELD_TYPES
	LOW_FORCE                     =210        # from enum ENUM_FIELD_TYPES
	LOW_THRESHOLD                 =224        # from enum ENUM_FIELD_TYPES
	MACHINE_TYPE                  =227        # from enum ENUM_FIELD_TYPES
	MAGNIFICATION                 =485        # from enum ENUM_FIELD_TYPES
	MANUAL_FINE_PROBING           =94         # from enum ENUM_FIELD_TYPES
	MANUAL_PREPOSITION            =534        # from enum ENUM_FIELD_TYPES
	MAN_RETRACT                   =176        # from enum ENUM_FIELD_TYPES
	MATERIAL_COEFFICIENT          =221        # from enum ENUM_FIELD_TYPES
	MAX_ANGLE                     =242        # from enum ENUM_FIELD_TYPES
	MAX_FORCE                     =209        # from enum ENUM_FIELD_TYPES
	MAX_INCREMENT                 =240        # from enum ENUM_FIELD_TYPES
	MAX_THICKNESS                 =1127       # from enum ENUM_FIELD_TYPES
	MEAN                          =491        # from enum ENUM_FIELD_TYPES
	MEASURED_2D3D_TYPE            =66         # from enum ENUM_FIELD_TYPES
	MEASUREMENT_STRATEGY          =919        # from enum ENUM_FIELD_TYPES
	MEASURE_ALL_FEATURES          =141        # from enum ENUM_FIELD_TYPES
	MEASURE_ORDER_TYPE            =59         # from enum ENUM_FIELD_TYPES
	MEASURMENT_STRATEGY           =919        # from enum ENUM_FIELD_TYPES
	MEASVEC_I                     =106        # from enum ENUM_FIELD_TYPES
	MEASVEC_J                     =107        # from enum ENUM_FIELD_TYPES
	MEASVEC_K                     =108        # from enum ENUM_FIELD_TYPES
	MEAS_A                        =569        # from enum ENUM_FIELD_TYPES
	MEAS_A2                       =612        # from enum ENUM_FIELD_TYPES
	MEAS_ANGLE                    =30         # from enum ENUM_FIELD_TYPES
	MEAS_AREA                     =721        # from enum ENUM_FIELD_TYPES
	MEAS_DEPTH                    =556        # from enum ENUM_FIELD_TYPES
	MEAS_DIAM                     =29         # from enum ENUM_FIELD_TYPES
	MEAS_EA                       =584        # from enum ENUM_FIELD_TYPES
	MEAS_EH                       =585        # from enum ENUM_FIELD_TYPES
	MEAS_EI                       =936        # from enum ENUM_FIELD_TYPES
	MEAS_EJ                       =937        # from enum ENUM_FIELD_TYPES
	MEAS_EK                       =938        # from enum ENUM_FIELD_TYPES
	MEAS_END_ANG                  =624        # from enum ENUM_FIELD_TYPES
	MEAS_ER                       =583        # from enum ENUM_FIELD_TYPES
	MEAS_EX                       =313        # from enum ENUM_FIELD_TYPES
	MEAS_EY                       =314        # from enum ENUM_FIELD_TYPES
	MEAS_EZ                       =315        # from enum ENUM_FIELD_TYPES
	MEAS_FLUSH                    =552        # from enum ENUM_FIELD_TYPES
	MEAS_GAP                      =554        # from enum ENUM_FIELD_TYPES
	MEAS_H                        =570        # from enum ENUM_FIELD_TYPES
	MEAS_H2                       =613        # from enum ENUM_FIELD_TYPES
	MEAS_HEIGHT                   =306        # from enum ENUM_FIELD_TYPES
	MEAS_I                        =25         # from enum ENUM_FIELD_TYPES
	MEAS_J                        =26         # from enum ENUM_FIELD_TYPES
	MEAS_K                        =27         # from enum ENUM_FIELD_TYPES
	MEAS_LENGTH                   =28         # from enum ENUM_FIELD_TYPES
	MEAS_MINOR_AXIS               =305        # from enum ENUM_FIELD_TYPES
	MEAS_MINOR_DIAMETER           =921        # from enum ENUM_FIELD_TYPES
	MEAS_PERIMETER                =719        # from enum ENUM_FIELD_TYPES
	MEAS_R                        =568        # from enum ENUM_FIELD_TYPES
	MEAS_R2                       =611        # from enum ENUM_FIELD_TYPES
	MEAS_RADIUS                   =978        # from enum ENUM_FIELD_TYPES
	MEAS_SA                       =581        # from enum ENUM_FIELD_TYPES
	MEAS_SH                       =582        # from enum ENUM_FIELD_TYPES
	MEAS_SI                       =933        # from enum ENUM_FIELD_TYPES
	MEAS_SJ                       =934        # from enum ENUM_FIELD_TYPES
	MEAS_SK                       =935        # from enum ENUM_FIELD_TYPES
	MEAS_SLOTVEC_I                =307        # from enum ENUM_FIELD_TYPES
	MEAS_SLOTVEC_J                =308        # from enum ENUM_FIELD_TYPES
	MEAS_SLOTVEC_K                =309        # from enum ENUM_FIELD_TYPES
	MEAS_SR                       =580        # from enum ENUM_FIELD_TYPES
	MEAS_START_ANG                =623        # from enum ENUM_FIELD_TYPES
	MEAS_SX                       =310        # from enum ENUM_FIELD_TYPES
	MEAS_SY                       =311        # from enum ENUM_FIELD_TYPES
	MEAS_SZ                       =312        # from enum ENUM_FIELD_TYPES
	MEAS_WIDTH                    =316        # from enum ENUM_FIELD_TYPES
	MEAS_X                        =22         # from enum ENUM_FIELD_TYPES
	MEAS_X2                       =396        # from enum ENUM_FIELD_TYPES
	MEAS_Y                        =23         # from enum ENUM_FIELD_TYPES
	MEAS_Y2                       =397        # from enum ENUM_FIELD_TYPES
	MEAS_Z                        =24         # from enum ENUM_FIELD_TYPES
	MEAS_Z2                       =398        # from enum ENUM_FIELD_TYPES
	MERGE                         =1061       # from enum ENUM_FIELD_TYPES
	MESH_COP_TYPE                 =979        # from enum ENUM_FIELD_TYPES
	MESH_HOLE_OPTION_TYPE         =983        # from enum ENUM_FIELD_TYPES
	MESH_MAXLENGTHTRIANGLETOFILLHOLE=987        # from enum ENUM_FIELD_TYPES
	MESH_NOISE_REDUCTION_TYPE     =980        # from enum ENUM_FIELD_TYPES
	MESH_REFINE_DEVIATIONERROR    =982        # from enum ENUM_FIELD_TYPES
	MESH_REFINE_MESH              =991        # from enum ENUM_FIELD_TYPES
	MESH_REFINE_MINTRIANGLESIZE   =990        # from enum ENUM_FIELD_TYPES
	MESH_TRIANGLES_NUM            =988        # from enum ENUM_FIELD_TYPES
	MESH_VERTICES_NUM             =989        # from enum ENUM_FIELD_TYPES
	METHOD_TYPE                   =357        # from enum ENUM_FIELD_TYPES
	MIDPOINT_X                    =100        # from enum ENUM_FIELD_TYPES
	MIDPOINT_Y                    =101        # from enum ENUM_FIELD_TYPES
	MIDPOINT_Z                    =102        # from enum ENUM_FIELD_TYPES
	MINIMUMAVERAGEDISTANCE        =981        # from enum ENUM_FIELD_TYPES
	MINOR_WORD_TOGGLE             =486        # from enum ENUM_FIELD_TYPES
	MIN_ANGLE                     =241        # from enum ENUM_FIELD_TYPES
	MIN_INCREMENT                 =239        # from enum ENUM_FIELD_TYPES
	MODE_TYPE                     =58         # from enum ENUM_FIELD_TYPES
	MODIFIER_LIST                 =1040       # from enum ENUM_FIELD_TYPES
	MOVE_TYPE                     =45         # from enum ENUM_FIELD_TYPES
	NEW_STATS_DIR                 =249        # from enum ENUM_FIELD_TYPES
	NEW_TIP                       =157        # from enum ENUM_FIELD_TYPES
	NOFLIPFLIP_CONFIG             =482        # from enum ENUM_FIELD_TYPES
	NOMINAL                       =166        # from enum ENUM_FIELD_TYPES
	NOMINAL_COLOR                 =321        # from enum ENUM_FIELD_TYPES
	NORM_RELEARN                  =232        # from enum ENUM_FIELD_TYPES
	NO_APPROACH_VECTOR_FLIP       =826        # from enum ENUM_FIELD_TYPES
	NSIGMA_FILTER                 =909        # from enum ENUM_FIELD_TYPES
	NUM_CONTROL_POINTS            =317        # from enum ENUM_FIELD_TYPES
	NUM_FIT_POINTS                =320        # from enum ENUM_FIELD_TYPES
	NUM_ITERATIONS                =356        # from enum ENUM_FIELD_TYPES
	NUM_RETURN_DATA               =215        # from enum ENUM_FIELD_TYPES
	N_CONTROLPOINTS               =429        # from enum ENUM_FIELD_TYPES
	N_HITS                        =70         # from enum ENUM_FIELD_TYPES
	N_INIT_HITS_TYPE              =55         # from enum ENUM_FIELD_TYPES
	N_PERM_HITS_TYPE              =56         # from enum ENUM_FIELD_TYPES
	N_POINTS                      =1080       # from enum ENUM_FIELD_TYPES
	N_RINGS                       =1101       # from enum ENUM_FIELD_TYPES
	N_ROWS                        =71         # from enum ENUM_FIELD_TYPES
	N_SIDES                       =489        # from enum ENUM_FIELD_TYPES
	OFFSET_LINE_METHOD            =61         # from enum ENUM_FIELD_TYPES
	OFFSET_TOLERANCE              =238        # from enum ENUM_FIELD_TYPES
	OFFSET_TYPE                   =1030       # from enum ENUM_FIELD_TYPES
	OLD_TIP                       =156        # from enum ENUM_FIELD_TYPES
	ONOFF_TYPE                    =285        # from enum ENUM_FIELD_TYPES
	OPERATOR_NORM_MATH_TYPE       =1037       # from enum ENUM_FIELD_TYPES
	OPERTYPE                      =620        # from enum ENUM_FIELD_TYPES
	ORIENTATION_ORIGIN_TOGGLE     =976        # from enum ENUM_FIELD_TYPES
	ORIGIN                        =220        # from enum ENUM_FIELD_TYPES
	ORIGIN_REF_ID                 =6          # from enum ENUM_FIELD_TYPES
	OUTER_SPACER                  =851        # from enum ENUM_FIELD_TYPES
	OUTLIER                       =1009       # from enum ENUM_FIELD_TYPES
	OUTPUT_DMIS_REPORT            =449        # from enum ENUM_FIELD_TYPES
	OUTPUT_FEATURE_NOMS           =447        # from enum ENUM_FIELD_TYPES
	OUTPUT_FEAT_W_DIMENS          =448        # from enum ENUM_FIELD_TYPES
	OUTPUT_TO_REPORT              =970        # from enum ENUM_FIELD_TYPES
	OUTPUT_TYPE                   =165        # from enum ENUM_FIELD_TYPES
	OVERRIDE                      =999        # from enum ENUM_FIELD_TYPES
	OVERWRITE                     =446        # from enum ENUM_FIELD_TYPES
	PART_NAME                     =191        # from enum ENUM_FIELD_TYPES
	PATH_TYPE                     =1020       # from enum ENUM_FIELD_TYPES
	PATTERN_TYPE                  =519        # from enum ENUM_FIELD_TYPES
	PAUSE_EXECUTION               =947        # from enum ENUM_FIELD_TYPES
	PERCENTAGE                    =487        # from enum ENUM_FIELD_TYPES
	PERIMETER_BOUNDARY_TYPE       =1011       # from enum ENUM_FIELD_TYPES
	PERM_HITS                     =73         # from enum ENUM_FIELD_TYPES
	PERP_PARALLEL_TYPE            =170        # from enum ENUM_FIELD_TYPES
	PERUNIT_LENGTH                =326        # from enum ENUM_FIELD_TYPES
	PERUNIT_STEPSIZE              =325        # from enum ENUM_FIELD_TYPES
	PERUNIT_WIDTH                 =327        # from enum ENUM_FIELD_TYPES
	PINVEC_I                      =115        # from enum ENUM_FIELD_TYPES
	PINVEC_J                      =116        # from enum ENUM_FIELD_TYPES
	PINVEC_K                      =117        # from enum ENUM_FIELD_TYPES
	PLANE_CONSTRAINT_TYPE         =1036       # from enum ENUM_FIELD_TYPES
	PLAN_CREATE_TIME              =992        # from enum ENUM_FIELD_TYPES
	POINTINFO_FEATURE_OR_DIMENSION_SYMBOL=1117       # from enum ENUM_FIELD_TYPES
	POINTINFO_FEATURE_OR_DIMENSION_TYPE=1118       # from enum ENUM_FIELD_TYPES
	POINTINFO_FILTER_DEVIATION    =380        # from enum ENUM_FIELD_TYPES
	POINTINFO_FILTER_DEVIATION_NUMBER=381        # from enum ENUM_FIELD_TYPES
	POINTINFO_FILTER_INTERVAL     =301        # from enum ENUM_FIELD_TYPES
	POINTINFO_FILTER_INTERVAL_NUMBER=302        # from enum ENUM_FIELD_TYPES
	POINTINFO_FILTER_MINMAX       =1022       # from enum ENUM_FIELD_TYPES
	POINTINFO_FILTER_OUTTOL       =382        # from enum ENUM_FIELD_TYPES
	POINTINFO_FILTER_WORST        =378        # from enum ENUM_FIELD_TYPES
	POINTINFO_FILTER_WORST_NUMBER =379        # from enum ENUM_FIELD_TYPES
	POINTINFO_HITNUMBER           =1119       # from enum ENUM_FIELD_TYPES
	POINT_INFO_HEADING            =186        # from enum ENUM_FIELD_TYPES
	POLAR_VECTOR_COMPENSATION     =218        # from enum ENUM_FIELD_TYPES
	POSITIONAL_ACCURACY           =214        # from enum ENUM_FIELD_TYPES
	POSITION_SEGMENT              =993        # from enum ENUM_FIELD_TYPES
	POS_REPORT_AXIS_X             =277        # from enum ENUM_FIELD_TYPES
	POS_REPORT_AXIS_Y             =278        # from enum ENUM_FIELD_TYPES
	POS_REPORT_AXIS_Z             =279        # from enum ENUM_FIELD_TYPES
	POS_REPT_DISPLAY_OPTION       =462        # from enum ENUM_FIELD_TYPES
	PPROG                         =399        # from enum ENUM_FIELD_TYPES
	PRECISION                     =175        # from enum ENUM_FIELD_TYPES
	PREHIT_RETRACT                =1014       # from enum ENUM_FIELD_TYPES
	PRE_PROBE_CYLINDER            =1016       # from enum ENUM_FIELD_TYPES
	PRIMARY_DROP                  =1088       # from enum ENUM_FIELD_TYPES
	PRINT_DELETE_RUNS             =377        # from enum ENUM_FIELD_TYPES
	PRINT_DRAFTMODE               =376        # from enum ENUM_FIELD_TYPES
	PRINT_TO_FILE                 =374        # from enum ENUM_FIELD_TYPES
	PRINT_TO_PRINTER              =375        # from enum ENUM_FIELD_TYPES
	PROBE_ACCURACY                =213        # from enum ENUM_FIELD_TYPES
	PROBE_COMP                    =228        # from enum ENUM_FIELD_TYPES
	PROBE_DIRECTION               =793        # from enum ENUM_FIELD_TYPES
	PROBE_TYPE                    =834        # from enum ENUM_FIELD_TYPES
	PROBING_MODE                  =299        # from enum ENUM_FIELD_TYPES
	PROBING_PERIOD                =1015       # from enum ENUM_FIELD_TYPES
	PROFILE_BOTTOM_CURVE          =1087       # from enum ENUM_FIELD_TYPES
	PROFILE_FORM_TYPE             =174        # from enum ENUM_FIELD_TYPES
	PROFILE_TOP_CURVE             =1086       # from enum ENUM_FIELD_TYPES
	PROFILE_TYPE                  =550        # from enum ENUM_FIELD_TYPES
	PROGRAM_GAGE_FEAT_TYPE        =521        # from enum ENUM_FIELD_TYPES
	PROGRAM_GAGE_TYPE             =522        # from enum ENUM_FIELD_TYPES
	PROJECTOR                     =847        # from enum ENUM_FIELD_TYPES
	PROJECT_POINT                 =948        # from enum ENUM_FIELD_TYPES
	PTDENSITY_DEVLIMIT            =843        # from enum ENUM_FIELD_TYPES
	PTDENSITY_MAXSPAN             =844        # from enum ENUM_FIELD_TYPES
	PTDENSITY_TOGGLE              =841        # from enum ENUM_FIELD_TYPES
	PTDENSITY_UPPERBOUND          =842        # from enum ENUM_FIELD_TYPES
	PUNCHVEC_I                    =118        # from enum ENUM_FIELD_TYPES
	PUNCHVEC_J                    =119        # from enum ENUM_FIELD_TYPES
	PUNCHVEC_K                    =120        # from enum ENUM_FIELD_TYPES
	QDAS_CATALOG_FILENAME         =1075       # from enum ENUM_FIELD_TYPES
	QDAS_CONFIGURATION_FILENAME   =1074       # from enum ENUM_FIELD_TYPES
	QDAS_OUTPUT_FILE_TYPE         =1073       # from enum ENUM_FIELD_TYPES
	QUALITY_THRESHOLD             =1156       # from enum ENUM_FIELD_TYPES
	QUERY_SHOW_GRAPHIC_SETTINGS   =470        # from enum ENUM_FIELD_TYPES
	RADIUS_TYPE                   =171        # from enum ENUM_FIELD_TYPES
	RANGE                         =1048       # from enum ENUM_FIELD_TYPES
	READPOS_TYPE                  =46         # from enum ENUM_FIELD_TYPES
	READ_FILE_PRIOR_EXEC          =1108       # from enum ENUM_FIELD_TYPES
	READ_WRITE                    =196        # from enum ENUM_FIELD_TYPES
	REDUCTION_FILTER              =864        # from enum ENUM_FIELD_TYPES
	REDUCTION_FILTER_PERCENTAGE   =913        # from enum ENUM_FIELD_TYPES
	REFRACTIVE_INDEX              =1081       # from enum ENUM_FIELD_TYPES
	REF_ID                        =3          # from enum ENUM_FIELD_TYPES
	REF_TEMP                      =222        # from enum ENUM_FIELD_TYPES
	REF_UID                       =798        # from enum ENUM_FIELD_TYPES
	REGR                          =412        # from enum ENUM_FIELD_TYPES
	RELATIVE_COMMENTS             =830        # from enum ENUM_FIELD_TYPES
	REPIERCE_CAD                  =142        # from enum ENUM_FIELD_TYPES
	REPORTVEC_I                   =121        # from enum ENUM_FIELD_TYPES
	REPORTVEC_J                   =122        # from enum ENUM_FIELD_TYPES
	REPORTVEC_K                   =123        # from enum ENUM_FIELD_TYPES
	REPORT_GRAPH_ANALYSIS         =1064       # from enum ENUM_FIELD_TYPES
	REPORT_LABEL_AXIS             =1131       # from enum ENUM_FIELD_TYPES
	REPORT_LABEL_BONUS            =1137       # from enum ENUM_FIELD_TYPES
	REPORT_LABEL_DEV              =1136       # from enum ENUM_FIELD_TYPES
	REPORT_LABEL_ISPLANAR         =1139       # from enum ENUM_FIELD_TYPES
	REPORT_LABEL_MEAS             =1133       # from enum ENUM_FIELD_TYPES
	REPORT_LABEL_MINUSTOL         =1135       # from enum ENUM_FIELD_TYPES
	REPORT_LABEL_NOMINAL          =1132       # from enum ENUM_FIELD_TYPES
	REPORT_LABEL_OUTTOL           =1138       # from enum ENUM_FIELD_TYPES
	REPORT_LABEL_PLANAR_OPEN_IN_X =1144       # from enum ENUM_FIELD_TYPES
	REPORT_LABEL_PLANAR_XDEV      =1142       # from enum ENUM_FIELD_TYPES
	REPORT_LABEL_PLANAR_XTOL      =1140       # from enum ENUM_FIELD_TYPES
	REPORT_LABEL_PLANAR_YDEV      =1143       # from enum ENUM_FIELD_TYPES
	REPORT_LABEL_PLANAR_YTOL      =1141       # from enum ENUM_FIELD_TYPES
	REPORT_LABEL_PLUSTOL          =1134       # from enum ENUM_FIELD_TYPES
	REPORT_MODE                   =323        # from enum ENUM_FIELD_TYPES
	REPORT_SURFVEC_I              =383        # from enum ENUM_FIELD_TYPES
	REPORT_SURFVEC_J              =384        # from enum ENUM_FIELD_TYPES
	REPORT_SURFVEC_K              =385        # from enum ENUM_FIELD_TYPES
	RETURN_SPEED                  =216        # from enum ENUM_FIELD_TYPES
	RET_ONLY_TYPE                 =188        # from enum ENUM_FIELD_TYPES
	REVISION_NUMBER               =192        # from enum ENUM_FIELD_TYPES
	RMEASFEATID                   =69         # from enum ENUM_FIELD_TYPES
	RMEASFEATIDX                  =524        # from enum ENUM_FIELD_TYPES
	RMEASFEATIDY                  =525        # from enum ENUM_FIELD_TYPES
	RMEASFEATIDZ                  =526        # from enum ENUM_FIELD_TYPES
	RMEAS_TYPE                    =48         # from enum ENUM_FIELD_TYPES
	ROTAB_MOVE_SIMULTANEOUS       =1123       # from enum ENUM_FIELD_TYPES
	ROTATE_REF_ID                 =5          # from enum ENUM_FIELD_TYPES
	ROTATION_TYPE                 =158        # from enum ENUM_FIELD_TYPES
	ROTATION_TYPE_2               =833        # from enum ENUM_FIELD_TYPES
	ROW_ID                        =286        # from enum ENUM_FIELD_TYPES
	RPT_DIMENSION_TABLES          =639        # from enum ENUM_FIELD_TYPES
	SAMPLE_FEATURE                =950        # from enum ENUM_FIELD_TYPES
	SAMPLE_HIT_MEAS_A             =965        # from enum ENUM_FIELD_TYPES
	SAMPLE_HIT_MEAS_H             =966        # from enum ENUM_FIELD_TYPES
	SAMPLE_HIT_MEAS_R             =964        # from enum ENUM_FIELD_TYPES
	SAMPLE_HIT_MEAS_X             =961        # from enum ENUM_FIELD_TYPES
	SAMPLE_HIT_MEAS_Y             =962        # from enum ENUM_FIELD_TYPES
	SAMPLE_HIT_MEAS_Z             =963        # from enum ENUM_FIELD_TYPES
	SAMPLE_HIT_THEO_A             =956        # from enum ENUM_FIELD_TYPES
	SAMPLE_HIT_THEO_H             =957        # from enum ENUM_FIELD_TYPES
	SAMPLE_HIT_THEO_I             =958        # from enum ENUM_FIELD_TYPES
	SAMPLE_HIT_THEO_J             =959        # from enum ENUM_FIELD_TYPES
	SAMPLE_HIT_THEO_K             =960        # from enum ENUM_FIELD_TYPES
	SAMPLE_HIT_THEO_R             =955        # from enum ENUM_FIELD_TYPES
	SAMPLE_HIT_THEO_X             =952        # from enum ENUM_FIELD_TYPES
	SAMPLE_HIT_THEO_Y             =953        # from enum ENUM_FIELD_TYPES
	SAMPLE_HIT_THEO_Z             =954        # from enum ENUM_FIELD_TYPES
	SAMPLE_HIT_TYPE               =969        # from enum ENUM_FIELD_TYPES
	SAMPLE_METHOD                 =951        # from enum ENUM_FIELD_TYPES
	SAVE_ALIGN_CAD_TO_PARTS       =151        # from enum ENUM_FIELD_TYPES
	SCALING                       =795        # from enum ENUM_FIELD_TYPES
	SCAN_4AXIS                    =1060       # from enum ENUM_FIELD_TYPES
	SCAN_ACCELERATION             =92         # from enum ENUM_FIELD_TYPES
	SCAN_AXISVEC_I                =265        # from enum ENUM_FIELD_TYPES
	SCAN_AXISVEC_J                =266        # from enum ENUM_FIELD_TYPES
	SCAN_AXISVEC_K                =267        # from enum ENUM_FIELD_TYPES
	SCAN_BNDRY_TYPE               =432        # from enum ENUM_FIELD_TYPES
	SCAN_COMPENSATION             =1008       # from enum ENUM_FIELD_TYPES
	SCAN_CROSS_TOTAL              =274        # from enum ENUM_FIELD_TYPES
	SCAN_CURVE_TYPE               =1105       # from enum ENUM_FIELD_TYPES
	SCAN_CUTPLANEVEC_I            =259        # from enum ENUM_FIELD_TYPES
	SCAN_CUTPLANEVEC_J            =260        # from enum ENUM_FIELD_TYPES
	SCAN_CUTPLANEVEC_K            =261        # from enum ENUM_FIELD_TYPES
	SCAN_DENSITY                  =217        # from enum ENUM_FIELD_TYPES
	SCAN_EDGE_THICK               =276        # from enum ENUM_FIELD_TYPES
	SCAN_ENDVEC_I                 =268        # from enum ENUM_FIELD_TYPES
	SCAN_ENDVEC_J                 =269        # from enum ENUM_FIELD_TYPES
	SCAN_ENDVEC_K                 =270        # from enum ENUM_FIELD_TYPES
	SCAN_EXECUTION_MODE           =1079       # from enum ENUM_FIELD_TYPES
	SCAN_INITDIR_I                =271        # from enum ENUM_FIELD_TYPES
	SCAN_INITDIR_J                =272        # from enum ENUM_FIELD_TYPES
	SCAN_INITDIR_K                =273        # from enum ENUM_FIELD_TYPES
	SCAN_INITVEC_I                =262        # from enum ENUM_FIELD_TYPES
	SCAN_INITVEC_J                =263        # from enum ENUM_FIELD_TYPES
	SCAN_INITVEC_K                =264        # from enum ENUM_FIELD_TYPES
	SCAN_MODE                     =855        # from enum ENUM_FIELD_TYPES
	SCAN_OFFSET_FORCE             =93         # from enum ENUM_FIELD_TYPES
	SCAN_PATH_DENSITY             =1099       # from enum ENUM_FIELD_TYPES
	SCAN_SHAPE_TEACH_TYPE         =1107       # from enum ENUM_FIELD_TYPES
	SCAN_TECHNIQUE                =358        # from enum ENUM_FIELD_TYPES
	SCAN_TIME_INCR                =275        # from enum ENUM_FIELD_TYPES
	SCAN_TYPE                     =1005       # from enum ENUM_FIELD_TYPES
	SCONDARY_DROP                 =1089       # from enum ENUM_FIELD_TYPES
	SCREEN_CAPTURE_AUTO_TIME      =540        # from enum ENUM_FIELD_TYPES
	SCREEN_CAPTURE_AUTO_TYPE      =536        # from enum ENUM_FIELD_TYPES
	SCREEN_CAPTURE_QUALITY        =503        # from enum ENUM_FIELD_TYPES
	SCREEN_CAPTURE_SCALE          =502        # from enum ENUM_FIELD_TYPES
	SCREEN_CAPTURE_TYPE           =535        # from enum ENUM_FIELD_TYPES
	SEARCHMODE_TYPE               =57         # from enum ENUM_FIELD_TYPES
	SECTION_INDEX                 =764        # from enum ENUM_FIELD_TYPES
	SEGMENT_TOGGLE                =1065       # from enum ENUM_FIELD_TYPES
	SEGMENT_TYPE                  =1066       # from enum ENUM_FIELD_TYPES
	SEGMENT_TYPE_TOGGLE           =1067       # from enum ENUM_FIELD_TYPES
	SELECT_BY_TOTAL_HITS          =1026       # from enum ENUM_FIELD_TYPES
	SELECT_CENTER                 =1100       # from enum ENUM_FIELD_TYPES
	SELECT_EVERY_NPOINTS          =1027       # from enum ENUM_FIELD_TYPES
	SELECT_FIRST_POINT            =1024       # from enum ENUM_FIELD_TYPES
	SELECT_LAST_POINT             =1025       # from enum ENUM_FIELD_TYPES
	SELECT_TOTAL_NHITS            =1028       # from enum ENUM_FIELD_TYPES
	SELF_CENTER_CUT_VECTOR_I      =1055       # from enum ENUM_FIELD_TYPES
	SELF_CENTER_CUT_VECTOR_J      =1056       # from enum ENUM_FIELD_TYPES
	SELF_CENTER_CUT_VECTOR_K      =1057       # from enum ENUM_FIELD_TYPES
	SELF_CENTER_POINT             =1054       # from enum ENUM_FIELD_TYPES
	SENSITIVITY_MODE              =865        # from enum ENUM_FIELD_TYPES
	SENSOR_LIST                   =225        # from enum ENUM_FIELD_TYPES
	SERIAL_NUMBER                 =193        # from enum ENUM_FIELD_TYPES
	SHIFT_BONUS                   =915        # from enum ENUM_FIELD_TYPES
	SHIFT_BONUS2                  =916        # from enum ENUM_FIELD_TYPES
	SHOW_COLUMN                   =494        # from enum ENUM_FIELD_TYPES
	SHOW_DETAILS                  =136        # from enum ENUM_FIELD_TYPES
	SHOW_HEADINGS                 =179        # from enum ENUM_FIELD_TYPES
	SHOW_IDS                      =135        # from enum ENUM_FIELD_TYPES
	SHOW_MORE_SPC_CALCS           =414        # from enum ENUM_FIELD_TYPES
	SHOW_NOMS                     =723        # from enum ENUM_FIELD_TYPES
	SHOW_OPTIONS                  =728        # from enum ENUM_FIELD_TYPES
	SHOW_POINT_INFO               =187        # from enum ENUM_FIELD_TYPES
	SHOW_ROW                      =493        # from enum ENUM_FIELD_TYPES
	SHOW_SPC_CALCS                =402        # from enum ENUM_FIELD_TYPES
	SIMULT_EVAL                   =763        # from enum ENUM_FIELD_TYPES
	SIMUL_NUMBER_POSITION_FCFS    =912        # from enum ENUM_FIELD_TYPES
	SIMUL_NUMBER_PROFILE_FCFS     =911        # from enum ENUM_FIELD_TYPES
	SINGLE_POINT                  =235        # from enum ENUM_FIELD_TYPES
	SINGLE_POINT_DEVIATION        =849        # from enum ENUM_FIELD_TYPES
	SIZE_NOMINAL                  =1068       # from enum ENUM_FIELD_TYPES
	SIZE_SYMBOL                   =866        # from enum ENUM_FIELD_TYPES
	SIZE_TOLERANCE                =1002       # from enum ENUM_FIELD_TYPES
	SKIP_NUM                      =145        # from enum ENUM_FIELD_TYPES
	SKIP_RINGS                    =1104       # from enum ENUM_FIELD_TYPES
	SLOTVEC_I                     =109        # from enum ENUM_FIELD_TYPES
	SLOTVEC_J                     =110        # from enum ENUM_FIELD_TYPES
	SLOTVEC_K                     =111        # from enum ENUM_FIELD_TYPES
	SLOT_MIN_MAX_TYPE             =53         # from enum ENUM_FIELD_TYPES
	SLOT_NUMBER                   =297        # from enum ENUM_FIELD_TYPES
	SLOT_TYPE                     =563        # from enum ENUM_FIELD_TYPES
	SMOOTHING_CORNER_RADIUS       =1106       # from enum ENUM_FIELD_TYPES
	SMOOTHING_TOLERANCE           =1021       # from enum ENUM_FIELD_TYPES
	SNAP_TYPE                     =43         # from enum ENUM_FIELD_TYPES
	SOLID                         =416        # from enum ENUM_FIELD_TYPES
	SPECIFICATION_STRING          =1041       # from enum ENUM_FIELD_TYPES
	SPEC_LIMITS                   =403        # from enum ENUM_FIELD_TYPES
	SPEC_OFFSET                   =415        # from enum ENUM_FIELD_TYPES
	SPHERE_CENTER_X               =1109       # from enum ENUM_FIELD_TYPES
	SPHERE_CENTER_Y               =1110       # from enum ENUM_FIELD_TYPES
	SPHERE_CENTER_Z               =1111       # from enum ENUM_FIELD_TYPES
	SRC_EXPR                      =134        # from enum ENUM_FIELD_TYPES
	STANDARD                      =1042       # from enum ENUM_FIELD_TYPES
	STANDARD_DEVIATION            =181        # from enum ENUM_FIELD_TYPES
	START_ANG                     =98         # from enum ENUM_FIELD_TYPES
	START_LABEL                   =466        # from enum ENUM_FIELD_TYPES
	START_NUM                     =143        # from enum ENUM_FIELD_TYPES
	STATS_DATASOURCE              =391        # from enum ENUM_FIELD_TYPES
	STATS_DB_TYPE                 =453        # from enum ENUM_FIELD_TYPES
	STATS_DIR                     =248        # from enum ENUM_FIELD_TYPES
	STATS_TYPE                    =247        # from enum ENUM_FIELD_TYPES
	STAT_CALC_TYPE                =254        # from enum ENUM_FIELD_TYPES
	STAT_COUNT                    =194        # from enum ENUM_FIELD_TYPES
	STAT_NAME_TYPE                =253        # from enum ENUM_FIELD_TYPES
	STDDEV                        =405        # from enum ENUM_FIELD_TYPES
	STRIPE_DISTANCE               =1076       # from enum ENUM_FIELD_TYPES
	SUB_NAME                      =195        # from enum ENUM_FIELD_TYPES
	SUMMARY_AXIS                  =690        # from enum ENUM_FIELD_TYPES
	SUMMARY_BONUS                 =781        # from enum ENUM_FIELD_TYPES
	SUMMARY_COLUMN_HDR            =684        # from enum ENUM_FIELD_TYPES
	SUMMARY_DEV                   =640        # from enum ENUM_FIELD_TYPES
	SUMMARY_FEAT                  =685        # from enum ENUM_FIELD_TYPES
	SUMMARY_MAX                   =779        # from enum ENUM_FIELD_TYPES
	SUMMARY_MEAS                  =692        # from enum ENUM_FIELD_TYPES
	SUMMARY_MIN                   =780        # from enum ENUM_FIELD_TYPES
	SUMMARY_MINUSTOL              =778        # from enum ENUM_FIELD_TYPES
	SUMMARY_NOMINAL               =691        # from enum ENUM_FIELD_TYPES
	SUMMARY_OUTTOL                =776        # from enum ENUM_FIELD_TYPES
	SUMMARY_PLUSTOL               =777        # from enum ENUM_FIELD_TYPES
	SUMMARY_TBLHDR                =689        # from enum ENUM_FIELD_TYPES
	SURFACE                       =484        # from enum ENUM_FIELD_TYPES
	SURFACE_INTERPERTATION_IF_POSSIBLE=995        # from enum ENUM_FIELD_TYPES
	SURFACE_TYPE                  =998        # from enum ENUM_FIELD_TYPES
	SURFVEC_I                     =112        # from enum ENUM_FIELD_TYPES
	SURFVEC_J                     =113        # from enum ENUM_FIELD_TYPES
	SURFVEC_K                     =114        # from enum ENUM_FIELD_TYPES
	SURFVEC_MEAS_I                =546        # from enum ENUM_FIELD_TYPES
	SURFVEC_MEAS_J                =547        # from enum ENUM_FIELD_TYPES
	SURFVEC_MEAS_K                =548        # from enum ENUM_FIELD_TYPES
	SURFVEC_TARG_I                =329        # from enum ENUM_FIELD_TYPES
	SURFVEC_TARG_J                =330        # from enum ENUM_FIELD_TYPES
	SURFVEC_TARG_K                =331        # from enum ENUM_FIELD_TYPES
	TARGET_BLOB_TYPE              =557        # from enum ENUM_FIELD_TYPES
	TARGET_COLOR                  =282        # from enum ENUM_FIELD_TYPES
	TARGET_COVERAGE               =832        # from enum ENUM_FIELD_TYPES
	TARGET_COVERAGE_ACTIVE_TARGETS=923        # from enum ENUM_FIELD_TYPES
	TARGET_DIRECTION              =474        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_ANGLE             =520        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_CROSSHAIR_CENTER  =853        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_DARKLIGHT         =975        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_DENSITY           =508        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_EDGEDETECT        =712        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_EDGENUM           =538        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_EDGESELECT        =537        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_END_VALUE         =828        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_FILTER_AREA       =715        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_FILTER_AREA_SIZE  =716        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_FILTER_CLEAN      =713        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_FILTER_CLEAN_STRENGTH=714        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_GRADIENT          =717        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_GREYSCALE_THRESHHOLD=974        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_HEIGHT            =711        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_ILLUM             =505        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_IMAGE_RGB_MIXING_B=870        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_IMAGE_RGB_MIXING_G=869        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_IMAGE_RGB_MIXING_R=868        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_MIN_AREA          =973        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_MIN_MAX_TYPE      =884        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_MIN_MAX_TYPE_TOGGLE=885        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_MIN_MAX_WIDTH     =883        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_POLARITY          =475        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_SENSILIGHT        =592        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_SIZE              =504        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_START_VALUE       =827        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_STRENGTH          =507        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_TOL               =506        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_TYPE              =509        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_UNDERSCAN         =549        # from enum ENUM_FIELD_TYPES
	TARGET_EDGE_WIDTH             =710        # from enum ENUM_FIELD_TYPES
	TARGET_FILTER_AREA            =715        # from enum ENUM_FIELD_TYPES
	TARGET_FILTER_AREA_SIZE       =716        # from enum ENUM_FIELD_TYPES
	TARGET_FILTER_CLEAN           =713        # from enum ENUM_FIELD_TYPES
	TARGET_FILTER_CLEAN_STRENGTH  =714        # from enum ENUM_FIELD_TYPES
	TARGET_FILTER_OUTLIER         =561        # from enum ENUM_FIELD_TYPES
	TARGET_FILTER_OUTLIER_DISTANCE_MULTIPLIER=986        # from enum ENUM_FIELD_TYPES
	TARGET_FILTER_OUTLIER_DISTANCE_THRESHOLD=562        # from enum ENUM_FIELD_TYPES
	TARGET_FILTER_OUTLIER_MIN_NEIGHBORS=985        # from enum ENUM_FIELD_TYPES
	TARGET_FILTER_OUTLIER_STD_DEV_THRESHOLD=599        # from enum ENUM_FIELD_TYPES
	TARGET_FILTER_OUTLIER_USING_NEIGHBORS=984        # from enum ENUM_FIELD_TYPES
	TARGET_FOCUS                  =523        # from enum ENUM_FIELD_TYPES
	TARGET_MEASURE_AT_FOV_CENTER  =845        # from enum ENUM_FIELD_TYPES
	TARGET_SURFACE_CROSSHAIR_HEIGHT=722        # from enum ENUM_FIELD_TYPES
	TARGET_SURFACE_DURATION       =499        # from enum ENUM_FIELD_TYPES
	TARGET_SURFACE_FIND_SURFACE   =846        # from enum ENUM_FIELD_TYPES
	TARGET_SURFACE_HEIGHT         =497        # from enum ENUM_FIELD_TYPES
	TARGET_SURFACE_HIACC          =501        # from enum ENUM_FIELD_TYPES
	TARGET_SURFACE_ILLUM          =490        # from enum ENUM_FIELD_TYPES
	TARGET_SURFACE_IMAGE_RGB_MIXING_B=870        # from enum ENUM_FIELD_TYPES
	TARGET_SURFACE_IMAGE_RGB_MIXING_G=869        # from enum ENUM_FIELD_TYPES
	TARGET_SURFACE_IMAGE_RGB_MIXING_R=868        # from enum ENUM_FIELD_TYPES
	TARGET_SURFACE_MODE           =500        # from enum ENUM_FIELD_TYPES
	TARGET_SURFACE_RANGE          =498        # from enum ENUM_FIELD_TYPES
	TARGET_SURFACE_SENSILIGHT     =495        # from enum ENUM_FIELD_TYPES
	TARGET_SURFACE_SURFACE_VARIANCE=829        # from enum ENUM_FIELD_TYPES
	TARGET_SURFACE_TYPE           =511        # from enum ENUM_FIELD_TYPES
	TARGET_SURFACE_WIDTH          =496        # from enum ENUM_FIELD_TYPES
	TARGET_TYPE                   =564        # from enum ENUM_FIELD_TYPES
	TARGSLOT_I                    =124        # from enum ENUM_FIELD_TYPES
	TARGSLOT_J                    =125        # from enum ENUM_FIELD_TYPES
	TARGSLOT_K                    =126        # from enum ENUM_FIELD_TYPES
	TARG_A                        =572        # from enum ENUM_FIELD_TYPES
	TARG_EA                       =590        # from enum ENUM_FIELD_TYPES
	TARG_EH                       =591        # from enum ENUM_FIELD_TYPES
	TARG_EI                       =942        # from enum ENUM_FIELD_TYPES
	TARG_EJ                       =943        # from enum ENUM_FIELD_TYPES
	TARG_EK                       =944        # from enum ENUM_FIELD_TYPES
	TARG_ER                       =589        # from enum ENUM_FIELD_TYPES
	TARG_EX                       =516        # from enum ENUM_FIELD_TYPES
	TARG_EY                       =517        # from enum ENUM_FIELD_TYPES
	TARG_EZ                       =518        # from enum ENUM_FIELD_TYPES
	TARG_H                        =573        # from enum ENUM_FIELD_TYPES
	TARG_I                        =31         # from enum ENUM_FIELD_TYPES
	TARG_J                        =32         # from enum ENUM_FIELD_TYPES
	TARG_K                        =33         # from enum ENUM_FIELD_TYPES
	TARG_R                        =571        # from enum ENUM_FIELD_TYPES
	TARG_SA                       =587        # from enum ENUM_FIELD_TYPES
	TARG_SH                       =588        # from enum ENUM_FIELD_TYPES
	TARG_SI                       =939        # from enum ENUM_FIELD_TYPES
	TARG_SJ                       =940        # from enum ENUM_FIELD_TYPES
	TARG_SK                       =941        # from enum ENUM_FIELD_TYPES
	TARG_SR                       =586        # from enum ENUM_FIELD_TYPES
	TARG_SX                       =513        # from enum ENUM_FIELD_TYPES
	TARG_SY                       =514        # from enum ENUM_FIELD_TYPES
	TARG_SZ                       =515        # from enum ENUM_FIELD_TYPES
	TARG_X                        =19         # from enum ENUM_FIELD_TYPES
	TARG_Y                        =20         # from enum ENUM_FIELD_TYPES
	TARG_Z                        =21         # from enum ENUM_FIELD_TYPES
	TEMPLATE_MATCH                =1091       # from enum ENUM_FIELD_TYPES
	TEMPLATE_MATCH_CORRELATION    =1092       # from enum ENUM_FIELD_TYPES
	TEMPP                         =532        # from enum ENUM_FIELD_TYPES
	TEMPX                         =529        # from enum ENUM_FIELD_TYPES
	TEMPY                         =530        # from enum ENUM_FIELD_TYPES
	TEMPZ                         =531        # from enum ENUM_FIELD_TYPES
	TEXTANAL_LABEL_DEV            =761        # from enum ENUM_FIELD_TYPES
	TEXTANAL_LABEL_MEAS_I         =758        # from enum ENUM_FIELD_TYPES
	TEXTANAL_LABEL_MEAS_J         =759        # from enum ENUM_FIELD_TYPES
	TEXTANAL_LABEL_MEAS_K         =760        # from enum ENUM_FIELD_TYPES
	TEXTANAL_LABEL_MEAS_X         =755        # from enum ENUM_FIELD_TYPES
	TEXTANAL_LABEL_MEAS_Y         =756        # from enum ENUM_FIELD_TYPES
	TEXTANAL_LABEL_MEAS_Z         =757        # from enum ENUM_FIELD_TYPES
	TEXTANAL_LABEL_MINMAX         =762        # from enum ENUM_FIELD_TYPES
	TEXT_ANALYSIS                 =163        # from enum ENUM_FIELD_TYPES
	THEOBF_TYPE                   =49         # from enum ENUM_FIELD_TYPES
	THEO_A                        =566        # from enum ENUM_FIELD_TYPES
	THEO_A2                       =609        # from enum ENUM_FIELD_TYPES
	THEO_ANGLE                    =38         # from enum ENUM_FIELD_TYPES
	THEO_AREA                     =720        # from enum ENUM_FIELD_TYPES
	THEO_DEPTH                    =555        # from enum ENUM_FIELD_TYPES
	THEO_DIAM                     =34         # from enum ENUM_FIELD_TYPES
	THEO_DX                       =1083       # from enum ENUM_FIELD_TYPES
	THEO_DY                       =1084       # from enum ENUM_FIELD_TYPES
	THEO_DZ                       =1085       # from enum ENUM_FIELD_TYPES
	THEO_EA                       =578        # from enum ENUM_FIELD_TYPES
	THEO_EH                       =579        # from enum ENUM_FIELD_TYPES
	THEO_EI                       =930        # from enum ENUM_FIELD_TYPES
	THEO_EJ                       =931        # from enum ENUM_FIELD_TYPES
	THEO_EK                       =932        # from enum ENUM_FIELD_TYPES
	THEO_END_ANG                  =284        # from enum ENUM_FIELD_TYPES
	THEO_ER                       =577        # from enum ENUM_FIELD_TYPES
	THEO_EX                       =13         # from enum ENUM_FIELD_TYPES
	THEO_EY                       =14         # from enum ENUM_FIELD_TYPES
	THEO_EZ                       =15         # from enum ENUM_FIELD_TYPES
	THEO_FLUSH                    =551        # from enum ENUM_FIELD_TYPES
	THEO_GAP                      =553        # from enum ENUM_FIELD_TYPES
	THEO_H                        =567        # from enum ENUM_FIELD_TYPES
	THEO_H2                       =610        # from enum ENUM_FIELD_TYPES
	THEO_HEIGHT                   =37         # from enum ENUM_FIELD_TYPES
	THEO_I                        =16         # from enum ENUM_FIELD_TYPES
	THEO_J                        =17         # from enum ENUM_FIELD_TYPES
	THEO_K                        =18         # from enum ENUM_FIELD_TYPES
	THEO_LENGTH                   =36         # from enum ENUM_FIELD_TYPES
	THEO_MINOR_AXIS               =130        # from enum ENUM_FIELD_TYPES
	THEO_MINOR_DIAMETER           =920        # from enum ENUM_FIELD_TYPES
	THEO_PERIMETER                =718        # from enum ENUM_FIELD_TYPES
	THEO_R                        =565        # from enum ENUM_FIELD_TYPES
	THEO_R2                       =608        # from enum ENUM_FIELD_TYPES
	THEO_RADIUS                   =977        # from enum ENUM_FIELD_TYPES
	THEO_SA                       =575        # from enum ENUM_FIELD_TYPES
	THEO_SH                       =576        # from enum ENUM_FIELD_TYPES
	THEO_SI                       =927        # from enum ENUM_FIELD_TYPES
	THEO_SJ                       =928        # from enum ENUM_FIELD_TYPES
	THEO_SK                       =929        # from enum ENUM_FIELD_TYPES
	THEO_SR                       =574        # from enum ENUM_FIELD_TYPES
	THEO_START_ANG                =283        # from enum ENUM_FIELD_TYPES
	THEO_SX                       =10         # from enum ENUM_FIELD_TYPES
	THEO_SY                       =11         # from enum ENUM_FIELD_TYPES
	THEO_SZ                       =12         # from enum ENUM_FIELD_TYPES
	THEO_WIDTH                    =35         # from enum ENUM_FIELD_TYPES
	THEO_X                        =7          # from enum ENUM_FIELD_TYPES
	THEO_X2                       =393        # from enum ENUM_FIELD_TYPES
	THEO_Y                        =8          # from enum ENUM_FIELD_TYPES
	THEO_Y2                       =394        # from enum ENUM_FIELD_TYPES
	THEO_Z                        =9          # from enum ENUM_FIELD_TYPES
	THEO_Z2                       =395        # from enum ENUM_FIELD_TYPES
	THICKNESS_DROP                =1090       # from enum ENUM_FIELD_TYPES
	THICKNESS_GAGE_DISTANCE       =1096       # from enum ENUM_FIELD_TYPES
	THICKNESS_GAGE_PRIMARY_FEATURE=1094       # from enum ENUM_FIELD_TYPES
	THICKNESS_GAGE_SECONDARY_FEATURE=1095       # from enum ENUM_FIELD_TYPES
	THICKNESS_GAGE_SHOW_POI       =1097       # from enum ENUM_FIELD_TYPES
	THICKNESS_TYPE                =41         # from enum ENUM_FIELD_TYPES
	THICKNESS_TYPE_EDGE           =594        # from enum ENUM_FIELD_TYPES
	THINNING_TOL                  =67         # from enum ENUM_FIELD_TYPES
	THREADED_HOLE                 =1017       # from enum ENUM_FIELD_TYPES
	THRESHOLD                     =488        # from enum ENUM_FIELD_TYPES
	TIME_ARG                      =450        # from enum ENUM_FIELD_TYPES
	TIME_FILTER                   =401        # from enum ENUM_FIELD_TYPES
	TIME_STAMP                    =835        # from enum ENUM_FIELD_TYPES
	TIP_I                         =229        # from enum ENUM_FIELD_TYPES
	TIP_J                         =230        # from enum ENUM_FIELD_TYPES
	TIP_K                         =231        # from enum ENUM_FIELD_TYPES
	TITLE                         =418        # from enum ENUM_FIELD_TYPES
	TOLERANCE_CODE                =1047       # from enum ENUM_FIELD_TYPES
	TOLERANCE_ZONE_DIRECTION      =994        # from enum ENUM_FIELD_TYPES
	TOOL_DIAM                     =349        # from enum ENUM_FIELD_TYPES
	TOOL_X                        =346        # from enum ENUM_FIELD_TYPES
	TOOL_Y                        =347        # from enum ENUM_FIELD_TYPES
	TOOL_Z                        =348        # from enum ENUM_FIELD_TYPES
	TPS_SUB_COMMAND_TYPE          =887        # from enum ENUM_FIELD_TYPES
	TP_MODIFIER                   =169        # from enum ENUM_FIELD_TYPES
	TP_MODIFIER2                  =726        # from enum ENUM_FIELD_TYPES
	TRACE_DATA_SOURCE             =1077       # from enum ENUM_FIELD_TYPES
	TRACE_DISPLAY_MESSAGE         =1072       # from enum ENUM_FIELD_TYPES
	TRACE_DISPLAY_ONREPORT        =1093       # from enum ENUM_FIELD_TYPES
	TRACE_FILTER                  =400        # from enum ENUM_FIELD_TYPES
	TRACE_FILTER_ARG              =451        # from enum ENUM_FIELD_TYPES
	TRACE_NAME                    =257        # from enum ENUM_FIELD_TYPES
	TRACE_VALUE                   =258        # from enum ENUM_FIELD_TYPES
	TRACE_VALUE_LIMIT             =473        # from enum ENUM_FIELD_TYPES
	TRACE_VALUE_OPTION            =1078       # from enum ENUM_FIELD_TYPES
	TRACKER_GRAVITY_PLANE         =882        # from enum ENUM_FIELD_TYPES
	TRACKER_SUB_COMMAND_TYPE      =881        # from enum ENUM_FIELD_TYPES
	TRANSFER_DIR                  =255        # from enum ENUM_FIELD_TYPES
	TRANSLATION_MODIFIER          =1125       # from enum ENUM_FIELD_TYPES
	TRIGGERPLANE                  =469        # from enum ENUM_FIELD_TYPES
	TRIGGERTOLERANCE              =463        # from enum ENUM_FIELD_TYPES
	TRIGGERTOLVALUE               =464        # from enum ENUM_FIELD_TYPES
	TRIGGER_FORCE                 =212        # from enum ENUM_FIELD_TYPES
	TWO_D_THREE_D_TYPE            =131        # from enum ENUM_FIELD_TYPES
	T_VALUE                       =345        # from enum ENUM_FIELD_TYPES
	UCL_LCL                       =406        # from enum ENUM_FIELD_TYPES
	UID                           =797        # from enum ENUM_FIELD_TYPES
	UNEQUAL_TOL_LINE2             =890        # from enum ENUM_FIELD_TYPES
	UNEQUAL_TOL_LINE3             =891        # from enum ENUM_FIELD_TYPES
	UNEQUAL_TOL_ZONE_LINE2        =888        # from enum ENUM_FIELD_TYPES
	UNEQUAL_TOL_ZONE_LINE3        =889        # from enum ENUM_FIELD_TYPES
	UNIT_AREA_LINE3               =898        # from enum ENUM_FIELD_TYPES
	UNIT_TYPE                     =172        # from enum ENUM_FIELD_TYPES
	UPDATEVEC_I                   =127        # from enum ENUM_FIELD_TYPES
	UPDATEVEC_J                   =128        # from enum ENUM_FIELD_TYPES
	UPDATEVEC_K                   =129        # from enum ENUM_FIELD_TYPES
	UPPER_BOUNDARY                =1129       # from enum ENUM_FIELD_TYPES
	UPPER_MODIFIER                =1045       # from enum ENUM_FIELD_TYPES
	UPPER_SIZE                    =1049       # from enum ENUM_FIELD_TYPES
	UPPER_TOLERANCE               =1043       # from enum ENUM_FIELD_TYPES
	UPR                           =1006       # from enum ENUM_FIELD_TYPES
	UP_FORCE                      =211        # from enum ENUM_FIELD_TYPES
	USEPIN_TYPE                   =44         # from enum ENUM_FIELD_TYPES
	USER_DEFINED_HITS             =1071       # from enum ENUM_FIELD_TYPES
	USER_DEFINED_THEOS            =794        # from enum ENUM_FIELD_TYPES
	USES_SPECIFIED_TOLERANCE_ZONE_DIRECTION=1128       # from enum ENUM_FIELD_TYPES
	USE_3DFILTER                  =431        # from enum ENUM_FIELD_TYPES
	USE_AXIS                      =139        # from enum ENUM_FIELD_TYPES
	USE_AXIS2                     =753        # from enum ENUM_FIELD_TYPES
	USE_BOUNDARY_OFFSET           =968        # from enum ENUM_FIELD_TYPES
	USE_CAD_PLANAR_SEGREGATION    =924        # from enum ENUM_FIELD_TYPES
	USE_FORM                      =996        # from enum ENUM_FIELD_TYPES
	USE_HSSDAT                    =541        # from enum ENUM_FIELD_TYPES
	USE_INCIDENCE_ANGLE           =1038       # from enum ENUM_FIELD_TYPES
	USE_LOCATION                  =1003       # from enum ENUM_FIELD_TYPES
	USE_MIN_MAX_FIT               =1029       # from enum ENUM_FIELD_TYPES
	USE_SCALING                   =796        # from enum ENUM_FIELD_TYPES
	USE_SCAN_FILTER               =1018       # from enum ENUM_FIELD_TYPES
	USE_SIZE                      =1001       # from enum ENUM_FIELD_TYPES
	USE_STARTENDDELAY             =542        # from enum ENUM_FIELD_TYPES
	USE_THEO                      =281        # from enum ENUM_FIELD_TYPES
	USE_THEOS                     =1062       # from enum ENUM_FIELD_TYPES
	U_HITS                        =318        # from enum ENUM_FIELD_TYPES
	U_L_BOUNDS                    =417        # from enum ENUM_FIELD_TYPES
	VERTICAL_CLIPPING             =900        # from enum ENUM_FIELD_TYPES
	VIDEO_GAIN                    =363        # from enum ENUM_FIELD_TYPES
	VIDEO_LASERLIGHT1             =366        # from enum ENUM_FIELD_TYPES
	VIDEO_LASERLIGHT2             =367        # from enum ENUM_FIELD_TYPES
	VIDEO_LEDLIGHT                =365        # from enum ENUM_FIELD_TYPES
	VIDEO_LSEG                    =370        # from enum ENUM_FIELD_TYPES
	VIDEO_OFFSET                  =364        # from enum ENUM_FIELD_TYPES
	VIDEO_XSEG                    =371        # from enum ENUM_FIELD_TYPES
	VIDEO_YEND                    =369        # from enum ENUM_FIELD_TYPES
	VIDEO_YORIGIN                 =368        # from enum ENUM_FIELD_TYPES
	VIDEO_YSEG                    =372        # from enum ENUM_FIELD_TYPES
	VOID_DETECT                   =512        # from enum ENUM_FIELD_TYPES
	V_HITS                        =319        # from enum ENUM_FIELD_TYPES
	WAVELENGTH                    =1000       # from enum ENUM_FIELD_TYPES
	WAVELENGTHPLANE               =1113       # from enum ENUM_FIELD_TYPES
	WAVE_FILE                     =322        # from enum ENUM_FIELD_TYPES
	WEIGHT                        =137        # from enum ENUM_FIELD_TYPES
	WORK_PLANE                    =154        # from enum ENUM_FIELD_TYPES
	X_OFFSET                      =146        # from enum ENUM_FIELD_TYPES
	Y_OFFSET                      =147        # from enum ENUM_FIELD_TYPES
	ZONES                         =404        # from enum ENUM_FIELD_TYPES
	Z_OFFSET                      =148        # from enum ENUM_FIELD_TYPES
	PCD_FILE_CLOSE                =1          # from enum ENUM_FILE_IO_TYPES
	PCD_FILE_COPY                 =11         # from enum ENUM_FILE_IO_TYPES
	PCD_FILE_DELETE               =13         # from enum ENUM_FILE_IO_TYPES
	PCD_FILE_DIALOG               =15         # from enum ENUM_FILE_IO_TYPES
	PCD_FILE_EXISTS               =14         # from enum ENUM_FILE_IO_TYPES
	PCD_FILE_MOVE                 =12         # from enum ENUM_FILE_IO_TYPES
	PCD_FILE_OPEN                 =0          # from enum ENUM_FILE_IO_TYPES
	PCD_FILE_READBLOCK            =7          # from enum ENUM_FILE_IO_TYPES
	PCD_FILE_READCHARACTER        =5          # from enum ENUM_FILE_IO_TYPES
	PCD_FILE_READLINE             =3          # from enum ENUM_FILE_IO_TYPES
	PCD_FILE_READUPTO             =16         # from enum ENUM_FILE_IO_TYPES
	PCD_FILE_RECALLPOSITION       =10         # from enum ENUM_FILE_IO_TYPES
	PCD_FILE_REWIND               =8          # from enum ENUM_FILE_IO_TYPES
	PCD_FILE_SAVEPOSITION         =9          # from enum ENUM_FILE_IO_TYPES
	PCD_FILE_WRITEBLOCK           =6          # from enum ENUM_FILE_IO_TYPES
	PCD_FILE_WRITECHARACTER       =4          # from enum ENUM_FILE_IO_TYPES
	PCD_FILE_WRITELINE            =2          # from enum ENUM_FILE_IO_TYPES
	PCD_FILE_APPEND               =3          # from enum ENUM_FILE_OPEN_TYPES
	PCD_FILE_READ                 =2          # from enum ENUM_FILE_OPEN_TYPES
	PCD_FILE_WRITE                =1          # from enum ENUM_FILE_OPEN_TYPES
	FILTER_LINEAR                 =0          # from enum ENUM_FILTER_TYPES
	FILTER_POLAR                  =1          # from enum ENUM_FILTER_TYPES
	GENERIC_ALIGN_DEPENDENT       =0          # from enum ENUM_GENERIC_ALIGN
	GENERIC_ALIGN_INDEPENDENT     =1          # from enum ENUM_GENERIC_ALIGN
	GENERIC_DISPLAY_DIAMETER      =1          # from enum ENUM_GENERIC_DISPLAY
	GENERIC_DISPLAY_RADIUS        =0          # from enum ENUM_GENERIC_DISPLAY
	GENERIC_CIRCLE                =3          # from enum ENUM_GENERIC_TYPES
	GENERIC_CONE                  =8          # from enum ENUM_GENERIC_TYPES
	GENERIC_CYLINDER              =5          # from enum ENUM_GENERIC_TYPES
	GENERIC_LINE                  =2          # from enum ENUM_GENERIC_TYPES
	GENERIC_NONE                  =9          # from enum ENUM_GENERIC_TYPES
	GENERIC_PLANE                 =1          # from enum ENUM_GENERIC_TYPES
	GENERIC_POINT                 =0          # from enum ENUM_GENERIC_TYPES
	GENERIC_ROUND_SLOT            =6          # from enum ENUM_GENERIC_TYPES
	GENERIC_SPHERE                =4          # from enum ENUM_GENERIC_TYPES
	GENERIC_SQUARE_SLOT           =7          # from enum ENUM_GENERIC_TYPES
	HATCH_STYLE_BDIAGONAL         =3          # from enum ENUM_HATCH_STYLE
	HATCH_STYLE_CROSS             =4          # from enum ENUM_HATCH_STYLE
	HATCH_STYLE_DIAGCROSS         =5          # from enum ENUM_HATCH_STYLE
	HATCH_STYLE_FDIAGONAL         =2          # from enum ENUM_HATCH_STYLE
	HATCH_STYLE_HORIZONTAL        =0          # from enum ENUM_HATCH_STYLE
	HATCH_STYLE_NONE              =99         # from enum ENUM_HATCH_STYLE
	HATCH_STYLE_VERTICAL          =1          # from enum ENUM_HATCH_STYLE
	NEWALIGN                      =0          # from enum ENUM_MARK_NEW_ALIGNMENT_MODE
	SAMEALIGN                     =1          # from enum ENUM_MARK_NEW_ALIGNMENT_MODE
	MEASURE_BOTH                  =0          # from enum ENUM_MASTERSLAVEDIALOG_MEASUREARM
	MEASURE_MASTER                =1          # from enum ENUM_MASTERSLAVEDIALOG_MEASUREARM
	MEASURE_SLAVE                 =2          # from enum ENUM_MASTERSLAVEDIALOG_MEASUREARM
	MEASURE_DCC                   =1          # from enum ENUM_MASTERSLAVEDIALOG_MEASUREDCC
	MEASURE_MANUAL                =0          # from enum ENUM_MASTERSLAVEDIALOG_MEASUREDCC
	PAPER_10X11                   =45         # from enum ENUM_PAGE_FORMAT
	PAPER_10X14                   =16         # from enum ENUM_PAGE_FORMAT
	PAPER_11X17                   =17         # from enum ENUM_PAGE_FORMAT
	PAPER_12X11                   =90         # from enum ENUM_PAGE_FORMAT
	PAPER_15X11                   =46         # from enum ENUM_PAGE_FORMAT
	PAPER_9X11                    =44         # from enum ENUM_PAGE_FORMAT
	PAPER_A2                      =66         # from enum ENUM_PAGE_FORMAT
	PAPER_A3                      =8          # from enum ENUM_PAGE_FORMAT
	PAPER_A3_EXTRA                =63         # from enum ENUM_PAGE_FORMAT
	PAPER_A3_EXTRA_TRANSVERSE     =68         # from enum ENUM_PAGE_FORMAT
	PAPER_A3_ROTATED              =76         # from enum ENUM_PAGE_FORMAT
	PAPER_A3_TRANSVERSE           =67         # from enum ENUM_PAGE_FORMAT
	PAPER_A4                      =9          # from enum ENUM_PAGE_FORMAT
	PAPER_A4SMALL                 =10         # from enum ENUM_PAGE_FORMAT
	PAPER_A4_EXTRA                =53         # from enum ENUM_PAGE_FORMAT
	PAPER_A4_PLUS                 =60         # from enum ENUM_PAGE_FORMAT
	PAPER_A4_ROTATED              =77         # from enum ENUM_PAGE_FORMAT
	PAPER_A4_TRANSVERSE           =55         # from enum ENUM_PAGE_FORMAT
	PAPER_A5                      =11         # from enum ENUM_PAGE_FORMAT
	PAPER_A5_EXTRA                =64         # from enum ENUM_PAGE_FORMAT
	PAPER_A5_ROTATED              =78         # from enum ENUM_PAGE_FORMAT
	PAPER_A5_TRANSVERSE           =61         # from enum ENUM_PAGE_FORMAT
	PAPER_A6                      =70         # from enum ENUM_PAGE_FORMAT
	PAPER_A6_ROTATED              =83         # from enum ENUM_PAGE_FORMAT
	PAPER_A_PLUS                  =57         # from enum ENUM_PAGE_FORMAT
	PAPER_B4                      =12         # from enum ENUM_PAGE_FORMAT
	PAPER_B4_JIS_ROTATED          =79         # from enum ENUM_PAGE_FORMAT
	PAPER_B5                      =13         # from enum ENUM_PAGE_FORMAT
	PAPER_B5_EXTRA                =65         # from enum ENUM_PAGE_FORMAT
	PAPER_B5_JIS_ROTATED          =80         # from enum ENUM_PAGE_FORMAT
	PAPER_B5_TRANSVERSE           =62         # from enum ENUM_PAGE_FORMAT
	PAPER_B6_JIS                  =88         # from enum ENUM_PAGE_FORMAT
	PAPER_B6_JIS_ROTATED          =89         # from enum ENUM_PAGE_FORMAT
	PAPER_B_PLUS                  =58         # from enum ENUM_PAGE_FORMAT
	PAPER_CSHEET                  =24         # from enum ENUM_PAGE_FORMAT
	PAPER_DBL_JAPANESE_POSTCARD   =69         # from enum ENUM_PAGE_FORMAT
	PAPER_DBL_JAPANESE_POSTCARD_ROTATED=82         # from enum ENUM_PAGE_FORMAT
	PAPER_DSHEET                  =25         # from enum ENUM_PAGE_FORMAT
	PAPER_ENV_10                  =20         # from enum ENUM_PAGE_FORMAT
	PAPER_ENV_11                  =21         # from enum ENUM_PAGE_FORMAT
	PAPER_ENV_12                  =22         # from enum ENUM_PAGE_FORMAT
	PAPER_ENV_14                  =23         # from enum ENUM_PAGE_FORMAT
	PAPER_ENV_9                   =19         # from enum ENUM_PAGE_FORMAT
	PAPER_ENV_B4                  =33         # from enum ENUM_PAGE_FORMAT
	PAPER_ENV_B5                  =34         # from enum ENUM_PAGE_FORMAT
	PAPER_ENV_B6                  =35         # from enum ENUM_PAGE_FORMAT
	PAPER_ENV_C3                  =29         # from enum ENUM_PAGE_FORMAT
	PAPER_ENV_C4                  =30         # from enum ENUM_PAGE_FORMAT
	PAPER_ENV_C5                  =28         # from enum ENUM_PAGE_FORMAT
	PAPER_ENV_C6                  =31         # from enum ENUM_PAGE_FORMAT
	PAPER_ENV_C65                 =32         # from enum ENUM_PAGE_FORMAT
	PAPER_ENV_DL                  =27         # from enum ENUM_PAGE_FORMAT
	PAPER_ENV_INVITE              =47         # from enum ENUM_PAGE_FORMAT
	PAPER_ENV_ITALY               =36         # from enum ENUM_PAGE_FORMAT
	PAPER_ENV_MONARCH             =37         # from enum ENUM_PAGE_FORMAT
	PAPER_ENV_PERSONAL            =38         # from enum ENUM_PAGE_FORMAT
	PAPER_ESHEET                  =26         # from enum ENUM_PAGE_FORMAT
	PAPER_EXECUTIVE               =7          # from enum ENUM_PAGE_FORMAT
	PAPER_FANFOLD_LGL_GERMAN      =41         # from enum ENUM_PAGE_FORMAT
	PAPER_FANFOLD_STD_GERMAN      =40         # from enum ENUM_PAGE_FORMAT
	PAPER_FANFOLD_US              =39         # from enum ENUM_PAGE_FORMAT
	PAPER_FOLIO                   =14         # from enum ENUM_PAGE_FORMAT
	PAPER_ISO_B4                  =42         # from enum ENUM_PAGE_FORMAT
	PAPER_JAPANESE_POSTCARD       =43         # from enum ENUM_PAGE_FORMAT
	PAPER_JAPANESE_POSTCARD_ROTATED=81         # from enum ENUM_PAGE_FORMAT
	PAPER_JENV_CHOU3              =73         # from enum ENUM_PAGE_FORMAT
	PAPER_JENV_CHOU3_ROTATED      =86         # from enum ENUM_PAGE_FORMAT
	PAPER_JENV_CHOU4              =74         # from enum ENUM_PAGE_FORMAT
	PAPER_JENV_CHOU4_ROTATED      =87         # from enum ENUM_PAGE_FORMAT
	PAPER_JENV_KAKU2              =71         # from enum ENUM_PAGE_FORMAT
	PAPER_JENV_KAKU2_ROTATED      =84         # from enum ENUM_PAGE_FORMAT
	PAPER_JENV_KAKU3              =72         # from enum ENUM_PAGE_FORMAT
	PAPER_JENV_KAKU3_ROTATED      =85         # from enum ENUM_PAGE_FORMAT
	PAPER_JENV_YOU4               =91         # from enum ENUM_PAGE_FORMAT
	PAPER_JENV_YOU4_ROTATED       =92         # from enum ENUM_PAGE_FORMAT
	PAPER_LEDGER                  =4          # from enum ENUM_PAGE_FORMAT
	PAPER_LEGAL                   =5          # from enum ENUM_PAGE_FORMAT
	PAPER_LEGAL_EXTRA             =51         # from enum ENUM_PAGE_FORMAT
	PAPER_LETTER                  =1          # from enum ENUM_PAGE_FORMAT
	PAPER_LETTERSMALL             =2          # from enum ENUM_PAGE_FORMAT
	PAPER_LETTER_EXTRA            =50         # from enum ENUM_PAGE_FORMAT
	PAPER_LETTER_EXTRA_TRANSVERSE =56         # from enum ENUM_PAGE_FORMAT
	PAPER_LETTER_PLUS             =59         # from enum ENUM_PAGE_FORMAT
	PAPER_LETTER_ROTATED          =75         # from enum ENUM_PAGE_FORMAT
	PAPER_LETTER_TRANSVERSE       =54         # from enum ENUM_PAGE_FORMAT
	PAPER_NOTE                    =18         # from enum ENUM_PAGE_FORMAT
	PAPER_P16K                    =93         # from enum ENUM_PAGE_FORMAT
	PAPER_P16K_ROTATED            =106        # from enum ENUM_PAGE_FORMAT
	PAPER_P32K                    =94         # from enum ENUM_PAGE_FORMAT
	PAPER_P32KBIG                 =95         # from enum ENUM_PAGE_FORMAT
	PAPER_P32KBIG_ROTATED         =108        # from enum ENUM_PAGE_FORMAT
	PAPER_P32K_ROTATED            =107        # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_1                  =96         # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_10                 =105        # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_10_ROTATED         =118        # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_1_ROTATED          =109        # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_2                  =97         # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_2_ROTATED          =110        # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_3                  =98         # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_3_ROTATED          =111        # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_4                  =99         # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_4_ROTATED          =112        # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_5                  =100        # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_5_ROTATED          =113        # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_6                  =101        # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_6_ROTATED          =114        # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_7                  =102        # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_7_ROTATED          =115        # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_8                  =103        # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_8_ROTATED          =116        # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_9                  =104        # from enum ENUM_PAGE_FORMAT
	PAPER_PENV_9_ROTATED          =117        # from enum ENUM_PAGE_FORMAT
	PAPER_QUARTO                  =15         # from enum ENUM_PAGE_FORMAT
	PAPER_STATEMENT               =6          # from enum ENUM_PAGE_FORMAT
	PAPER_TABLOID                 =3          # from enum ENUM_PAGE_FORMAT
	PAPER_TABLOID_EXTRA           =52         # from enum ENUM_PAGE_FORMAT
	ORIENT_LANDSCAPE              =2          # from enum ENUM_PAGE_ORIENTATION
	ORIENT_PORTRAIT               =1          # from enum ENUM_PAGE_ORIENTATION
	PCDMSG_ABORT                  =3          # from enum ENUM_PCDMSG_RETVALS
	PCDMSG_CANCEL                 =2          # from enum ENUM_PCDMSG_RETVALS
	PCDMSG_IGNORE                 =5          # from enum ENUM_PCDMSG_RETVALS
	PCDMSG_NO                     =7          # from enum ENUM_PCDMSG_RETVALS
	PCDMSG_OK                     =1          # from enum ENUM_PCDMSG_RETVALS
	PCDMSG_RETRY                  =4          # from enum ENUM_PCDMSG_RETVALS
	PCDMSG_YES                    =6          # from enum ENUM_PCDMSG_RETVALS
	MSGTYP_ABORTRETRYIGNORE       =2          # from enum ENUM_PCDMSG_TYPES
	MSGTYP_DEFBUTTON2             =256        # from enum ENUM_PCDMSG_TYPES
	MSGTYP_DEFBUTTON3             =512        # from enum ENUM_PCDMSG_TYPES
	MSGTYP_ICONASTERISK           =64         # from enum ENUM_PCDMSG_TYPES
	MSGTYP_ICONEXCLAMATION        =48         # from enum ENUM_PCDMSG_TYPES
	MSGTYP_ICONHAND               =16         # from enum ENUM_PCDMSG_TYPES
	MSGTYP_ICONQUESTION           =32         # from enum ENUM_PCDMSG_TYPES
	MSGTYP_OK                     =0          # from enum ENUM_PCDMSG_TYPES
	MSGTYP_OKCANCEL               =1          # from enum ENUM_PCDMSG_TYPES
	MSGTYP_RETRY_CANCEL           =5          # from enum ENUM_PCDMSG_TYPES
	MSGTYP_YESNO                  =4          # from enum ENUM_PCDMSG_TYPES
	MSGTYP_YESNOCANCEL            =3          # from enum ENUM_PCDMSG_TYPES
	PCD_COMMENT_DOCUMENTATION     =3          # from enum ENUM_PCD_COMMENT_TYPES
	PCD_COMMENT_INPUT             =2          # from enum ENUM_PCD_COMMENT_TYPES
	PCD_COMMENT_OPER              =0          # from enum ENUM_PCD_COMMENT_TYPES
	PCD_COMMENT_READOUT           =5          # from enum ENUM_PCD_COMMENT_TYPES
	PCD_COMMENT_REPORT            =1          # from enum ENUM_PCD_COMMENT_TYPES
	PCD_COMMENT_YESNO             =4          # from enum ENUM_PCD_COMMENT_TYPES
	DMIS_OFF                      =0          # from enum ENUM_PCD_ON_OFF
	DMIS_ON                       =1          # from enum ENUM_PCD_ON_OFF
	PCD_STATS_DATABASE            =4          # from enum ENUM_PCD_STAT_TYPES
	PCD_STATS_OFF                 =0          # from enum ENUM_PCD_STAT_TYPES
	PCD_STATS_ON                  =1          # from enum ENUM_PCD_STAT_TYPES
	PCD_STATS_RECORD              =5          # from enum ENUM_PCD_STAT_TYPES
	PCD_STATS_TRANSFER            =2          # from enum ENUM_PCD_STAT_TYPES
	PCD_STATS_UPDATE              =3          # from enum ENUM_PCD_STAT_TYPES
	PLANE_BACK                    =2          # from enum ENUM_PLANE_TYPE
	PLANE_BOTTOM                  =3          # from enum ENUM_PLANE_TYPE
	PLANE_FRONT                   =5          # from enum ENUM_PLANE_TYPE
	PLANE_LEFT                    =4          # from enum ENUM_PLANE_TYPE
	PLANE_RIGHT                   =1          # from enum ENUM_PLANE_TYPE
	PLANE_TOP                     =0          # from enum ENUM_PLANE_TYPE
	DEVIATION_INFO                =4          # from enum ENUM_POINT_INFO_TYPES
	MEAS_POINT_INFO               =2          # from enum ENUM_POINT_INFO_TYPES
	MEAS_VECTOR_INFO              =3          # from enum ENUM_POINT_INFO_TYPES
	THEO_POINT_INFO               =0          # from enum ENUM_POINT_INFO_TYPES
	THEO_VECTOR_INFO              =1          # from enum ENUM_POINT_INFO_TYPES
	BUTTON_NOT_AVAILABLE          =1          # from enum ENUM_PRESS_BUTTON_RESULTS
	DIALOG_ALREADY_CLOSED         =2          # from enum ENUM_PRESS_BUTTON_RESULTS
	DIALOG_NOT_FOUND              =3          # from enum ENUM_PRESS_BUTTON_RESULTS
	SUCCESS                       =0          # from enum ENUM_PRESS_BUTTON_RESULTS
	CREATE_NEW_MAP                =0          # from enum ENUM_QUAL_CREATE_REPLACE
	REPLACE_CLOSET_MAP            =1          # from enum ENUM_QUAL_CREATE_REPLACE
	RT_CUSTOM                     =3          # from enum ENUM_RELEASE_TYPE
	RT_QA                         =0          # from enum ENUM_RELEASE_TYPE
	RT_RELEASE                    =2          # from enum ENUM_RELEASE_TYPE
	RT_RELEASE_CANDIDATE          =1          # from enum ENUM_RELEASE_TYPE
	ID_HOB_ARC                    =60478      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_BITMAP                 =60462      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_BORDER                 =60473      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_CADIMAGEOBJECT_OB      =19105      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_CIRCLE                 =60471      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_GAUGE                  =60452      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_GRAPH                  =60458      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_LINE                   =60450      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_PCD_ANALWIN_OB         =19104      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_PCD_CAD_REPORT_OBJECT  =26514      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_PCD_COMMAND_TEXT_OB    =26324      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_PCD_DIMCOLOR_OB        =19102      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_PCD_GRID_CTRL_OB       =19100      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_PCD_LABEL_OB           =26603      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_PCD_LEADERLINE_OB      =19101      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_PCD_SPC_CHART_OB       =26619      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_PCD_TEXT_REPORT_OBJECT =26515      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_POLYLINE               =60472      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_PTR                    =60459      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_TEXT                   =60448      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	ID_HOB_TEXT_RT                =60449      # from enum ENUM_REPORT_TEMPLATE_OBJECTS
	RMEAS_ABSOLUTE                =1          # from enum ENUM_RMEAS_MODE
	RMEAS_NORMAL                  =0          # from enum ENUM_RMEAS_MODE
	RMEAS_DEFAULT                 =1          # from enum ENUM_RMEAS_MODE_NEW
	RMEAS_LEGACY                  =0          # from enum ENUM_RMEAS_MODE_NEW
	SCAN_INNER                    =0          # from enum ENUM_SCAN_INOUT_TYPES
	SCAN_OUTER                    =1          # from enum ENUM_SCAN_INOUT_TYPES
	SCAN_PLANAR                   =2          # from enum ENUM_SCAN_INOUT_TYPES
	PCD_STAT_DIM_NAME             =0          # from enum ENUM_STAT_NAME_TYPES
	PCD_STAT_FEAT_NAME            =1          # from enum ENUM_STAT_NAME_TYPES
	TIP_ANALOG_BALL               =16         # from enum ENUM_TIPTYPES
	TIP_ANALOG_DISK               =17         # from enum ENUM_TIPTYPES
	TIP_ANALOG_OPTIC              =20         # from enum ENUM_TIPTYPES
	TIP_ANALOG_SHANK              =18         # from enum ENUM_TIPTYPES
	TIP_BALL                      =0          # from enum ENUM_TIPTYPES
	TIP_DISK                      =1          # from enum ENUM_TIPTYPES
	TIP_FIXED_BALL                =32         # from enum ENUM_TIPTYPES
	TIP_FIXED_DISK                =33         # from enum ENUM_TIPTYPES
	TIP_FIXED_OPTIC               =36         # from enum ENUM_TIPTYPES
	TIP_FIXED_SHANK               =34         # from enum ENUM_TIPTYPES
	TIP_INFINIT_ARM               =256        # from enum ENUM_TIPTYPES
	TIP_OPTIC                     =4          # from enum ENUM_TIPTYPES
	TIP_SHANK                     =2          # from enum ENUM_TIPTYPES
	TIP_SLAVE                     =512        # from enum ENUM_TIPTYPES
	TIP_SP600                     =64         # from enum ENUM_TIPTYPES
	TIP_WB_OPTIC                  =128        # from enum ENUM_TIPTYPES
	TOOL_MOVED_ASK                =2          # from enum ENUM_TOOL_MOVED
	TOOL_MOVED_NO                 =0          # from enum ENUM_TOOL_MOVED
	TOOL_MOVED_YES                =1          # from enum ENUM_TOOL_MOVED
	MAJOR_MINOR_THIRD_ROTATE_ONLY =3          # from enum ENUM_TRANSFORMATION_TYPES
	MAJOR_MINOR_THIRD_ROT_AND_TRANS=2          # from enum ENUM_TRANSFORMATION_TYPES
	ROTATE_AND_TRANSLATE          =0          # from enum ENUM_TRANSFORMATION_TYPES
	ROTATE_ONLY                   =1          # from enum ENUM_TRANSFORMATION_TYPES
	VISION_TES_DOMINANT_EDGE      =0          # from enum ENUM_VISION_TARGET_EDGE_SELECTION
	VISION_TES_MATCHING_EDGE      =2          # from enum ENUM_VISION_TARGET_EDGE_SELECTION
	VISION_TES_NEAREST_NOMINAL_EDGE=1          # from enum ENUM_VISION_TARGET_EDGE_SELECTION
	VISION_TES_SPECIFIED_EDGE     =3          # from enum ENUM_VISION_TARGET_EDGE_SELECTION
	VISION_TFR_10MM               =7          # from enum ENUM_VISION_TARGET_FOCUS_RANGE
	VISION_TFR_1MM                =2          # from enum ENUM_VISION_TARGET_FOCUS_RANGE
	VISION_TFR_20MM               =8          # from enum ENUM_VISION_TARGET_FOCUS_RANGE
	VISION_TFR_2MM                =3          # from enum ENUM_VISION_TARGET_FOCUS_RANGE
	VISION_TFR_3MM                =4          # from enum ENUM_VISION_TARGET_FOCUS_RANGE
	VISION_TFR_4MM                =5          # from enum ENUM_VISION_TARGET_FOCUS_RANGE
	VISION_TFR_50MM               =9          # from enum ENUM_VISION_TARGET_FOCUS_RANGE
	VISION_TFR_5MM                =6          # from enum ENUM_VISION_TARGET_FOCUS_RANGE
	VISION_TFR_HALFMM             =1          # from enum ENUM_VISION_TARGET_FOCUS_RANGE
	VISION_TFR_TENTHMM            =0          # from enum ENUM_VISION_TARGET_FOCUS_RANGE
	VISION_TPD_HIGH               =3          # from enum ENUM_VISION_TARGET_POINT_DENSITY
	VISION_TPD_LOW                =1          # from enum ENUM_VISION_TARGET_POINT_DENSITY
	VISION_TPD_NONE               =0          # from enum ENUM_VISION_TARGET_POINT_DENSITY
	VISION_TPD_NORMAL             =2          # from enum ENUM_VISION_TARGET_POINT_DENSITY
	VISION_TARGET_TYPE_AUTOMATIC  =2          # from enum ENUM_VISION_TARGET_TYPE
	VISION_TARGET_TYPE_COMPARATOR =3          # from enum ENUM_VISION_TARGET_TYPE
	VISION_TARGET_TYPE_GAGE       =0          # from enum ENUM_VISION_TARGET_TYPE
	VISION_TARGET_TYPE_MANUAL_TARGET=1          # from enum ENUM_VISION_TARGET_TYPE
	ERROR_JUMPLABEL               =1          # from enum ERRORMODES
	ERROR_LASER_SKIP              =1          # from enum ERRORMODES
	ERROR_OFF                     =0          # from enum ERRORMODES
	ERROR_SETVAR                  =2          # from enum ERRORMODES
	ERROR_SKIP                    =3          # from enum ERRORMODES
	ERROR_EDGE_NOT_DETECTED       =3          # from enum ERRORTYPES
	ERROR_FOCUS_NOT_DETECTED      =4          # from enum ERRORTYPES
	ERROR_LASER_ERROR             =5          # from enum ERRORTYPES
	ERROR_MISSED_HIT              =1          # from enum ERRORTYPES
	ERROR_REFLECTOR_NOT_FOUND     =2          # from enum ERRORTYPES
	ERROR_UNEXPECTED_HIT          =0          # from enum ERRORTYPES
	EVAL_ACTUALS                  =2          # from enum EVALUATION_TYPES
	EVAL_BOTH                     =3          # from enum EVALUATION_TYPES
	EVAL_NOMINALS                 =1          # from enum EVALUATION_TYPES
	Chn                           =63007      # from enum Enum_Language_Type
	Cze                           =63011      # from enum Enum_Language_Type
	Eng                           =63000      # from enum Enum_Language_Type
	Frn                           =63002      # from enum Enum_Language_Type
	Grm                           =63003      # from enum Enum_Language_Type
	Hng                           =63015      # from enum Enum_Language_Type
	Ita                           =63001      # from enum Enum_Language_Type
	Jpn                           =63006      # from enum Enum_Language_Type
	Kor                           =63008      # from enum Enum_Language_Type
	Nld                           =63016      # from enum Enum_Language_Type
	Pol                           =63009      # from enum Enum_Language_Type
	Prt                           =63005      # from enum Enum_Language_Type
	Rus                           =63010      # from enum Enum_Language_Type
	Spn                           =63004      # from enum Enum_Language_Type
	Swe                           =63012      # from enum Enum_Language_Type
	Trk                           =63014      # from enum Enum_Language_Type
	Twn                           =63013      # from enum Enum_Language_Type
	FDATA_CAD                     =5          # from enum FDATA_COORDSYS
	FDATA_MACHINE                 =11         # from enum FDATA_COORDSYS
	FDATA_PART                    =13         # from enum FDATA_COORDSYS
	FDATA_PARTMM3                 =10         # from enum FDATA_COORDSYS
	FDATA_POLAR                   =4          # from enum FDATA_COORDSYS
	FDATA_ALL                     =100        # from enum FDATA_DATASET
	FDATA_MEAS                    =3          # from enum FDATA_DATASET
	FDATA_TARG                    =27         # from enum FDATA_DATASET
	FDATA_THEO                    =2          # from enum FDATA_DATASET
	FDATA_AB_ANGLES               =48         # from enum FDATA_TYPES
	FDATA_ANALOG_DEVIATIONS       =46         # from enum FDATA_TYPES
	FDATA_ANGLE                   =16         # from enum FDATA_TYPES
	FDATA_ANGLE2                  =53         # from enum FDATA_TYPES
	FDATA_ANGLE_VECTOR            =29         # from enum FDATA_TYPES
	FDATA_AUTO_MOVE_DISTANCE      =25         # from enum FDATA_TYPES
	FDATA_CENTROID                =0          # from enum FDATA_TYPES
	FDATA_CORNER_RADIUS           =47         # from enum FDATA_TYPES
	FDATA_CORNER_VECTOR2          =58         # from enum FDATA_TYPES
	FDATA_CORNER_VECTOR3          =60         # from enum FDATA_TYPES
	FDATA_DEPTH                   =26         # from enum FDATA_TYPES
	FDATA_DEVIATION               =18         # from enum FDATA_TYPES
	FDATA_DIAMETER                =6          # from enum FDATA_TYPES
	FDATA_ENDPOINT                =9          # from enum FDATA_TYPES
	FDATA_FLUSH                   =79         # from enum FDATA_TYPES
	FDATA_FOCUS1                  =69         # from enum FDATA_TYPES
	FDATA_FOCUS2                  =70         # from enum FDATA_TYPES
	FDATA_GAP2                    =80         # from enum FDATA_TYPES
	FDATA_HEIGHT                  =40         # from enum FDATA_TYPES
	FDATA_INDENT                  =24         # from enum FDATA_TYPES
	FDATA_INDENT2                 =62         # from enum FDATA_TYPES
	FDATA_INDENT3                 =63         # from enum FDATA_TYPES
	FDATA_LENGTH                  =14         # from enum FDATA_TYPES
	FDATA_MAJOR_AXIS              =2001       # from enum FDATA_TYPES
	FDATA_MANSCAN_INCR_DIST       =74         # from enum FDATA_TYPES
	FDATA_MANSCAN_INCR_TIME       =75         # from enum FDATA_TYPES
	FDATA_MEASURE_VECTOR          =41         # from enum FDATA_TYPES
	FDATA_MIDPOINT                =8          # from enum FDATA_TYPES
	FDATA_MINOR_AXIS              =15         # from enum FDATA_TYPES
	FDATA_MIN_CIRC_SCAN_DOWN      =78         # from enum FDATA_TYPES
	FDATA_MIN_CIRC_SCAN_INIT      =77         # from enum FDATA_TYPES
	FDATA_OFFSET                  =64         # from enum FDATA_TYPES
	FDATA_ORG_HIT_VECTOR          =49         # from enum FDATA_TYPES
	FDATA_PIN_DIAMETER            =35         # from enum FDATA_TYPES
	FDATA_PIN_VECTOR              =33         # from enum FDATA_TYPES
	FDATA_PUNCH_VECTOR            =31         # from enum FDATA_TYPES
	FDATA_REPORT_SURF_VECTOR      =38         # from enum FDATA_TYPES
	FDATA_REPORT_VECTOR           =36         # from enum FDATA_TYPES
	FDATA_ROTAB_ANGLE             =66         # from enum FDATA_TYPES
	FDATA_SCANSEG_END             =73         # from enum FDATA_TYPES
	FDATA_SCANSEG_START           =72         # from enum FDATA_TYPES
	FDATA_SLOT_VECTOR             =2002       # from enum FDATA_TYPES
	FDATA_SNAP_CENTROID           =45         # from enum FDATA_TYPES
	FDATA_SPACER                  =23         # from enum FDATA_TYPES
	FDATA_STARTPOINT              =7          # from enum FDATA_TYPES
	FDATA_SURFACEVECTOR2          =67         # from enum FDATA_TYPES
	FDATA_SURFACEVECTOR2NONORM    =68         # from enum FDATA_TYPES
	FDATA_SURFACE_VECTOR          =19         # from enum FDATA_TYPES
	FDATA_TARGET                  =27         # from enum FDATA_TYPES
	FDATA_THICKNESS               =21         # from enum FDATA_TYPES
	FDATA_TIPRADIUS               =65         # from enum FDATA_TYPES
	FDATA_UPDATE_VECTOR           =43         # from enum FDATA_TYPES
	FDATA_VECTOR                  =1          # from enum FDATA_TYPES
	FDATA_VERTEX                  =71         # from enum FDATA_TYPES
	FDATA_WIDTH                   =2000       # from enum FDATA_TYPES
	FDATA_WIDTH2                  =76         # from enum FDATA_TYPES
	FHITDATA_BALLCENTER           =12         # from enum FHITDATA_TYPES
	FHITDATA_CENTROID             =0          # from enum FHITDATA_TYPES
	FHITDATA_VECTOR               =1          # from enum FHITDATA_TYPES
	FPOINT_BALLCENTER             =12         # from enum FPOINT_TYPES
	FPOINT_CENTROID               =0          # from enum FPOINT_TYPES
	FPOINT_ENDPOINT               =9          # from enum FPOINT_TYPES
	FPOINT_MIDPOINT               =8          # from enum FPOINT_TYPES
	FPOINT_SNAP_CENTROID          =45         # from enum FPOINT_TYPES
	FPOINT_STARTPOINT             =7          # from enum FPOINT_TYPES
	FVECTOR_ANGLE_VECTOR          =29         # from enum FVECTOR_TYPES
	FVECTOR_CORNER_VECTOR2        =58         # from enum FVECTOR_TYPES
	FVECTOR_CORNER_VECTOR3        =60         # from enum FVECTOR_TYPES
	FVECTOR_MEASURE_VECTOR        =41         # from enum FVECTOR_TYPES
	FVECTOR_ORG_HIT_VECTOR        =49         # from enum FVECTOR_TYPES
	FVECTOR_PIN_VECTOR            =33         # from enum FVECTOR_TYPES
	FVECTOR_PUNCH_VECTOR          =31         # from enum FVECTOR_TYPES
	FVECTOR_REPORT_SURF_VECTOR    =38         # from enum FVECTOR_TYPES
	FVECTOR_REPORT_VECTOR         =36         # from enum FVECTOR_TYPES
	FVECTOR_SLOT_VECTOR           =2002       # from enum FVECTOR_TYPES
	FVECTOR_SURFACE_VECTOR        =19         # from enum FVECTOR_TYPES
	FVECTOR_UPDATE_VECTOR         =43         # from enum FVECTOR_TYPES
	FVECTOR_VECTOR                =1          # from enum FVECTOR_TYPES
	PCD_DIMENSION                 =1000       # from enum GETIDTYPE
	PCD_FEATURE                   =31         # from enum GETIDTYPE
	PCD__ALIGNMENT                =1          # from enum GETIDTYPE
	GUESS_MANUAL_SCAN             =26211      # from enum GUESSTYPE
	GUESS_MEASURED_CIRCLE         =26204      # from enum GUESSTYPE
	GUESS_MEASURED_CONE           =26205      # from enum GUESSTYPE
	GUESS_MEASURED_CYLINDER       =26206      # from enum GUESSTYPE
	GUESS_MEASURED_GUESS          =26210      # from enum GUESSTYPE
	GUESS_MEASURED_LINE           =26202      # from enum GUESSTYPE
	GUESS_MEASURED_PLANE          =26203      # from enum GUESSTYPE
	GUESS_MEASURED_POINT          =26201      # from enum GUESSTYPE
	GUESS_MEASURED_ROUND_SLOT     =26208      # from enum GUESSTYPE
	GUESS_MEASURED_SPHERE         =26207      # from enum GUESSTYPE
	GUESS_MEASURED_SQUARE_SLOT    =26209      # from enum GUESSTYPE
	SEARCH_MODE_BOX               =0          # from enum HIGH_POINT_SEARCH_MODES
	SEARCH_MODE_CIRCULAR          =1          # from enum HIGH_POINT_SEARCH_MODES
	PCD_SLOTVECTOR                =609        # from enum IJKTYPES
	PCD_SURFACEVECTOR             =610        # from enum IJKTYPES
	PCD__VECTOR                   =608        # from enum IJKTYPES
	PCD_AV_ERROR                  =2          # from enum ITERATEFLAGS
	PCD_BODY_AX                   =1          # from enum ITERATEFLAGS
	PCD_MEAS_ALL                  =4          # from enum ITERATEFLAGS
	PCD_MEAS_ALL_ALWAYS           =8          # from enum ITERATEFLAGS
	PCD_CLOCKWISE                 =1          # from enum MOVEDIRECTION
	PCD_COUNTERCLOCKWISE          =2          # from enum MOVEDIRECTION
	PCD_SHORTEST                  =3          # from enum MOVEDIRECTION
	PCD_CIRCULAR                  =92         # from enum MOVETYPE
	PCD_CLEARPLANE                =90         # from enum MOVETYPE
	PCD_INCREMENT                 =91         # from enum MOVETYPE
	PCD_POINT                     =93         # from enum MOVETYPE
	PCD_ROTAB                     =94         # from enum MOVETYPE
	MachineConnected              =2          # from enum MachineConnectionStatus
	MachineConnecting             =1          # from enum MachineConnectionStatus
	MachineDisconnecting          =3          # from enum MachineConnectionStatus
	MachineHoming                 =4          # from enum MachineConnectionStatus
	MachineNotConnected           =0          # from enum MachineConnectionStatus
	NotAvailable                  =-1         # from enum MachineConnectionStatus
	ADJUST_FILTER                 =595        # from enum OBTYPE
	ANALYSIS_VIEW                 =176        # from enum OBTYPE
	ANGLE_HIT                     =107        # from enum OBTYPE
	ANYORDER_EXECUTETOL           =215        # from enum OBTYPE
	ARRAY_INDEX                   =95         # from enum OBTYPE
	ASME_SIZE_COMMAND             =1321       # from enum OBTYPE
	ASME_TOLERANCE_COMMAND        =1302       # from enum OBTYPE
	ASSIGNMENT                    =195        # from enum OBTYPE
	ATTACH_PROGRAM                =22         # from enum OBTYPE
	AUTOCALIB_MASTERSLAVE_COMMAND =144        # from enum OBTYPE
	AUTOCALIB_PROBE_COMMAND       =143        # from enum OBTYPE
	AUTOTRIGGERCOMMAND            =116        # from enum OBTYPE
	AUTO_ANGLE_FEATURE            =643        # from enum OBTYPE
	AUTO_BLOB                     =626        # from enum OBTYPE
	AUTO_CIRCLE                   =648        # from enum OBTYPE
	AUTO_CONE                     =655        # from enum OBTYPE
	AUTO_CORNER_FEATURE           =644        # from enum OBTYPE
	AUTO_CYLINDER                 =656        # from enum OBTYPE
	AUTO_EDGE_FEATURE             =642        # from enum OBTYPE
	AUTO_ELLIPSE                  =649        # from enum OBTYPE
	AUTO_FLUSH_GAP                =625        # from enum OBTYPE
	AUTO_HIGH_FEATURE             =645        # from enum OBTYPE
	AUTO_LINE                     =646        # from enum OBTYPE
	AUTO_NOTCH                    =652        # from enum OBTYPE
	AUTO_PLANE                    =647        # from enum OBTYPE
	AUTO_POLYGON                  =654        # from enum OBTYPE
	AUTO_PROFILE_2D               =623        # from enum OBTYPE
	AUTO_ROUND_SLOT               =650        # from enum OBTYPE
	AUTO_SET                      =620        # from enum OBTYPE
	AUTO_SPHERE                   =657        # from enum OBTYPE
	AUTO_SQUARE_SLOT              =651        # from enum OBTYPE
	AUTO_SURFACE_FEATURE          =641        # from enum OBTYPE
	AUTO_VECTOR_FEATURE           =640        # from enum OBTYPE
	BASIC_HIT                     =104        # from enum OBTYPE
	BASIC_SCAN_OBJECT             =214        # from enum OBTYPE
	BASIC_SCRIPT                  =12346      # from enum OBTYPE
	BF2D_ALIGN                    =13         # from enum OBTYPE
	BF3D_ALIGN                    =15         # from enum OBTYPE
	BFUSER_ALIGN                  =17         # from enum OBTYPE
	BUNDLE_ALIGN                  =123        # from enum OBTYPE
	CALIBRATEROTAB_COMMAND        =901        # from enum OBTYPE
	CALIB_ASSEMBLY                =142        # from enum OBTYPE
	CALIB_SPHERE                  =141        # from enum OBTYPE
	CALL_SUBROUTINE               =76         # from enum OBTYPE
	CASE_COMMAND                  =92         # from enum OBTYPE
	CHECK_DISTANCE                =102        # from enum OBTYPE
	CLAMP                         =99         # from enum OBTYPE
	CLEARANCE_PLANE               =130        # from enum OBTYPE
	CNC_PASS_THRU_COMMAND         =807        # from enum OBTYPE
	CNC_READ_VARIABLE             =806        # from enum OBTYPE
	CNC_SELECT_TABLE_COMMAND      =808        # from enum OBTYPE
	CNC_SET_PROTECTION_COMMAND    =803        # from enum OBTYPE
	CNC_UPDATE_TOOLOFSET          =804        # from enum OBTYPE
	CNC_UPDATE_WORKOFSET          =800        # from enum OBTYPE
	CNC_USE_WORKOFSET             =801        # from enum OBTYPE
	CNC_WRITE_VARIABLE            =805        # from enum OBTYPE
	COLUMN132_DISPLAY             =181        # from enum OBTYPE
	CONST_ALN_LINE                =548        # from enum OBTYPE
	CONST_ALN_PLANE               =576        # from enum OBTYPE
	CONST_BFRE_CIRCLE             =520        # from enum OBTYPE
	CONST_BFRE_CONE               =551        # from enum OBTYPE
	CONST_BFRE_CYLINDER           =560        # from enum OBTYPE
	CONST_BFRE_ELLIPSE            =580        # from enum OBTYPE
	CONST_BFRE_LINE               =540        # from enum OBTYPE
	CONST_BFRE_PLANE              =570        # from enum OBTYPE
	CONST_BFRE_SLOT               =507        # from enum OBTYPE
	CONST_BFRE_SPHERE             =530        # from enum OBTYPE
	CONST_BFRE_SQSLOT             =591        # from enum OBTYPE
	CONST_BF_CIRCLE               =521        # from enum OBTYPE
	CONST_BF_CONE                 =552        # from enum OBTYPE
	CONST_BF_CYLINDER             =561        # from enum OBTYPE
	CONST_BF_ELLIPSE              =581        # from enum OBTYPE
	CONST_BF_LINE                 =541        # from enum OBTYPE
	CONST_BF_PLANE                =571        # from enum OBTYPE
	CONST_BF_SLOT                 =506        # from enum OBTYPE
	CONST_BF_SPHERE               =531        # from enum OBTYPE
	CONST_BF_SQSLOT               =590        # from enum OBTYPE
	CONST_CAST_CIRCLE             =525        # from enum OBTYPE
	CONST_CAST_CONE               =555        # from enum OBTYPE
	CONST_CAST_CYLINDER           =564        # from enum OBTYPE
	CONST_CAST_ELLIPSE            =584        # from enum OBTYPE
	CONST_CAST_LINE               =545        # from enum OBTYPE
	CONST_CAST_PLANE              =574        # from enum OBTYPE
	CONST_CAST_POINT              =517        # from enum OBTYPE
	CONST_CAST_SLOT               =509        # from enum OBTYPE
	CONST_CAST_SPHERE             =534        # from enum OBTYPE
	CONST_CAST_SQSLOT             =593        # from enum OBTYPE
	CONST_CONE_CIRCLE             =524        # from enum OBTYPE
	CONST_CORNER_POINT            =518        # from enum OBTYPE
	CONST_CYLINDER_CIRCLE         =538        # from enum OBTYPE
	CONST_DROP_POINT              =514        # from enum OBTYPE
	CONST_HIPNT_PLANE             =579        # from enum OBTYPE
	CONST_INT_CIRCLE              =526        # from enum OBTYPE
	CONST_INT_ELLIPSE             =585        # from enum OBTYPE
	CONST_INT_LINE                =546        # from enum OBTYPE
	CONST_INT_POINT               =516        # from enum OBTYPE
	CONST_MID_LINE                =544        # from enum OBTYPE
	CONST_MID_PLANE               =573        # from enum OBTYPE
	CONST_MID_POINT               =513        # from enum OBTYPE
	CONST_MIN_CIRCLE_SCAN         =528        # from enum OBTYPE
	CONST_OFF_LINE                =547        # from enum OBTYPE
	CONST_OFF_PLANE               =575        # from enum OBTYPE
	CONST_OFF_POINT               =511        # from enum OBTYPE
	CONST_ORIG_POINT              =510        # from enum OBTYPE
	CONST_PIERCE_POINT            =515        # from enum OBTYPE
	CONST_PLTO_LINE               =550        # from enum OBTYPE
	CONST_PLTO_PLANE              =578        # from enum OBTYPE
	CONST_PRIMARY_DATUM           =579        # from enum OBTYPE
	CONST_PROJ_CIRCLE             =522        # from enum OBTYPE
	CONST_PROJ_CONE               =553        # from enum OBTYPE
	CONST_PROJ_CYLINDER           =562        # from enum OBTYPE
	CONST_PROJ_ELLIPSE            =582        # from enum OBTYPE
	CONST_PROJ_LINE               =542        # from enum OBTYPE
	CONST_PROJ_POINT              =512        # from enum OBTYPE
	CONST_PROJ_SLOT               =508        # from enum OBTYPE
	CONST_PROJ_SPHERE             =532        # from enum OBTYPE
	CONST_PROJ_SQSLOT             =592        # from enum OBTYPE
	CONST_PRTO_LINE               =549        # from enum OBTYPE
	CONST_PRTO_PLANE              =577        # from enum OBTYPE
	CONST_REV_CIRCLE              =523        # from enum OBTYPE
	CONST_REV_CONE                =554        # from enum OBTYPE
	CONST_REV_CYLINDER            =563        # from enum OBTYPE
	CONST_REV_ELLIPSE             =583        # from enum OBTYPE
	CONST_REV_LINE                =543        # from enum OBTYPE
	CONST_REV_PLANE               =572        # from enum OBTYPE
	CONST_REV_SPHERE              =533        # from enum OBTYPE
	CONST_ROUND_SLOT              =505        # from enum OBTYPE
	CONST_SCAN_SEG_ARC            =527        # from enum OBTYPE
	CONST_SCAN_SEG_LINE           =539        # from enum OBTYPE
	CONST_SECONDARY_DATUM_LINE    =557        # from enum OBTYPE
	CONST_SET                     =596        # from enum OBTYPE
	CONST_SPHERE_CIRCLE           =537        # from enum OBTYPE
	CONST_TANCIRCLES_CIRCLE       =536        # from enum OBTYPE
	CONST_TANGENT_PLANE           =579        # from enum OBTYPE
	CONST_TANLINES_CIRCLE         =529        # from enum OBTYPE
	CONST_TERTIARY_DATUM_POINT    =558        # from enum OBTYPE
	CONST_TRANSLATED_PLANE        =569        # from enum OBTYPE
	CONST_VECT_DIST_POINT         =519        # from enum OBTYPE
	CONST_WIDTH2D_FEATURE         =586        # from enum OBTYPE
	CONST_WIDTH3D_FEATURE         =587        # from enum OBTYPE
	CONTACT_ANGLE_POINT_FEATURE   =605        # from enum OBTYPE
	CONTACT_CIRCLE_FEATURE        =612        # from enum OBTYPE
	CONTACT_CONE_FEATURE          =615        # from enum OBTYPE
	CONTACT_CORNER_POINT_FEATURE  =606        # from enum OBTYPE
	CONTACT_CYLINDER_FEATURE      =616        # from enum OBTYPE
	CONTACT_EDGE_POINT_FEATURE    =604        # from enum OBTYPE
	CONTACT_ELLIPSE_FEATURE       =621        # from enum OBTYPE
	CONTACT_HIGH_POINT_FEATURE    =607        # from enum OBTYPE
	CONTACT_LINE_FEATURE          =614        # from enum OBTYPE
	CONTACT_PLANE_FEATURE         =617        # from enum OBTYPE
	CONTACT_POLYGON_FEATURE       =627        # from enum OBTYPE
	CONTACT_SLOT_NOTCH_FEATURE    =622        # from enum OBTYPE
	CONTACT_SLOT_ROUND_FEATURE    =618        # from enum OBTYPE
	CONTACT_SLOT_SQUARE_FEATURE   =619        # from enum OBTYPE
	CONTACT_SPHERE_FEATURE        =613        # from enum OBTYPE
	CONTACT_SURFACE_POINT_FEATURE =603        # from enum OBTYPE
	CONTACT_VECTOR_POINT_FEATURE  =602        # from enum OBTYPE
	CORNER_HIT                    =106        # from enum OBTYPE
	CURVE_FEATURE                 =38         # from enum OBTYPE
	DATDEF_COMMAND                =1299       # from enum OBTYPE
	DCCSCAN_OBJECT                =211        # from enum OBTYPE
	DEFAULT_CASE_COMMAND          =94         # from enum OBTYPE
	DIMENSION_2D_ANGLE            =1109       # from enum OBTYPE
	DIMENSION_2D_DISTANCE         =1107       # from enum OBTYPE
	DIMENSION_3D_ANGLE            =1108       # from enum OBTYPE
	DIMENSION_3D_DISTANCE         =1106       # from enum OBTYPE
	DIMENSION_ANGULARITY          =1112       # from enum OBTYPE
	DIMENSION_A_LOCATION          =1007       # from enum OBTYPE
	DIMENSION_CIRCULARITY         =1101       # from enum OBTYPE
	DIMENSION_CIRCULAR_RUNOUT     =1117       # from enum OBTYPE
	DIMENSION_COAXIALITY          =1114       # from enum OBTYPE
	DIMENSION_CONCENTRICITY       =1111       # from enum OBTYPE
	DIMENSION_CYLINDRICITY        =1116       # from enum OBTYPE
	DIMENSION_D_LOCATION          =1005       # from enum OBTYPE
	DIMENSION_END_LOCATION        =1001       # from enum OBTYPE
	DIMENSION_FLATNESS            =1102       # from enum OBTYPE
	DIMENSION_FLATNESS_LOCATION   =1018       # from enum OBTYPE
	DIMENSION_FORMAT              =180        # from enum OBTYPE
	DIMENSION_H_LOCATION          =1017       # from enum OBTYPE
	DIMENSION_INFORMATION         =182        # from enum OBTYPE
	DIMENSION_KEYIN               =1113       # from enum OBTYPE
	DIMENSION_L_LOCATION          =1012       # from enum OBTYPE
	DIMENSION_PARALLELISM         =1104       # from enum OBTYPE
	DIMENSION_PA_LOCATION         =1010       # from enum OBTYPE
	DIMENSION_PD_LOCATION         =1013       # from enum OBTYPE
	DIMENSION_PERPENDICULARITY    =1103       # from enum OBTYPE
	DIMENSION_PROFILE             =1105       # from enum OBTYPE
	DIMENSION_PROFILE_LINE        =1118       # from enum OBTYPE
	DIMENSION_PROFILE_SURFACE     =1105       # from enum OBTYPE
	DIMENSION_PR_LOCATION         =1009       # from enum OBTYPE
	DIMENSION_ROUNDNESS           =1101       # from enum OBTYPE
	DIMENSION_ROUNDNESS_LOCATION  =1019       # from enum OBTYPE
	DIMENSION_RS_LOCATION         =1016       # from enum OBTYPE
	DIMENSION_RT_LOCATION         =1014       # from enum OBTYPE
	DIMENSION_RUNOUT              =1110       # from enum OBTYPE
	DIMENSION_R_LOCATION          =1006       # from enum OBTYPE
	DIMENSION_START_LOCATION      =1000       # from enum OBTYPE
	DIMENSION_STRAIGHTNESS        =1100       # from enum OBTYPE
	DIMENSION_STRAIGHTNESS_LOCATION=1020       # from enum OBTYPE
	DIMENSION_SYMMETRY            =1115       # from enum OBTYPE
	DIMENSION_S_LOCATION          =1015       # from enum OBTYPE
	DIMENSION_TOTAL_RUNOUT        =1110       # from enum OBTYPE
	DIMENSION_TRUE_D1_LOCATION    =1214       # from enum OBTYPE
	DIMENSION_TRUE_D2_LOCATION    =1215       # from enum OBTYPE
	DIMENSION_TRUE_D3_LOCATION    =1216       # from enum OBTYPE
	DIMENSION_TRUE_DD_LOCATION    =1205       # from enum OBTYPE
	DIMENSION_TRUE_DF_LOCATION    =1206       # from enum OBTYPE
	DIMENSION_TRUE_DIAM_LOCATION  =1209       # from enum OBTYPE
	DIMENSION_TRUE_END_POSITION   =1201       # from enum OBTYPE
	DIMENSION_TRUE_FLATNESS_LOCATION=1217       # from enum OBTYPE
	DIMENSION_TRUE_LD_LOCATION    =1210       # from enum OBTYPE
	DIMENSION_TRUE_LF_LOCATION    =1212       # from enum OBTYPE
	DIMENSION_TRUE_LOCATION       =1220       # from enum OBTYPE
	DIMENSION_TRUE_PA_LOCATION    =1208       # from enum OBTYPE
	DIMENSION_TRUE_PR_LOCATION    =1207       # from enum OBTYPE
	DIMENSION_TRUE_ROUNDNESS_LOCATION=1218       # from enum OBTYPE
	DIMENSION_TRUE_START_POSITION =1200       # from enum OBTYPE
	DIMENSION_TRUE_STRAIGHTNESS_LOCATION=1219       # from enum OBTYPE
	DIMENSION_TRUE_WD_LOCATION    =1211       # from enum OBTYPE
	DIMENSION_TRUE_WF_LOCATION    =1213       # from enum OBTYPE
	DIMENSION_TRUE_X_LOCATION     =1202       # from enum OBTYPE
	DIMENSION_TRUE_Y_LOCATION     =1203       # from enum OBTYPE
	DIMENSION_TRUE_Z_LOCATION     =1204       # from enum OBTYPE
	DIMENSION_T_LOCATION          =1008       # from enum OBTYPE
	DIMENSION_V_LOCATION          =1011       # from enum OBTYPE
	DIMENSION_X_LOCATION          =1002       # from enum OBTYPE
	DIMENSION_Y_LOCATION          =1003       # from enum OBTYPE
	DIMENSION_Z_LOCATION          =1004       # from enum OBTYPE
	DISPLAYPRECISION              =114        # from enum OBTYPE
	DISPLAY_METAFILE              =702        # from enum OBTYPE
	DO_COMMAND                    =81         # from enum OBTYPE
	EDGE_HIT                      =109        # from enum OBTYPE
	ELSE_COMMAND                  =91         # from enum OBTYPE
	ELSE_IF_COMMAND               =90         # from enum OBTYPE
	ENDWHILE_COMMAND              =80         # from enum OBTYPE
	END_ALIGN                     =19         # from enum OBTYPE
	END_CASE_COMMAND              =85         # from enum OBTYPE
	END_DEFAULT_CASE_COMMAND      =87         # from enum OBTYPE
	END_ELSE_COMMAND              =84         # from enum OBTYPE
	END_ELSE_IF_COMMAND           =83         # from enum OBTYPE
	END_HYPER_FORM                =12351      # from enum OBTYPE
	END_HYPER_REPORT              =12349      # from enum OBTYPE
	END_IF_COMMAND                =82         # from enum OBTYPE
	END_MEASURED_FEATURE          =213        # from enum OBTYPE
	END_MOVE_SWEEP                =159        # from enum OBTYPE
	END_PROGRAM                   =169        # from enum OBTYPE
	END_READ_TEMPERATURE          =409        # from enum OBTYPE
	END_SCRIPT                    =12347      # from enum OBTYPE
	END_SELECT_COMMAND            =86         # from enum OBTYPE
	END_SUBROUTINE                =77         # from enum OBTYPE
	EQUATE_ALIGN                  =11         # from enum OBTYPE
	EW_GROUP_END                  =753        # from enum OBTYPE
	EW_GROUP_START                =752        # from enum OBTYPE
	EXTERNAL_COMMAND              =175        # from enum OBTYPE
	FASTPROBEMODE_COMMAND         =902        # from enum OBTYPE
	FEATURE_CONTROL_FRAME         =184        # from enum OBTYPE
	FILE_IO_OBJECT                =96         # from enum OBTYPE
	FILTER_SET                    =598        # from enum OBTYPE
	FLY_MODE                      =168        # from enum OBTYPE
	GAP_ONLY                      =193        # from enum OBTYPE
	GENERIC_CONSTRUCTION          =597        # from enum OBTYPE
	GET_PROBECHANGER_DATA         =262        # from enum OBTYPE
	GET_PROBE_DATA                =61         # from enum OBTYPE
	GOTO_COMMAND                  =73         # from enum OBTYPE
	HYPER_CUSTOM                  =12352      # from enum OBTYPE
	HYPER_FORM                    =12350      # from enum OBTYPE
	HYPER_LABEL                   =12356      # from enum OBTYPE
	HYPER_LEGACY                  =12348      # from enum OBTYPE
	HYPER_REPORT                  =12355      # from enum OBTYPE
	HYPER_TEMPLATE                =12353      # from enum OBTYPE
	IF_BLOCK_COMMAND              =89         # from enum OBTYPE
	IF_GOTO_COMMAND               =74         # from enum OBTYPE
	IGNOREMOTIONERRORS            =119        # from enum OBTYPE
	IGNOREROTAB_COMMAND           =900        # from enum OBTYPE
	INBETWEEN_TOL                 =1301       # from enum OBTYPE
	IOCHANNELCOMMAND              =120        # from enum OBTYPE
	ISO_SIZE_COMMAND              =1320       # from enum OBTYPE
	ISO_TOLERANCE_COMMAND         =1303       # from enum OBTYPE
	ITER_ALIGN                    =12         # from enum OBTYPE
	LABEL_CMD                     =72         # from enum OBTYPE
	LASER_CIRCLE_FEATURE          =270        # from enum OBTYPE
	LASER_CONE_FEATURE            =281        # from enum OBTYPE
	LASER_CYLINDER_FEATURE        =279        # from enum OBTYPE
	LASER_EDGE_POINT_FEATURE      =276        # from enum OBTYPE
	LASER_FLUSH_AND_GAP_FEATURE   =274        # from enum OBTYPE
	LASER_LINE_FEATURE            =277        # from enum OBTYPE
	LASER_PLANE_FEATURE           =272        # from enum OBTYPE
	LASER_POLYGON_FEATURE         =280        # from enum OBTYPE
	LASER_SLOT_FEATURE            =273        # from enum OBTYPE
	LASER_SLOT_SQUARE_FEATURE     =278        # from enum OBTYPE
	LASER_SPHERE_FEATURE          =275        # from enum OBTYPE
	LASER_SURFACE_POINT_FEATURE   =271        # from enum OBTYPE
	LEAPFROG                      =115        # from enum OBTYPE
	LEVEL_ALIGN                   =2          # from enum OBTYPE
	LOAD_COLUMN                   =173        # from enum OBTYPE
	LOAD_FIXTURE                  =172        # from enum OBTYPE
	LOAD_MACHINE                  =171        # from enum OBTYPE
	LOOP_END                      =71         # from enum OBTYPE
	LOOP_START                    =70         # from enum OBTYPE
	MANRETRACT                    =117        # from enum OBTYPE
	MANSCAN_OBJECT                =212        # from enum OBTYPE
	MAN_DCC_MODE                  =103        # from enum OBTYPE
	MEASURED_CIRCLE               =202        # from enum OBTYPE
	MEASURED_CONE                 =205        # from enum OBTYPE
	MEASURED_CYLINDER             =206        # from enum OBTYPE
	MEASURED_LINE                 =204        # from enum OBTYPE
	MEASURED_PLANE                =207        # from enum OBTYPE
	MEASURED_POINT                =201        # from enum OBTYPE
	MEASURED_ROUND_SLOT           =208        # from enum OBTYPE
	MEASURED_SET                  =210        # from enum OBTYPE
	MEASURED_SPHERE               =203        # from enum OBTYPE
	MEASURED_SQUARE_SLOT          =209        # from enum OBTYPE
	MEASURED_TORUS                =200        # from enum OBTYPE
	MESH_ALIGN                    =18         # from enum OBTYPE
	MESH_OPER_COLORMAP            =2024       # from enum OBTYPE
	MESH_OPER_EMPTY               =2025       # from enum OBTYPE
	MESH_OPER_FILEEXPORT          =2023       # from enum OBTYPE
	MESH_OPER_FILEIMPORT          =2022       # from enum OBTYPE
	MOVE_ALL                      =162        # from enum OBTYPE
	MOVE_CIRCULAR                 =155        # from enum OBTYPE
	MOVE_CLEARP                   =151        # from enum OBTYPE
	MOVE_CLEARPOINT               =163        # from enum OBTYPE
	MOVE_EXCLUSIVE                =161        # from enum OBTYPE
	MOVE_INCREMENT                =154        # from enum OBTYPE
	MOVE_PH9_OFFSET               =156        # from enum OBTYPE
	MOVE_POINT                    =150        # from enum OBTYPE
	MOVE_ROTAB                    =153        # from enum OBTYPE
	MOVE_SPEED                    =45         # from enum OBTYPE
	MOVE_SWEEP_POINT              =160        # from enum OBTYPE
	MOVE_SYNC                     =157        # from enum OBTYPE
	ONERROR                       =78         # from enum OBTYPE
	OPTIONMOTION                  =112        # from enum OBTYPE
	OPTIONPROBE                   =111        # from enum OBTYPE
	PART_TEMPERATURE              =408        # from enum OBTYPE
	PLANNER_ANGLE_POINT_FEATURE   =2110       # from enum OBTYPE
	PLANNER_CIRCLE_FEATURE        =2102       # from enum OBTYPE
	PLANNER_CONE_FEATURE          =2108       # from enum OBTYPE
	PLANNER_CORNER_POINT_FEATURE  =2111       # from enum OBTYPE
	PLANNER_CYLINDER_FEATURE      =2107       # from enum OBTYPE
	PLANNER_EDGE_POINT_FEATURE    =2101       # from enum OBTYPE
	PLANNER_ELLIPSE_FEATURE       =2112       # from enum OBTYPE
	PLANNER_LINE_FEATURE          =2103       # from enum OBTYPE
	PLANNER_PLANE_FEATURE         =2104       # from enum OBTYPE
	PLANNER_POLYGON_FEATURE       =2113       # from enum OBTYPE
	PLANNER_SLOT_NOTCH_FEATURE    =2114       # from enum OBTYPE
	PLANNER_SLOT_ROUND_FEATURE    =2105       # from enum OBTYPE
	PLANNER_SLOT_SQUARE_FEATURE   =2106       # from enum OBTYPE
	PLANNER_SPHERE_FEATURE        =2109       # from enum OBTYPE
	PLANNER_VECTOR_POINT_FEATURE  =2100       # from enum OBTYPE
	POINTCLOUD                    =2001       # from enum OBTYPE
	POINTCLOUD_ALIGN              =16         # from enum OBTYPE
	POINTCLOUD_MESH               =2004       # from enum OBTYPE
	POINTCLOUD_OPER               =2002       # from enum OBTYPE
	POINTCLOUD_OPER_BOOLEAN       =2016       # from enum OBTYPE
	POINTCLOUD_OPER_CLEAN         =2012       # from enum OBTYPE
	POINTCLOUD_OPER_COLORMAPFACE  =2019       # from enum OBTYPE
	POINTCLOUD_OPER_COLORMAPPNT   =2020       # from enum OBTYPE
	POINTCLOUD_OPER_CROSSSECTION  =2021       # from enum OBTYPE
	POINTCLOUD_OPER_EMPTY         =2013       # from enum OBTYPE
	POINTCLOUD_OPER_FILEEXPORT    =2011       # from enum OBTYPE
	POINTCLOUD_OPER_FILEIMPORT    =2010       # from enum OBTYPE
	POINTCLOUD_OPER_FILTER        =2017       # from enum OBTYPE
	POINTCLOUD_OPER_NEW           =2003       # from enum OBTYPE
	POINTCLOUD_OPER_OLD           =2009       # from enum OBTYPE
	POINTCLOUD_OPER_PURGE         =2015       # from enum OBTYPE
	POINTCLOUD_OPER_RESET         =2014       # from enum OBTYPE
	POINTCLOUD_OPER_SELECTION     =2018       # from enum OBTYPE
	POINT_INFO                    =183        # from enum OBTYPE
	POLARVECTORCOMP               =113        # from enum OBTYPE
	POSITIVE_REPORTING            =196        # from enum OBTYPE
	PREHIT_DISTANCE               =100        # from enum OBTYPE
	PRINT_FORM_FEED               =750        # from enum OBTYPE
	PRINT_REPORT                  =751        # from enum OBTYPE
	PROBE_COMPENSATION            =140        # from enum OBTYPE
	READ_POINT                    =192        # from enum OBTYPE
	READ_TEMPERATURE              =404        # from enum OBTYPE
	RECALL_ALIGN                  =10         # from enum OBTYPE
	RECALL_VIEWSET                =51         # from enum OBTYPE
	RETRACT_DISTANCE              =101        # from enum OBTYPE
	RETROLINEAR_ONLY              =194        # from enum OBTYPE
	RMEAS_MODE                    =110        # from enum OBTYPE
	ROTATEOFF_ALIGN               =6          # from enum OBTYPE
	ROTATE_ALIGN                  =3          # from enum OBTYPE
	ROTATE_CIRCLE_ALIGN           =14         # from enum OBTYPE
	SAVE_ALIGN                    =9          # from enum OBTYPE
	SCAN_SPEED                    =47         # from enum OBTYPE
	SELECT_COMMAND                =93         # from enum OBTYPE
	SET_ACTIVE_TIP                =60         # from enum OBTYPE
	SET_COMMENT                   =170        # from enum OBTYPE
	SET_WORKPLANE                 =21         # from enum OBTYPE
	SIMULTANEOUS_EVALUATION       =1300       # from enum OBTYPE
	SNAPSHOT_COMMAND              =905        # from enum OBTYPE
	SPC_CHART                     =780        # from enum OBTYPE
	START_ALIGN                   =1          # from enum OBTYPE
	START_MOVE_SWEEP              =158        # from enum OBTYPE
	START_SUBROUTINE              =75         # from enum OBTYPE
	STATISTICS                    =190        # from enum OBTYPE
	STRAIGHTNESS_COMMAND          =1310       # from enum OBTYPE
	SURFACE_FEATURE               =39         # from enum OBTYPE
	SURFACE_HIT                   =108        # from enum OBTYPE
	TABLE_FORMAT                  =179        # from enum OBTYPE
	TEMP_COMP                     =62         # from enum OBTYPE
	TEMP_COMP_ORIGIN              =63         # from enum OBTYPE
	THICKNESS_GAGE                =2119       # from enum OBTYPE
	THICKNESS_SCAN                =2120       # from enum OBTYPE
	TOUCH_SPEED                   =46         # from enum OBTYPE
	TPS_CUSTOM_COMMAND            =402        # from enum OBTYPE
	TRACEFIELD                    =191        # from enum OBTYPE
	TRACKER_CUSTOM_COMMAND        =401        # from enum OBTYPE
	TRACKER_LEVEL_TO_GRAVITY      =233        # from enum OBTYPE
	TRANSOFF_ALIGN                =5          # from enum OBTYPE
	TRANS_ALIGN                   =4          # from enum OBTYPE
	TRIGGER_PLANE_COMMAND         =232        # from enum OBTYPE
	TRIGGER_TOLERANCE             =231        # from enum OBTYPE
	UNTIL_COMMAND                 =88         # from enum OBTYPE
	VECTOR_HIT                    =105        # from enum OBTYPE
	VIDEOSETUP                    =118        # from enum OBTYPE
	VIEWSET                       =50         # from enum OBTYPE
	VISION_ANGLE_POINT_FEATURE    =249        # from enum OBTYPE
	VISION_CIRCLE_FEATURE         =245        # from enum OBTYPE
	VISION_EDGE_POINT_FEATURE     =242        # from enum OBTYPE
	VISION_ELLIPSE_FEATURE        =244        # from enum OBTYPE
	VISION_IMAGE_CAPTURE          =253        # from enum OBTYPE
	VISION_LINE_FEATURE           =243        # from enum OBTYPE
	VISION_POLYGON_FEATURE        =251        # from enum OBTYPE
	VISION_PROFILE_2D_FEATURE     =247        # from enum OBTYPE
	VISION_SLOT_NOTCH_FEATURE     =250        # from enum OBTYPE
	VISION_SLOT_ROUND_FEATURE     =246        # from enum OBTYPE
	VISION_SLOT_SQUARE_FEATURE    =248        # from enum OBTYPE
	VISION_SURFACE_POINT_FEATURE  =241        # from enum OBTYPE
	WHILE_COMMAND                 =79         # from enum OBTYPE
	WRIST_SPEED                   =49         # from enum OBTYPE
	XML_STATISTICS                =189        # from enum OBTYPE
	X_TEMPERATURE                 =405        # from enum OBTYPE
	Y_TEMPERATURE                 =406        # from enum OBTYPE
	Z_TEMPERATURE                 =407        # from enum OBTYPE
	PCD_XAXIS                     =1          # from enum PAXISTYPE
	PCD_YAXIS                     =2          # from enum PAXISTYPE
	PCD_ZAXIS                     =0          # from enum PAXISTYPE
	PCD_BAUD_110                  =1          # from enum PCDBAUD
	PCD_BAUD_1200                 =4          # from enum PCDBAUD
	PCD_BAUD_128000               =12         # from enum PCDBAUD
	PCD_BAUD_14400                =8          # from enum PCDBAUD
	PCD_BAUD_19200                =9          # from enum PCDBAUD
	PCD_BAUD_2400                 =5          # from enum PCDBAUD
	PCD_BAUD_256000               =13         # from enum PCDBAUD
	PCD_BAUD_300                  =2          # from enum PCDBAUD
	PCD_BAUD_38400                =10         # from enum PCDBAUD
	PCD_BAUD_4800                 =6          # from enum PCDBAUD
	PCD_BAUD_56000                =11         # from enum PCDBAUD
	PCD_BAUD_600                  =3          # from enum PCDBAUD
	PCD_BAUD_9600                 =7          # from enum PCDBAUD
	PCD_INPUT                     =2          # from enum PCDCOMMENT
	PCD_OPERATOR                  =0          # from enum PCDCOMMENT
	PCD_REPORT                    =1          # from enum PCDCOMMENT
	PCD_DATA7                     =20         # from enum PCDDATABITS
	PCD_DATA8                     =19         # from enum PCDDATABITS
	DIM__2D_ANGLE                 =1109       # from enum PCDDIMTYPES
	DIM__2D_DISTANCE              =1107       # from enum PCDDIMTYPES
	DIM__3D_ANGLE                 =1108       # from enum PCDDIMTYPES
	DIM__3D_DISTANCE              =1106       # from enum PCDDIMTYPES
	DIM__ANGULARITY               =1112       # from enum PCDDIMTYPES
	DIM__CONCENTRICITY            =1111       # from enum PCDDIMTYPES
	DIM__FLATNESS                 =1102       # from enum PCDDIMTYPES
	DIM__KEYIN                    =1113       # from enum PCDDIMTYPES
	DIM__LOCATION                 =1000       # from enum PCDDIMTYPES
	DIM__PARALLELISM              =1104       # from enum PCDDIMTYPES
	DIM__PERPENDICULARITY         =1103       # from enum PCDDIMTYPES
	DIM__PROFILE                  =1105       # from enum PCDDIMTYPES
	DIM__ROUNDNESS                =1101       # from enum PCDDIMTYPES
	DIM__RUNOUT                   =1110       # from enum PCDDIMTYPES
	DIM__STRAIGHTNESS             =1100       # from enum PCDDIMTYPES
	DIM__TRUE_POSITION            =1200       # from enum PCDDIMTYPES
	PCD_3DPDF                     =3          # from enum PCDFILEPRINTFORMAT
	PCD_PDF                       =1          # from enum PCDFILEPRINTFORMAT
	PCD_RTF                       =0          # from enum PCDFILEPRINTFORMAT
	PCD_TXT                       =2          # from enum PCDFILEPRINTFORMAT
	PCD_VECTOR                    =608        # from enum PCDGETPOINTSTYPES
	PCD__BALLCENTER               =604        # from enum PCDGETPOINTSTYPES
	PCD__CENTROID                 =603        # from enum PCDGETPOINTSTYPES
	PCD_DTRDSR                    =24         # from enum PCDHANDSHAKE
	PCD_RTSCTS                    =25         # from enum PCDHANDSHAKE
	PCD_XONXOFF                   =26         # from enum PCDHANDSHAKE
	PCD_THEO                      =2          # from enum PCDMEASTHEO
	PCD__MEAS                     =3          # from enum PCDMEASTHEO
	PCD_OFF                       =0          # from enum PCDONOFF
	PCD_ON                        =-1         # from enum PCDONOFF
	PCD_EVENPARITY                =15         # from enum PCDPARITY
	PCD_MARKPARITY                =17         # from enum PCDPARITY
	PCD_NOPARITY                  =14         # from enum PCDPARITY
	PCD_ODDPARITY                 =16         # from enum PCDPARITY
	PCD_SPACEPARITY               =18         # from enum PCDPARITY
	PCD_APPEND                    =1          # from enum PCDPRINTFILEMODE
	PCD_AUTO                      =4          # from enum PCDPRINTFILEMODE
	PCD_NEWFILE                   =2          # from enum PCDPRINTFILEMODE
	PCD_OVERWRITE                 =3          # from enum PCDPRINTFILEMODE
	PCD_PROMPT                    =5          # from enum PCDPRINTFILEMODE
	PCD_FILE                      =2          # from enum PCDPRINTLOC
	PCD_PRINTER                   =1          # from enum PCDPRINTLOC
	PCD___OFF                     =0          # from enum PCDPRINTLOC
	PCD_ALIGNMENTS                =2          # from enum PCDREPORTSETTINGS
	PCD_COMMENTS                  =8          # from enum PCDREPORTSETTINGS
	PCD_DIMENSIONS                =16         # from enum PCDREPORTSETTINGS
	PCD_FEATURES                  =1          # from enum PCDREPORTSETTINGS
	PCD_HITS                      =32         # from enum PCDREPORTSETTINGS
	PCD_MOVES                     =4          # from enum PCDREPORTSETTINGS
	PCD_OUTTOL_ONLY               =64         # from enum PCDREPORTSETTINGS
	PCD_BODY                      =7          # from enum PCDSCANDIR1
	PCD_LINE                      =203        # from enum PCDSCANDIR1
	PCD_VARIABLE                  =8          # from enum PCDSCANDIR1
	PCD__BODY                     =7          # from enum PCDSCANDIR2
	PCD__LINE                     =203        # from enum PCDSCANDIR2
	PCD_EXTERIOR                  =0          # from enum PCDSCANHITFLAG
	PCD_INTERIOR                  =8          # from enum PCDSCANHITFLAG
	PCD_ANGLEHIT                  =20         # from enum PCDSCANHITTYPE
	PCD_EDGEHIT                   =19         # from enum PCDSCANHITTYPE
	PCD_SURFACEHIT                =18         # from enum PCDSCANHITTYPE
	PCD_VECTORHIT                 =17         # from enum PCDSCANHITTYPE
	PCD_CUTAXIS                   =12         # from enum PCDSCANTECHNIQUE
	PCD_FIXED_DELTA               =9          # from enum PCDSCANTECHNIQUE
	PCD_TIME_DELTA                =11         # from enum PCDSCANTECHNIQUE
	PCD_VARIABLE_DELTA            =10         # from enum PCDSCANTECHNIQUE
	PCD_CUTVECTOR                 =13         # from enum PCDSCANVECTOR
	PCD_INITDIR                   =15         # from enum PCDSCANVECTOR
	PCD_INITTOUCH                 =14         # from enum PCDSCANVECTOR
	PCD_ROWEND_APPROACH           =16         # from enum PCDSCANVECTOR
	PCD_BOUNDARY_PLANE            =23         # from enum PCDSCANVECTORSURF
	PCD_SIDE_SURFACE              =22         # from enum PCDSCANVECTORSURF
	PCD_TOP_SURFACE               =21         # from enum PCDSCANVECTORSURF
	PCD_ADD_RADIUS                =2          # from enum PCDSTARTDIMFLAGS
	PCD_LMC_LMC                   =4096       # from enum PCDSTARTDIMFLAGS
	PCD_LMC_MMC                   =1024       # from enum PCDSTARTDIMFLAGS
	PCD_LMC_RFS                   =512        # from enum PCDSTARTDIMFLAGS
	PCD_MMC_LMC                   =256        # from enum PCDSTARTDIMFLAGS
	PCD_MMC_MMC                   =128        # from enum PCDSTARTDIMFLAGS
	PCD_MMC_RFS                   =64         # from enum PCDSTARTDIMFLAGS
	PCD_NO_RADIUS                 =0          # from enum PCDSTARTDIMFLAGS
	PCD_PAR_TO                    =16384      # from enum PCDSTARTDIMFLAGS
	PCD_PERP_TO                   =8192       # from enum PCDSTARTDIMFLAGS
	PCD_RECALC_NOMS               =65536      # from enum PCDSTARTDIMFLAGS
	PCD_RFS_LMC                   =32         # from enum PCDSTARTDIMFLAGS
	PCD_RFS_MMC                   =16         # from enum PCDSTARTDIMFLAGS
	PCD_RFS_RFS                   =8          # from enum PCDSTARTDIMFLAGS
	PCD_SUB_RADIUS                =4          # from enum PCDSTARTDIMFLAGS
	PCD_ANGLE                     =256        # from enum PCDSTARTFEATFLAGS
	PCD_AUTOMOVE                  =131072     # from enum PCDSTARTFEATFLAGS
	PCD_BND                       =512        # from enum PCDSTARTFEATFLAGS
	PCD_FINDHOLE                  =262144     # from enum PCDSTARTFEATFLAGS
	PCD_HEM                       =4096       # from enum PCDSTARTFEATFLAGS
	PCD_IN                        =128        # from enum PCDSTARTFEATFLAGS
	PCD_LENGTH                    =0          # from enum PCDSTARTFEATFLAGS
	PCD_LINE_3D                   =32768      # from enum PCDSTARTFEATFLAGS
	PCD_MEASURE_BOTH              =2048       # from enum PCDSTARTFEATFLAGS
	PCD_MEASURE_EDGE              =1024       # from enum PCDSTARTFEATFLAGS
	PCD_MEASURE_SURFACE           =0          # from enum PCDSTARTFEATFLAGS
	PCD_MEASURE_WIDTH             =524288     # from enum PCDSTARTFEATFLAGS
	PCD_NORM                      =0          # from enum PCDSTARTFEATFLAGS
	PCD_OUT                       =0          # from enum PCDSTARTFEATFLAGS
	PCD_PIN                       =8192       # from enum PCDSTARTFEATFLAGS
	PCD_POLR                      =64         # from enum PCDSTARTFEATFLAGS
	PCD_READPOS                   =16384      # from enum PCDSTARTFEATFLAGS
	PCD_RECT                      =0          # from enum PCDSTARTFEATFLAGS
	PCD_TRIM                      =0          # from enum PCDSTARTFEATFLAGS
	PCD_UNBND                     =0          # from enum PCDSTARTFEATFLAGS
	PCD__BACK                     =5          # from enum PCDSTARTFEATFLAGS
	PCD__BOTTOM                   =1          # from enum PCDSTARTFEATFLAGS
	PCD__EXTERIOR                 =0          # from enum PCDSTARTFEATFLAGS
	PCD__FRONT                    =4          # from enum PCDSTARTFEATFLAGS
	PCD__INTERIOR                 =8          # from enum PCDSTARTFEATFLAGS
	PCD__LEFT                     =2          # from enum PCDSTARTFEATFLAGS
	PCD__RECALC_NOMS              =65536      # from enum PCDSTARTFEATFLAGS
	PCD__RIGHT                    =3          # from enum PCDSTARTFEATFLAGS
	PCD__TOP                      =0          # from enum PCDSTARTFEATFLAGS
	PCD__XAXIS                    =2          # from enum PCDSTARTFEATFLAGS
	PCD__XMINUS                   =3          # from enum PCDSTARTFEATFLAGS
	PCD__XPLUS                    =2          # from enum PCDSTARTFEATFLAGS
	PCD__YAXIS                    =4          # from enum PCDSTARTFEATFLAGS
	PCD__YMINUS                   =5          # from enum PCDSTARTFEATFLAGS
	PCD__YPLUS                    =4          # from enum PCDSTARTFEATFLAGS
	PCD__ZAXIS                    =0          # from enum PCDSTARTFEATFLAGS
	PCD__ZMINUS                   =1          # from enum PCDSTARTFEATFLAGS
	PCD__ZPLUS                    =0          # from enum PCDSTARTFEATFLAGS
	AUTO__ANGLE_HIT               =605        # from enum PCDSTARTFEATTYPES
	AUTO__CIRCLE                  =612        # from enum PCDSTARTFEATTYPES
	AUTO__CORNER_HIT              =606        # from enum PCDSTARTFEATTYPES
	AUTO__CYLINDER                =616        # from enum PCDSTARTFEATTYPES
	AUTO__EDGE_HIT                =604        # from enum PCDSTARTFEATTYPES
	AUTO__ELLIPSE                 =621        # from enum PCDSTARTFEATTYPES
	AUTO__ROUND_SLOT              =618        # from enum PCDSTARTFEATTYPES
	AUTO__SPHERE                  =613        # from enum PCDSTARTFEATTYPES
	AUTO__SQUARE_SLOT             =619        # from enum PCDSTARTFEATTYPES
	AUTO__SURFACE_HIT             =603        # from enum PCDSTARTFEATTYPES
	AUTO__VECTOR_HIT              =602        # from enum PCDSTARTFEATTYPES
	CONST__ALN_LINE               =548        # from enum PCDSTARTFEATTYPES
	CONST__ALN_PLANE              =576        # from enum PCDSTARTFEATTYPES
	CONST__BFRE_CIRCLE            =520        # from enum PCDSTARTFEATTYPES
	CONST__BFRE_CONE              =551        # from enum PCDSTARTFEATTYPES
	CONST__BFRE_CYLINDER          =560        # from enum PCDSTARTFEATTYPES
	CONST__BFRE_LINE              =540        # from enum PCDSTARTFEATTYPES
	CONST__BFRE_PLANE             =570        # from enum PCDSTARTFEATTYPES
	CONST__BFRE_SPHERE            =530        # from enum PCDSTARTFEATTYPES
	CONST__BF_CIRCLE              =521        # from enum PCDSTARTFEATTYPES
	CONST__BF_CONE                =552        # from enum PCDSTARTFEATTYPES
	CONST__BF_CYLINDER            =561        # from enum PCDSTARTFEATTYPES
	CONST__BF_LINE                =541        # from enum PCDSTARTFEATTYPES
	CONST__BF_PLANE               =571        # from enum PCDSTARTFEATTYPES
	CONST__BF_SPHERE              =531        # from enum PCDSTARTFEATTYPES
	CONST__CAST_CIRCLE            =525        # from enum PCDSTARTFEATTYPES
	CONST__CAST_CONE              =555        # from enum PCDSTARTFEATTYPES
	CONST__CAST_CYLINDER          =564        # from enum PCDSTARTFEATTYPES
	CONST__CAST_LINE              =545        # from enum PCDSTARTFEATTYPES
	CONST__CAST_PLANE             =574        # from enum PCDSTARTFEATTYPES
	CONST__CAST_POINT             =517        # from enum PCDSTARTFEATTYPES
	CONST__CAST_SPHERE            =534        # from enum PCDSTARTFEATTYPES
	CONST__CONE_CIRCLE            =524        # from enum PCDSTARTFEATTYPES
	CONST__CORNER_POINT           =518        # from enum PCDSTARTFEATTYPES
	CONST__DROP_POINT             =514        # from enum PCDSTARTFEATTYPES
	CONST__HIPNT_PLANE            =579        # from enum PCDSTARTFEATTYPES
	CONST__INT_CIRCLE             =526        # from enum PCDSTARTFEATTYPES
	CONST__INT_LINE               =546        # from enum PCDSTARTFEATTYPES
	CONST__INT_POINT              =516        # from enum PCDSTARTFEATTYPES
	CONST__MID_LINE               =544        # from enum PCDSTARTFEATTYPES
	CONST__MID_PLANE              =573        # from enum PCDSTARTFEATTYPES
	CONST__MID_POINT              =513        # from enum PCDSTARTFEATTYPES
	CONST__OFF_LINE               =547        # from enum PCDSTARTFEATTYPES
	CONST__OFF_PLANE              =575        # from enum PCDSTARTFEATTYPES
	CONST__OFF_POINT              =511        # from enum PCDSTARTFEATTYPES
	CONST__ORIG_POINT             =510        # from enum PCDSTARTFEATTYPES
	CONST__PIERCE_POINT           =515        # from enum PCDSTARTFEATTYPES
	CONST__PLTO_LINE              =550        # from enum PCDSTARTFEATTYPES
	CONST__PLTO_PLANE             =578        # from enum PCDSTARTFEATTYPES
	CONST__PROJ_CIRCLE            =522        # from enum PCDSTARTFEATTYPES
	CONST__PROJ_CONE              =553        # from enum PCDSTARTFEATTYPES
	CONST__PROJ_CYLINDER          =562        # from enum PCDSTARTFEATTYPES
	CONST__PROJ_LINE              =542        # from enum PCDSTARTFEATTYPES
	CONST__PROJ_POINT             =512        # from enum PCDSTARTFEATTYPES
	CONST__PROJ_SPHERE            =532        # from enum PCDSTARTFEATTYPES
	CONST__PRTO_LINE              =549        # from enum PCDSTARTFEATTYPES
	CONST__PRTO_PLANE             =577        # from enum PCDSTARTFEATTYPES
	CONST__REV_CIRCLE             =523        # from enum PCDSTARTFEATTYPES
	CONST__REV_CONE               =554        # from enum PCDSTARTFEATTYPES
	CONST__REV_CYLINDER           =563        # from enum PCDSTARTFEATTYPES
	CONST__REV_LINE               =543        # from enum PCDSTARTFEATTYPES
	CONST__REV_PLANE              =572        # from enum PCDSTARTFEATTYPES
	CONST__REV_SPHERE             =533        # from enum PCDSTARTFEATTYPES
	CONST__SCAN_SEG_ARC           =527        # from enum PCDSTARTFEATTYPES
	CONST__SCAN_SEG_LINE          =539        # from enum PCDSTARTFEATTYPES
	CONST__SET                    =596        # from enum PCDSTARTFEATTYPES
	MEASURED__CIRCLE              =202        # from enum PCDSTARTFEATTYPES
	MEASURED__CONE                =205        # from enum PCDSTARTFEATTYPES
	MEASURED__CYLINDER            =206        # from enum PCDSTARTFEATTYPES
	MEASURED__LINE                =204        # from enum PCDSTARTFEATTYPES
	MEASURED__PLANE               =207        # from enum PCDSTARTFEATTYPES
	MEASURED__POINT               =201        # from enum PCDSTARTFEATTYPES
	MEASURED__SET                 =210        # from enum PCDSTARTFEATTYPES
	MEASURED__SPHERE              =203        # from enum PCDSTARTFEATTYPES
	MEAS_CIRCLE                   =202        # from enum PCDSTARTFEATTYPES
	MEAS_CONE                     =205        # from enum PCDSTARTFEATTYPES
	MEAS_CYLINDER                 =206        # from enum PCDSTARTFEATTYPES
	MEAS_LINE                     =204        # from enum PCDSTARTFEATTYPES
	MEAS_PLANE                    =207        # from enum PCDSTARTFEATTYPES
	MEAS_POINT                    =201        # from enum PCDSTARTFEATTYPES
	MEAS_SET                      =210        # from enum PCDSTARTFEATTYPES
	MEAS_SPHERE                   =203        # from enum PCDSTARTFEATTYPES
	PCD__CURVE                    =38         # from enum PCDSTARTFEATTYPES
	READ__POINT                   =192        # from enum PCDSTARTFEATTYPES
	PCD_AUTOCLEARPLANE            =8          # from enum PCDSTARTSCANFLAGS
	PCD_HITNOTDISPLAYED           =16         # from enum PCDSTARTSCANFLAGS
	PCD_MASTERMODE                =2          # from enum PCDSTARTSCANFLAGS
	PCD_RELEARNMODE               =4          # from enum PCDSTARTSCANFLAGS
	PCD_SINGLEPOINT               =1          # from enum PCDSTARTSCANFLAGS
	PCD_HPROBE                    =5          # from enum PCDSTARTSCANTYPES
	PCD_LINEAR_CLOSED             =2          # from enum PCDSTARTSCANTYPES
	PCD_LINEAR_OPEN               =1          # from enum PCDSTARTSCANTYPES
	PCD_MANUALTTP                 =4          # from enum PCDSTARTSCANTYPES
	PCD_PATCH                     =3          # from enum PCDSTARTSCANTYPES
	PCD_PERIMETER                 =25         # from enum PCDSTARTSCANTYPES
	PCD_SECTION                   =24         # from enum PCDSTARTSCANTYPES
	PCD_DO_CONTROL_CALCS          =2          # from enum PCDSTATSFLAGS
	PCD_USE_DIM_NAME              =0          # from enum PCDSTATSFLAGS
	PCD_USE_FEAT_NAME             =1          # from enum PCDSTATSFLAGS
	PCD_ONE5STOPBITS              =22         # from enum PCDSTOPBITS
	PCD_ONESTOPBIT                =21         # from enum PCDSTOPBITS
	PCD_TWOSTOPBITS               =23         # from enum PCDSTOPBITS
	PCD_NO                        =0          # from enum PCDYESNO
	PCD_YES                       =-1         # from enum PCDYESNO
	PTPA_ContactAutoMoveProperties=23         # from enum Probe_Tool_Page
	PTPA_ContactFindHoleProperties=24         # from enum Probe_Tool_Page
	PTPA_ContactPathProperties    =21         # from enum Probe_Tool_Page
	PTPA_ContactSampleHitsProperties=22         # from enum Probe_Tool_Page
	PTPA_ContactTargets           =5          # from enum Probe_Tool_Page
	PTPA_LaserClippingPropertyPage=18         # from enum Probe_Tool_Page
	PTPA_LaserFeatExtractPropertyPage=19         # from enum Probe_Tool_Page
	PTPA_LaserFilteringCmsProperties=16         # from enum Probe_Tool_Page
	PTPA_LaserFilteringProperties =15         # from enum Probe_Tool_Page
	PTPA_LaserMultipleCreationPage=20         # from enum Probe_Tool_Page
	PTPA_LaserPixelLocatorProperties=17         # from enum Probe_Tool_Page
	PTPA_LaserScanCmsProperties   =13         # from enum Probe_Tool_Page
	PTPA_LaserScanProperties      =12         # from enum Probe_Tool_Page
	PTPA_LaserScanTScanProperties =14         # from enum Probe_Tool_Page
	PTPA_LaserTargets             =4          # from enum Probe_Tool_Page
	PTPA_Location                 =6          # from enum Probe_Tool_Page
	PTPA_MeasurementStrategies    =1          # from enum Probe_Tool_Page
	PTPA_None                     =-1         # from enum Probe_Tool_Page
	PTPA_Probe                    =0          # from enum Probe_Tool_Page
	PTPA_VisionBlobStrategy       =2          # from enum Probe_Tool_Page
	PTPA_VisionDiagnostics        =11         # from enum Probe_Tool_Page
	PTPA_VisionFocus              =9          # from enum Probe_Tool_Page
	PTPA_VisionGage               =10         # from enum Probe_Tool_Page
	PTPA_VisionIllumination       =8          # from enum Probe_Tool_Page
	PTPA_VisionMagnification      =7          # from enum Probe_Tool_Page
	PTPA_VisionTargets            =3          # from enum Probe_Tool_Page
	GenericSheet                  =0          # from enum PropertySheetTypes
	ReportConfigurationSheet      =1          # from enum PropertySheetTypes
	PCD_QUALIFICATION_SETTING_MODE_DCC=1          # from enum QUALIFICATION_SETTINGS_MODE
	PCD_QUALIFICATION_SETTING_MODE_DCC_PLUS_DCC=3          # from enum QUALIFICATION_SETTINGS_MODE
	PCD_QUALIFICATION_SETTING_MODE_MANUAL=0          # from enum QUALIFICATION_SETTINGS_MODE
	PCD_QUALIFICATION_SETTING_MODE_MANUAL_PLUS_DCC=2          # from enum QUALIFICATION_SETTINGS_MODE
	DFQ                           =1          # from enum QdasOutputFileToggleType
	DFX_DFD                       =2          # from enum QdasOutputFileToggleType
	PCD_AUTOPREHIT                =2          # from enum RPROGOPTIONSTYPE
	PCD_AUTOPROJREFPLANE          =4          # from enum RPROGOPTIONSTYPE
	PCD_AUTOTIPSELECT             =1          # from enum RPROGOPTIONSTYPE
	PCD_DISPSPEEDS                =8          # from enum RPROGOPTIONSTYPE
	PCD_ENDKEY                    =16         # from enum RPROGOPTIONSTYPE
	PCD_EXTSHEETMETAL             =32         # from enum RPROGOPTIONSTYPE
	PCD_FLYMODE                   =64         # from enum RPROGOPTIONSTYPE
	PCD_HASINDEXPH9               =6          # from enum RPROGOPTIONSTYPE
	PCD_HASINDEXROTTABLE          =7          # from enum RPROGOPTIONSTYPE
	PCD_HASMANPH9                 =9          # from enum RPROGOPTIONSTYPE
	PCD_HASMANROTTABLE            =11         # from enum RPROGOPTIONSTYPE
	PCD_HASPH9                    =13         # from enum RPROGOPTIONSTYPE
	PCD_HASPHS                    =10         # from enum RPROGOPTIONSTYPE
	PCD_HASROTTABLE               =12         # from enum RPROGOPTIONSTYPE
	PCD_ISARMTYPECMM              =5          # from enum RPROGOPTIONSTYPE
	PCD_ISONLINE                  =3          # from enum RPROGOPTIONSTYPE
	PCD_TABLEAVOIDANCE            =128        # from enum RPROGOPTIONSTYPE
	PCD_USEDIMCOLORS              =256        # from enum RPROGOPTIONSTYPE
	PCD_AUTOTRIGDISTANCE          =5          # from enum RPROGVALUESTYPE
	PCD_DIMPLACES                 =3          # from enum RPROGVALUESTYPE
	PCD_MANRETRACT                =7          # from enum RPROGVALUESTYPE
	PCD_MEASSCALE                 =8          # from enum RPROGVALUESTYPE
	PCD_PH9WARNDELTA              =9          # from enum RPROGVALUESTYPE
	PCD_PROBERADIUS               =2          # from enum RPROGVALUESTYPE
	PCD_ROTTABLEANGLE             =1          # from enum RPROGVALUESTYPE
	PCD_TABLETOL                  =6          # from enum RPROGVALUESTYPE
	PCD_VALISYSERRTIMEOUT         =10         # from enum RPROGVALUESTYPE
	RPT_MIRROR_HORIZONTAL         =1          # from enum RPT_MIRROR_OPT
	RPT_MIRROR_NONE               =0          # from enum RPT_MIRROR_OPT
	RPT_MIRROR_VERTICAL           =2          # from enum RPT_MIRROR_OPT
	RSA_ADMINISTRATOR             =0          # from enum RS_ACCESS
	RSA_USER                      =1          # from enum RS_ACCESS
	RSG_MACHINE                   =1          # from enum RS_GROUP
	RSG_USER                      =0          # from enum RS_GROUP
	BottomLeft                    =5          # from enum ScreenColorGradientType
	BottomRight                   =6          # from enum ScreenColorGradientType
	LeftRight                     =2          # from enum ScreenColorGradientType
	NONE                          =0          # from enum ScreenColorGradientType
	TopBottom                     =1          # from enum ScreenColorGradientType
	TopLeft                       =3          # from enum ScreenColorGradientType
	TopRight                      =4          # from enum ScreenColorGradientType
	TOOLCUBE                      =2          # from enum TOOLTYPES
	TOOLRING                      =1          # from enum TOOLTYPES
	TOOLSPHERE                    =0          # from enum TOOLTYPES
	SourceNone                    =0          # from enum TraceDataSourceEnum
	SourceQdas                    =1          # from enum TraceDataSourceEnum
	AlphaNumerical                =4          # from enum TraceValueTypeEnum
	DateTime                      =3          # from enum TraceValueTypeEnum
	FileName                      =5          # from enum TraceValueTypeEnum
	SpecialCoding                 =6          # from enum TraceValueTypeEnum
	TypeFloat                     =2          # from enum TraceValueTypeEnum
	TypeInteger                   =1          # from enum TraceValueTypeEnum
	ValueTypeNone                 =0          # from enum TraceValueTypeEnum
	INCH                          =0          # from enum UNITTYPE
	MM                            =1          # from enum UNITTYPE
	VARIABLE_TYPE_ARRAY           =5          # from enum VARIABLE_TYPE_TYPES
	VARIABLE_TYPE_COMMAND         =4          # from enum VARIABLE_TYPE_TYPES
	VARIABLE_TYPE_DOUBLE          =1          # from enum VARIABLE_TYPE_TYPES
	VARIABLE_TYPE_FUNCTION        =7          # from enum VARIABLE_TYPE_TYPES
	VARIABLE_TYPE_LONG            =0          # from enum VARIABLE_TYPE_TYPES
	VARIABLE_TYPE_POINT           =2          # from enum VARIABLE_TYPE_TYPES
	VARIABLE_TYPE_STRING          =3          # from enum VARIABLE_TYPE_TYPES
	PCD_XMINUS                    =16         # from enum WAXISTYPE
	PCD_XPLUS                     =32         # from enum WAXISTYPE
	PCD_YMINUS                    =4          # from enum WAXISTYPE
	PCD_YPLUS                     =8          # from enum WAXISTYPE
	PCD_ZMINUS                    =2          # from enum WAXISTYPE
	PCD_ZPLUS                     =1          # from enum WAXISTYPE
	PCD_BACK                      =8          # from enum WPLANETYPE
	PCD_BOTTOM                    =2          # from enum WPLANETYPE
	PCD_FRONT                     =4          # from enum WPLANETYPE
	PCD_LEFT                      =16         # from enum WPLANETYPE
	PCD_RIGHT                     =32         # from enum WPLANETYPE
	PCD_TOP                       =1          # from enum WPLANETYPE
	PCD__AUTOPREHIT               =2          # from enum WPROGOPTIONSTYPE
	PCD__AUTOPROJREFPLANE         =4          # from enum WPROGOPTIONSTYPE
	PCD__AUTOTIPSELECT            =1          # from enum WPROGOPTIONSTYPE
	PCD__DISPSPEEDS               =8          # from enum WPROGOPTIONSTYPE
	PCD__ENDKEY                   =16         # from enum WPROGOPTIONSTYPE
	PCD__EXTSHEETMETAL            =32         # from enum WPROGOPTIONSTYPE
	PCD__FLYMODE                  =64         # from enum WPROGOPTIONSTYPE
	PCD__TABLEAVOIDANCE           =128        # from enum WPROGOPTIONSTYPE
	PCD__USEDIMCOLORS             =256        # from enum WPROGOPTIONSTYPE
	PCD__AUTOTRIGDISTANCE         =5          # from enum WPROGVALUESTYPE
	PCD__DIMPLACES                =3          # from enum WPROGVALUESTYPE
	PCD__MANRETRACT               =7          # from enum WPROGVALUESTYPE
	PCD__MEASSCALE                =8          # from enum WPROGVALUESTYPE
	PCD__PH9WARNDELTA             =9          # from enum WPROGVALUESTYPE
	PCD__PROBERADIUS              =2          # from enum WPROGVALUESTYPE
	PCD__TABLETOL                 =6          # from enum WPROGVALUESTYPE
	PCD__VALISYSERRTIMEOUT        =10         # from enum WPROGVALUESTYPE
	FILE_OPEN_ERROR               =0          # from enum XMLImport_StatusCode
	IMPORT_FAILED                 =-1         # from enum XMLImport_StatusCode
	IMPORT_HEADER_NOT_FOUND       =4          # from enum XMLImport_StatusCode
	IMPORT_OK                     =2          # from enum XMLImport_StatusCode
	IMPORT_UNITS_MISMATCH         =3          # from enum XMLImport_StatusCode
	INSPECTIONPLAN_TAG_NOT_FOUND  =1          # from enum XMLImport_StatusCode
	PCD_BALLCENTER                =604        # from enum XYZTYPES
	PCD_CENTROID                  =603        # from enum XYZTYPES
	PCD_ENDPOINT                  =606        # from enum XYZTYPES
	PCD_MIDPOINT                  =607        # from enum XYZTYPES
	PCD_STARTPOINT                =605        # from enum XYZTYPES

RecordMap = {
}

CLSIDToClassMap = {}
CLSIDToPackageMap = {
	'{32C9FBEE-F603-4089-9219-2EB75A48A9AF}' : 'IFCFCommand',
	'{DBFA4CA8-C490-11D3-91B5-00C04F796327}' : 'IApplication',
	'{F8513E14-EAC0-11D1-94C3-0060084043B5}' : 'IPartPrograms',
	'{0699769F-B3D6-11D1-AF79-004005421EEC}' : 'IPartProgram',
	'{72555400-EC03-11D1-94C4-0060084043B5}' : 'IEditWindow',
	'{FCCF1AEB-FA24-11D1-94DC-0060084043B5}' : 'ICommand',
	'{FCCF1AE8-FA24-11D1-94DC-0060084043B5}' : 'ICommands',
	'{EB3ECBD1-0B76-11D2-94F0-0060084043B5}' : 'IAlignCommand',
	'{DBFA4CA7-C490-11D3-91B5-00C04F796327}' : 'IPoint',
	'{DBFA4CA4-C490-11D3-91B5-00C04F796327}' : 'IDmisMatrix',
	'{EB3ECBD4-0B76-11D2-94F0-0060084043B5}' : 'IDimensionCmd',
	'{EB3ECBD7-0B76-11D2-94F0-0060084043B5}' : 'IFeatCmd',
	'{2B25D782-AE2B-4EA0-BF00-E187C407A953}' : 'ITargets',
	'{164B26EB-91CB-43B3-A3C5-26998E7D9967}' : 'ITarget',
	'{EB3ECBDA-0B76-11D2-94F0-0060084043B5}' : 'IModalCmd',
	'{EB3ECBDD-0B76-11D2-94F0-0060084043B5}' : 'IMoveCmd',
	'{EB3ECBE0-0B76-11D2-94F0-0060084043B5}' : 'IFlowControlCmd',
	'{6DD103A4-28C4-11D2-910D-00C04F796327}' : 'IBasicScan',
	'{DBFA4CA3-C490-11D3-91B5-00C04F796327}' : 'IControlPoint',
	'{75EF6188-A979-11D2-9158-00C04F796327}' : 'ICalibration',
	'{75EF618C-A979-11D2-9158-00C04F796327}' : 'IAttach',
	'{75EF618F-A979-11D2-9158-00C04F796327}' : 'IExtCmd',
	'{75EF6192-A979-11D2-9158-00C04F796327}' : 'IOptionProbe',
	'{22C19177-E23F-11D2-B2FD-00C04F79637E}' : 'ILeapfrog',
	'{75EF6195-A979-11D2-9158-00C04F796327}' : 'IOptMotion',
	'{75EF6198-A979-11D2-9158-00C04F796327}' : 'IArrayIndex',
	'{75EF619B-A979-11D2-9158-00C04F796327}' : 'IFileIO',
	'{D0BC0E6D-AA4C-11D2-9158-00C04F796327}' : 'ITempComp',
	'{D0BC0E70-AA4C-11D2-9158-00C04F796327}' : 'IDispMetaFile',
	'{D0BC0E73-AA4C-11D2-9158-00C04F796327}' : 'IComment',
	'{D0BC0E76-AA4C-11D2-9158-00C04F796327}' : 'IStatistics',
	'{D0BC0E79-AA4C-11D2-9158-00C04F796327}' : 'ITraceField',
	'{D0BC0E7C-AA4C-11D2-9158-00C04F796327}' : 'IActiveTip',
	'{D0BC0E7F-AA4C-11D2-9158-00C04F796327}' : 'ILoadProbe',
	'{AF323DB7-AB0A-11D2-9158-00C04F796327}' : 'IDimFormat',
	'{AF323DBA-AB0A-11D2-9158-00C04F796327}' : 'IDimInfo',
	'{AF323DBD-AB0A-11D2-9158-00C04F796327}' : 'ILoadMachine',
	'{22407E79-608A-4D52-9B1D-465A486C81C4}' : 'IDataTypes',
	'{1202BE48-1B3C-45FB-BBB4-251DECBA02DE}' : 'IDataType',
	'{5C4DEB86-82ED-460B-9861-990503BF692D}' : 'IToolkitInternalCommands',
	'{AC0A42F6-617F-404A-B5FD-8612A9DBB92F}' : 'IStrategies',
	'{49DB8F85-3B2D-49AD-BB36-FFECA93BA97C}' : 'IStrategy',
	'{440AA797-C1F1-11D2-915D-00C04F796327}' : 'IDialog',
	'{E25251FE-27E8-4D8B-8852-98C9538A6061}' : 'IVariable',
	'{F8513E17-EAC0-11D1-94C3-0060084043B5}' : 'IOldBasic',
	'{DBFA4CA5-C490-11D3-91B5-00C04F796327}' : 'IFeatData',
	'{DBFA4CA6-C490-11D3-91B5-00C04F796327}' : 'IDimData',
	'{01F079F4-0209-11D2-A88A-482A06000000}' : 'ICadWindows',
	'{01F079F1-0209-11D2-A88A-482A06000000}' : 'ICadWindow',
	'{FCCF1ADF-FA24-11D1-94DC-0060084043B5}' : 'ITools',
	'{FCCF1AE2-FA24-11D1-94DC-0060084043B5}' : 'ITool',
	'{FCCF1AC1-FA24-11D1-94DC-0060084043B5}' : 'IProbes',
	'{FCCF1AC4-FA24-11D1-94DC-0060084043B5}' : 'IProbe',
	'{FCCF1AC7-FA24-11D1-94DC-0060084043B5}' : 'ITips',
	'{FCCF1ACA-FA24-11D1-94DC-0060084043B5}' : 'ITip',
	'{DBEFFD8F-8633-11D3-8B56-00C04F796352}' : 'IQualificationSettings',
	'{72555404-EC03-11D1-94C4-0060084043B5}' : 'IMachine',
	'{72555407-EC03-11D1-94C4-0060084043B5}' : 'IMachines',
	'{48378568-6951-4BCE-AA5C-967F2410BD23}' : 'IFPanel',
	'{B399BB60-5B6E-4302-A36F-9DBBEC842290}' : 'ISimulator',
	'{F7AA5E3C-0B88-4A1C-ADB7-382AFE884894}' : 'IArray',
	'{112BE1A4-C99B-11D5-ACCD-004005A2DBB9}' : 'IMasterSlaveDialog',
	'{708019DD-9211-40D6-AA5B-AACC08814146}' : 'ICadModel',
	'{66A57E07-3E65-4855-86A9-5C09D402F3B8}' : 'ICadPolyLinesOnSurface',
	'{64313293-F174-465B-BEFD-C407407AC7D4}' : 'ICadPolyLineOnSurface',
	'{584D132E-E21E-4415-A698-3BBE30E891BD}' : 'ICadPointsOnSurface',
	'{DEBA7389-A1AA-476C-973A-4D8DC5D0824E}' : 'ICadPointOnSurface',
	'{7CCC5A15-B174-4B28-BF0F-68037379F9BE}' : 'ICadHandle',
	'{17B3D7AE-C472-4C69-92D9-6797840E479E}' : 'IPartProgramSettings',
	'{8C6E9223-8A4F-439A-8560-5C8AE3433216}' : 'IMiniroutineSettings',
	'{0E2865D2-E3BD-4C9A-8DC7-DDA345DF253E}' : 'IDefaultDimensionColors',
	'{E0E27082-61E8-4442-BB8F-DACAC26C9F04}' : 'IExecutedCommands',
	'{9BA4E2E1-668C-4C94-A523-501F7515474A}' : 'IReportWindow',
	'{B3996797-3DB3-461A-971D-33D817AED50F}' : 'IPages',
	'{5ED185EF-494D-4D0C-931F-E83424C60315}' : 'IPage',
	'{87870BF7-ED5B-450B-A0EC-A848872134FA}' : 'IReportControls',
	'{33CE09F2-FFB4-4CBD-A906-0DFDD661CB3D}' : 'IReportControl',
	'{D2D09820-9054-11DB-B76B-0002A5D5C51B}' : 'IQuickStart',
	'{9D974AC0-906B-11DB-BB4D-0002A5D5C51B}' : 'IQuickStartTask',
	'{D763AEA0-9071-11DB-B575-0002A5D5C51B}' : 'IQuickStartSteps',
	'{229F5360-9072-11DB-9350-0002A5D5C51B}' : 'IQuickStartStep',
	'{49DA44C0-C066-11DB-AEB0-0002A5D5C51B}' : 'IQuickStartAddedCommands',
	'{1A0EA100-B0A0-4F0F-9A57-7316B2692FF8}' : 'IBundledStations',
	'{163B287B-7A93-4922-942A-33B6369E5436}' : 'IBundledStation',
	'{AC613900-226A-4784-A465-AB935B77C834}' : 'ISection',
	'{B72DB878-07CD-4D6A-BF88-5E2DA954C2D9}' : 'ISections',
	'{49B8EF53-B14E-4A41-A88A-733C51964712}' : 'IReportTemplate',
	'{CEED993E-7A5F-49C5-862D-85D30DDB1EE1}' : 'IReportTemplates',
	'{5B072B9E-E710-4D7A-9281-762E6DE2915E}' : 'IColors',
	'{520416B6-026F-45AD-B4F7-4FD732E58CA2}' : 'IColor',
	'{33D34472-461E-488E-B33C-F76470E4BCB3}' : 'IRoutineExecutionTimeManager',
	'{4B626FDC-46CE-45D3-BB5F-4D4284685EEF}' : 'IMiniroutineTimeInfoList',
	'{D33AB825-BB80-4884-8208-20B0AF06E616}' : 'IMiniroutineTimeInfo',
	'{6C4ED348-9DCE-460D-A735-420110714F30}' : 'IProbeToolBoxPages',
	'{C9F7879D-06B4-48FD-95C5-84684655F5CB}' : 'IProbeToolBoxPage',
	'{BA8B88DE-8F0B-4BC7-8A68-2DA9FCA79C40}' : 'IOptimizePath',
	'{D0BC0E7C-AA4C-11D2-9158-00C04F796326}' : 'ILIVWindow',
	'{73655400-EC03-11D1-94C4-0060084043B5}' : 'IExecutionWindow',
	'{D60EE92F-89A6-40EB-B790-345AA4477A16}' : 'IReadoutWindow',
	'{49D98C10-EE7F-422D-8A08-39B62106ED68}' : 'IStringArray',
	'{BB208E06-C78F-11D3-91B7-00C04F796327}' : 'IApplicationObjectEvents',
	'{6DCF14B7-782B-46FC-998C-648E8446F579}' : 'IApplicationSettings',
	'{C788B6D9-F58D-404F-9903-E0D75F641474}' : 'ILabelTemplates',
	'{FC615129-17F1-4118-879C-B6DC39182860}' : 'ILabelTemplate',
	'{FD022274-F973-4EFE-B501-820DE68643BB}' : 'ILabelControls',
	'{8E585DAD-26BD-497C-B74A-3E5BD5ECAA58}' : 'IPortLock',
	'{73D818D8-05CF-4DA7-A086-8BF048C3CE47}' : 'ILmsLicense',
	'{9221F403-70F8-4243-9440-AF69B527E1E1}' : 'IAutomationSettings',
	'{70031A72-A5AC-488D-B5A2-5488D06B6E9D}' : 'IRegistrySettings',
	'{E3A6908D-CB68-42EF-987C-A05B099EDD53}' : 'IRegistrySetting',
	'{4725089D-C54A-11D3-91B5-00C04F796327}' : 'IPartProgramEvents',
	'{72555405-EC03-11D1-94C4-0060084043B5}' : 'IMachineEvents',
	'{8651944B-1F78-11D3-B39B-00C04F79637E}' : 'IAutotrigger',
	'{CD2D3E11-0915-4860-916D-8095446DBBE2}' : 'IPropertySheetDialog',
	'{BB208E07-C78F-11D3-91B7-00C04F796327}' : 'IApplicationEvents',
	'{CF83D545-575C-41F5-A663-DB7EFD5C942C}' : 'IPCDMessageBox',
	'{8E2532D0-34DF-422E-9BD8-A0184EACA497}' : 'ICommentInputDialog',
	'{F2DB4C76-D494-47E3-BE88-24AE5D727179}' : 'IQuickFeatureSelection',
	'{9F997B30-BEBB-49EE-B5CA-421BD953B16D}' : 'Itutorhit',
	'{7C32B767-E299-46DD-938E-C80D74BB3FAA}' : 'IAnalysisWindow',
	'{C838CEFB-9F7A-40CC-96FB-328778919190}' : 'IHOBPointInfoList',
	'{80328CB9-F862-45DE-B655-C0654B349D10}' : 'IHOBPointInfo',
	'{069986B7-B3D6-11D1-AF79-004005421EEC}' : 'PartProgram',
	'{89D29409-C75A-4D0E-AB57-8206801C476C}' : 'Application',
	'{F8513E16-EAC0-11D1-94C3-0060084043B5}' : 'PartPrograms',
	'{54D10ACE-5CF5-4BBD-A358-94549AFC0887}' : 'OldBasic',
	'{72555402-EC03-11D1-94C4-0060084043B5}' : 'EditWindow',
	'{73655402-EC03-11D1-94C4-0060084043B5}' : 'ExecutionWindow',
	'{72555406-EC03-11D1-94C4-0060084043B5}' : 'Machine',
	'{72555409-EC03-11D1-94C4-0060084043B5}' : 'Machines',
	'{B8B43A25-7A4C-4552-906F-CD0A38B31A8F}' : 'PointData',
	'{FAFE9D91-DF8D-4C44-8C2F-9699FD853ACE}' : 'FeatData',
	'{22695DBF-D1EC-4B69-B51C-127F382EFCAB}' : 'DimData',
	'{FCCF1AC3-FA24-11D1-94DC-0060084043B5}' : 'Probes',
	'{FCCF1AC6-FA24-11D1-94DC-0060084043B5}' : 'probe',
	'{FCCF1AC9-FA24-11D1-94DC-0060084043B5}' : 'Tips',
	'{FCCF1ACC-FA24-11D1-94DC-0060084043B5}' : 'Tip',
	'{FCCF1AE1-FA24-11D1-94DC-0060084043B5}' : 'Tools',
	'{FCCF1AE4-FA24-11D1-94DC-0060084043B5}' : 'tool',
	'{FCCF1AEA-FA24-11D1-94DC-0060084043B5}' : 'Commands',
	'{E0E27084-61E8-4442-BB8F-DACAC26C9F04}' : 'ExecutedCommands',
	'{FCCF1AED-FA24-11D1-94DC-0060084043B5}' : 'Command',
	'{01F079F3-0209-11D2-A88A-482A06000000}' : 'CadWindow',
	'{01F079F6-0209-11D2-A88A-482A06000000}' : 'CadWindows',
	'{EB3ECBD3-0B76-11D2-94F0-0060084043B5}' : 'AlignCmnd',
	'{EB3ECBD6-0B76-11D2-94F0-0060084043B5}' : 'DimensionCmd',
	'{EB3ECBD9-0B76-11D2-94F0-0060084043B5}' : 'FeatCmd',
	'{EB3ECBDC-0B76-11D2-94F0-0060084043B5}' : 'ModalCmd',
	'{EB3ECBDF-0B76-11D2-94F0-0060084043B5}' : 'MoveCmd',
	'{EB3ECBE2-0B76-11D2-94F0-0060084043B5}' : 'FlowControlCmd',
	'{3158BF53-0353-4EED-8E56-649780CFD1EA}' : 'IPicture',
	'{AEF6B82B-53F8-40D4-8E75-7643BAC7C7FC}' : 'PictureData',
	'{6DD103A6-28C4-11D2-910D-00C04F796327}' : 'BasicScan',
	'{6DD103A8-28C4-11D2-910D-00C04F796327}' : 'Scan',
	'{75EF618A-A979-11D2-9158-00C04F796327}' : 'Calibration',
	'{75EF618E-A979-11D2-9158-00C04F796327}' : 'Attach',
	'{75EF6191-A979-11D2-9158-00C04F796327}' : 'ExternalCommand',
	'{75EF6194-A979-11D2-9158-00C04F796327}' : 'OPTIONPROBE',
	'{C82047B5-E246-11D2-B2FD-00C04F79637E}' : 'LEAPFROG',
	'{B01A08E7-1F7A-11D3-B39B-00C04F79637E}' : 'Autotrigger',
	'{75EF6197-A979-11D2-9158-00C04F796327}' : 'OptMotion',
	'{75EF619A-A979-11D2-9158-00C04F796327}' : 'ArrayIndex',
	'{75EF619D-A979-11D2-9158-00C04F796327}' : 'FileIO',
	'{D0BC0E6F-AA4C-11D2-9158-00C04F796327}' : 'TempComp',
	'{D0BC0E72-AA4C-11D2-9158-00C04F796327}' : 'DispMetaFile',
	'{D0BC0E75-AA4C-11D2-9158-00C04F796327}' : 'Comment',
	'{D0BC0E78-AA4C-11D2-9158-00C04F796327}' : 'STATISTICS',
	'{D0BC0E7B-AA4C-11D2-9158-00C04F796327}' : 'TRACEFIELD',
	'{D0BC0E7E-AA4C-11D2-9158-00C04F796327}' : 'ActiveTip',
	'{D0BC0E7E-AA4C-11D2-9158-00C04F796326}' : 'LIVWindow',
	'{D0BC0E81-AA4C-11D2-9158-00C04F796327}' : 'LoadProbe',
	'{AF323DB9-AB0A-11D2-9158-00C04F796327}' : 'DimFormat',
	'{AF323DBC-AB0A-11D2-9158-00C04F796327}' : 'DimInfo',
	'{AF323DBF-AB0A-11D2-9158-00C04F796327}' : 'LoadMachine',
	'{BA8D02EB-9262-44C0-A94A-ED3C56090707}' : 'DmisMatrix',
	'{440AA799-C1F1-11D2-915D-00C04F796327}' : 'DmisDialog',
	'{72629B79-D1BB-42B4-A6B9-CD6D620C3856}' : 'ControlPoint',
	'{DBEFFD91-8633-11D3-8B56-00C04F796352}' : 'QualificationSettings',
	'{BB208E08-C78F-11D3-91B7-00C04F796327}' : 'ApplicationObjectEvents',
	'{22407E7B-608A-4D52-9B1D-465A486C81C4}' : 'DataTypes',
	'{1202BE4A-1B3C-45FB-BBB4-251DECBA02DE}' : 'DataType',
	'{E25251FF-27E8-4D8B-8852-98C9538A6061}' : 'Variable',
	'{E7B7452E-DC6D-43C6-BD6E-2BF8BA639C66}' : 'tutorhit',
	'{92B4F07A-6108-486B-8D5B-ED6585CBB6D8}' : 'RegistrySettings',
	'{592E472E-3A42-4CC4-ADEF-54B1E0016C1A}' : 'RegistrySetting',
	'{112BE1A6-C99B-11D5-ACCD-004005A2DBB9}' : 'MasterSlaveDlg',
	'{EE7E22A4-F638-41BD-8A39-C482491F9CD6}' : 'ReportWindow',
	'{17B3D7AF-C472-4C69-92D9-6797840E479E}' : 'PartProgramSettings',
	'{AB73A4FD-D9E9-4D0A-8967-3444D6EA55EE}' : 'ApplicationSettings',
	'{13AC5439-CDD7-41F3-A289-64E625B61AD7}' : 'AutomationSettings',
	'{6F79B3A6-91DC-4FCE-95CF-56F841F096EA}' : 'CadHandle',
	'{98A4E4AB-7F12-42DA-B4CE-3FA85A2E62C0}' : 'CadModel',
	'{8058B133-FB7A-41BC-9841-65931448321A}' : 'FPanel',
	'{626D708C-AE68-471D-881A-E0937A5B1CD7}' : 'ReportTemplate',
	'{84AC695A-C435-4204-B5A1-3902369A7744}' : 'ReportTemplates',
	'{82E32640-1D89-4450-A987-6D9C40354542}' : 'VariableArray',
	'{A3E62781-0344-4650-AA15-B8DD1587ECAA}' : 'StringArray',
	'{ADEC1245-B314-4D32-A0A9-CDDEBB508C80}' : 'Section',
	'{710DF803-C9F5-4E47-9766-A8D04D81EE9C}' : 'Sections',
	'{709B1A9A-0E64-4255-A9AD-FC6F50508567}' : 'IReportData',
	'{491BA70B-1CFA-4EAE-8E3A-2404DFF5BF78}' : 'ReportData',
	'{8B856336-30C5-4278-A7FB-F02A0FA3D61C}' : 'ReportControls',
	'{7BA33A05-56E0-4B23-8088-272ED598E3CB}' : 'ReportControl',
	'{224B46E3-78B3-484D-946D-03C8FC479B2E}' : 'Targets',
	'{249C4869-0810-4333-AA51-D16DA3E3E6DB}' : 'Target',
	'{4DFB7CFF-B31A-4FEF-AA85-8F2A40AA9916}' : 'CadPolyLinesOnSurface',
	'{5394725A-31F3-4B1A-B42B-2181C548003A}' : 'CadPolyLineOnSurface',
	'{9CA26F44-7387-42A5-9942-D2A513FE7F34}' : 'CadPointsOnSurface',
	'{F9321DBE-14EA-4490-A60E-E0579A8138F4}' : 'CadPointOnSurface',
	'{D7954947-6BB2-4576-B613-FB08D0F24668}' : 'LabelTemplate',
	'{D1B75762-12F4-43FF-917D-DEDBB93BA3BB}' : 'LabelTemplates',
	'{F83B63E2-876F-4157-ABC4-1EC69703DE34}' : 'LabelControls',
	'{03E04EC5-84F5-4FF5-8303-FF9B233B67BD}' : 'Pages',
	'{68246336-3A48-453A-8444-6531178738A3}' : 'Page',
	'{ACFDB720-9A88-11DB-AF49-0002A5D5C51B}' : 'QuickStartStep',
	'{96469740-9A88-11DB-BB77-0002A5D5C51B}' : 'QuickStartSteps',
	'{7568E500-9A88-11DB-A948-0002A5D5C51B}' : 'QuickStartTask',
	'{31C43120-C066-11DB-9E5E-0002A5D5C51B}' : 'QuickStartAddedCommands',
	'{F47F0C00-9111-11DB-9159-0002A5D5C51B}' : 'QuickStart',
	'{C4807BAF-D1FC-4D9A-AAF7-6C733B904E29}' : 'Colors',
	'{28296353-4639-4821-A5C6-50D4873AF1FE}' : 'Color',
	'{41157E25-645F-4AC5-A216-7D27644CD7BC}' : 'PortLock',
	'{91E705FD-F068-4027-8DFA-2BCFF11AD83A}' : 'LmsLicense',
	'{DD73A98E-1C0C-4569-BE8E-C44AA5DC4014}' : 'BundledStation',
	'{F80275AB-44F6-496E-8E3D-93A538E3921E}' : 'BundledStations',
	'{165236FA-359F-4FF3-8B1F-1E96C193B240}' : 'ReadoutWindow',
	'{4CC8BB59-50AF-464B-AE0D-B17467C1BAF8}' : 'AnalysisWindow',
	'{C5CA7761-B005-4949-A932-4B39FA7207B1}' : 'HOBPointInfoList',
	'{1B4925F7-7EE4-4523-A8C2-C796C3AAD0BB}' : 'HOBPointInfo',
	'{5C4DEB88-82ED-460B-9861-990503BF692D}' : 'ToolkitInternalCommands',
	'{3A0373FF-EADA-4668-9892-AAC291414B39}' : 'PCDMessageBox',
	'{AA5A9C1A-9592-4F25-B7D7-A5EEA5378E77}' : 'CommentInputDialog',
	'{E87A1DF1-F6F7-4E3A-B982-6B67676B1452}' : 'Strategies',
	'{9D277AF4-E64E-4662-90FA-4533ACF0E5C9}' : 'Strategy',
	'{33F17B08-5CA5-48F3-BB66-5F5D5A8CA17B}' : 'FCFCommand',
	'{D878AD2E-F60B-487B-AF84-C95C7DA8248A}' : 'MiniroutineSettings',
	'{C6E621F8-2E7A-4084-9587-268213DA92AA}' : 'RoutineExecutionTimeManager',
	'{1D665211-FF77-42DE-921B-3CE80CE609BF}' : 'MiniroutineTimeInfo',
	'{1C490271-7071-4640-8DF2-41230B3491CC}' : 'MiniroutineTimeInfoList',
	'{17237251-42E4-4B7A-B334-8884115B3BF7}' : 'Simulator',
	'{55DBC58C-5110-40B2-A060-B3F8112345B7}' : 'ProbeToolBoxPages',
	'{A2A8DA62-32D8-460A-BAE0-A720AD55D086}' : 'ProbeToolBoxPage',
	'{0852E0D6-0ABB-43AA-AB06-1FF1AF33049F}' : 'OptimizePath',
	'{3C440739-A16B-415F-B031-6835B9E18B6B}' : 'QuickFeatureSelection',
	'{0CEAFDE5-740D-41D5-B0F0-DFECBACBFC12}' : 'PropertySheetDialog',
	'{82F7F0FA-B111-4642-828D-FF81470B00C8}' : 'DefaultDimensionColors',
}
VTablesToClassMap = {}
VTablesToPackageMap = {
}


NamesToIIDMap = {
	'IFCFCommand' : '{32C9FBEE-F603-4089-9219-2EB75A48A9AF}',
	'IApplication' : '{DBFA4CA8-C490-11D3-91B5-00C04F796327}',
	'IPartPrograms' : '{F8513E14-EAC0-11D1-94C3-0060084043B5}',
	'IPartProgram' : '{0699769F-B3D6-11D1-AF79-004005421EEC}',
	'IEditWindow' : '{72555400-EC03-11D1-94C4-0060084043B5}',
	'ICommand' : '{FCCF1AEB-FA24-11D1-94DC-0060084043B5}',
	'ICommands' : '{FCCF1AE8-FA24-11D1-94DC-0060084043B5}',
	'IAlignCommand' : '{EB3ECBD1-0B76-11D2-94F0-0060084043B5}',
	'IPoint' : '{DBFA4CA7-C490-11D3-91B5-00C04F796327}',
	'IDmisMatrix' : '{DBFA4CA4-C490-11D3-91B5-00C04F796327}',
	'IDimensionCmd' : '{EB3ECBD4-0B76-11D2-94F0-0060084043B5}',
	'IFeatCmd' : '{EB3ECBD7-0B76-11D2-94F0-0060084043B5}',
	'ITargets' : '{2B25D782-AE2B-4EA0-BF00-E187C407A953}',
	'ITarget' : '{164B26EB-91CB-43B3-A3C5-26998E7D9967}',
	'IModalCmd' : '{EB3ECBDA-0B76-11D2-94F0-0060084043B5}',
	'IMoveCmd' : '{EB3ECBDD-0B76-11D2-94F0-0060084043B5}',
	'IFlowControlCmd' : '{EB3ECBE0-0B76-11D2-94F0-0060084043B5}',
	'IBasicScan' : '{6DD103A4-28C4-11D2-910D-00C04F796327}',
	'IControlPoint' : '{DBFA4CA3-C490-11D3-91B5-00C04F796327}',
	'ICalibration' : '{75EF6188-A979-11D2-9158-00C04F796327}',
	'IAttach' : '{75EF618C-A979-11D2-9158-00C04F796327}',
	'IExtCmd' : '{75EF618F-A979-11D2-9158-00C04F796327}',
	'IOptionProbe' : '{75EF6192-A979-11D2-9158-00C04F796327}',
	'ILeapfrog' : '{22C19177-E23F-11D2-B2FD-00C04F79637E}',
	'IOptMotion' : '{75EF6195-A979-11D2-9158-00C04F796327}',
	'IArrayIndex' : '{75EF6198-A979-11D2-9158-00C04F796327}',
	'IFileIO' : '{75EF619B-A979-11D2-9158-00C04F796327}',
	'ITempComp' : '{D0BC0E6D-AA4C-11D2-9158-00C04F796327}',
	'IDispMetaFile' : '{D0BC0E70-AA4C-11D2-9158-00C04F796327}',
	'IComment' : '{D0BC0E73-AA4C-11D2-9158-00C04F796327}',
	'IStatistics' : '{D0BC0E76-AA4C-11D2-9158-00C04F796327}',
	'ITraceField' : '{D0BC0E79-AA4C-11D2-9158-00C04F796327}',
	'IActiveTip' : '{D0BC0E7C-AA4C-11D2-9158-00C04F796327}',
	'ILoadProbe' : '{D0BC0E7F-AA4C-11D2-9158-00C04F796327}',
	'IDimFormat' : '{AF323DB7-AB0A-11D2-9158-00C04F796327}',
	'IDimInfo' : '{AF323DBA-AB0A-11D2-9158-00C04F796327}',
	'ILoadMachine' : '{AF323DBD-AB0A-11D2-9158-00C04F796327}',
	'IDataTypes' : '{22407E79-608A-4D52-9B1D-465A486C81C4}',
	'IDataType' : '{1202BE48-1B3C-45FB-BBB4-251DECBA02DE}',
	'IToolkitInternalCommands' : '{5C4DEB86-82ED-460B-9861-990503BF692D}',
	'IStrategies' : '{AC0A42F6-617F-404A-B5FD-8612A9DBB92F}',
	'IStrategy' : '{49DB8F85-3B2D-49AD-BB36-FFECA93BA97C}',
	'IDialog' : '{440AA797-C1F1-11D2-915D-00C04F796327}',
	'IVariable' : '{E25251FE-27E8-4D8B-8852-98C9538A6061}',
	'IOldBasic' : '{F8513E17-EAC0-11D1-94C3-0060084043B5}',
	'IFeatData' : '{DBFA4CA5-C490-11D3-91B5-00C04F796327}',
	'IDimData' : '{DBFA4CA6-C490-11D3-91B5-00C04F796327}',
	'ICadWindows' : '{01F079F4-0209-11D2-A88A-482A06000000}',
	'ICadWindow' : '{01F079F1-0209-11D2-A88A-482A06000000}',
	'ITools' : '{FCCF1ADF-FA24-11D1-94DC-0060084043B5}',
	'ITool' : '{FCCF1AE2-FA24-11D1-94DC-0060084043B5}',
	'IProbes' : '{FCCF1AC1-FA24-11D1-94DC-0060084043B5}',
	'IProbe' : '{FCCF1AC4-FA24-11D1-94DC-0060084043B5}',
	'ITips' : '{FCCF1AC7-FA24-11D1-94DC-0060084043B5}',
	'ITip' : '{FCCF1ACA-FA24-11D1-94DC-0060084043B5}',
	'IQualificationSettings' : '{DBEFFD8F-8633-11D3-8B56-00C04F796352}',
	'IMachine' : '{72555404-EC03-11D1-94C4-0060084043B5}',
	'IMachines' : '{72555407-EC03-11D1-94C4-0060084043B5}',
	'IFPanel' : '{48378568-6951-4BCE-AA5C-967F2410BD23}',
	'ISimulator' : '{B399BB60-5B6E-4302-A36F-9DBBEC842290}',
	'IArray' : '{F7AA5E3C-0B88-4A1C-ADB7-382AFE884894}',
	'IMasterSlaveDialog' : '{112BE1A4-C99B-11D5-ACCD-004005A2DBB9}',
	'ICadModel' : '{708019DD-9211-40D6-AA5B-AACC08814146}',
	'ICadPolyLinesOnSurface' : '{66A57E07-3E65-4855-86A9-5C09D402F3B8}',
	'ICadPolyLineOnSurface' : '{64313293-F174-465B-BEFD-C407407AC7D4}',
	'ICadPointsOnSurface' : '{584D132E-E21E-4415-A698-3BBE30E891BD}',
	'ICadPointOnSurface' : '{DEBA7389-A1AA-476C-973A-4D8DC5D0824E}',
	'ICadHandle' : '{7CCC5A15-B174-4B28-BF0F-68037379F9BE}',
	'IPartProgramSettings' : '{17B3D7AE-C472-4C69-92D9-6797840E479E}',
	'IMiniroutineSettings' : '{8C6E9223-8A4F-439A-8560-5C8AE3433216}',
	'IDefaultDimensionColors' : '{0E2865D2-E3BD-4C9A-8DC7-DDA345DF253E}',
	'IExecutedCommands' : '{E0E27082-61E8-4442-BB8F-DACAC26C9F04}',
	'IReportWindow' : '{9BA4E2E1-668C-4C94-A523-501F7515474A}',
	'IPages' : '{B3996797-3DB3-461A-971D-33D817AED50F}',
	'IPage' : '{5ED185EF-494D-4D0C-931F-E83424C60315}',
	'IReportControls' : '{87870BF7-ED5B-450B-A0EC-A848872134FA}',
	'IReportControl' : '{33CE09F2-FFB4-4CBD-A906-0DFDD661CB3D}',
	'IQuickStart' : '{D2D09820-9054-11DB-B76B-0002A5D5C51B}',
	'IQuickStartTask' : '{9D974AC0-906B-11DB-BB4D-0002A5D5C51B}',
	'IQuickStartSteps' : '{D763AEA0-9071-11DB-B575-0002A5D5C51B}',
	'IQuickStartStep' : '{229F5360-9072-11DB-9350-0002A5D5C51B}',
	'IQuickStartAddedCommands' : '{49DA44C0-C066-11DB-AEB0-0002A5D5C51B}',
	'IBundledStations' : '{1A0EA100-B0A0-4F0F-9A57-7316B2692FF8}',
	'IBundledStation' : '{163B287B-7A93-4922-942A-33B6369E5436}',
	'ISection' : '{AC613900-226A-4784-A465-AB935B77C834}',
	'ISections' : '{B72DB878-07CD-4D6A-BF88-5E2DA954C2D9}',
	'IReportTemplate' : '{49B8EF53-B14E-4A41-A88A-733C51964712}',
	'IReportTemplates' : '{CEED993E-7A5F-49C5-862D-85D30DDB1EE1}',
	'IColors' : '{5B072B9E-E710-4D7A-9281-762E6DE2915E}',
	'IColor' : '{520416B6-026F-45AD-B4F7-4FD732E58CA2}',
	'IRoutineExecutionTimeManager' : '{33D34472-461E-488E-B33C-F76470E4BCB3}',
	'IMiniroutineTimeInfoList' : '{4B626FDC-46CE-45D3-BB5F-4D4284685EEF}',
	'IMiniroutineTimeInfo' : '{D33AB825-BB80-4884-8208-20B0AF06E616}',
	'IProbeToolBoxPages' : '{6C4ED348-9DCE-460D-A735-420110714F30}',
	'IProbeToolBoxPage' : '{C9F7879D-06B4-48FD-95C5-84684655F5CB}',
	'IOptimizePath' : '{BA8B88DE-8F0B-4BC7-8A68-2DA9FCA79C40}',
	'ILIVWindow' : '{D0BC0E7C-AA4C-11D2-9158-00C04F796326}',
	'IExecutionWindow' : '{73655400-EC03-11D1-94C4-0060084043B5}',
	'IReadoutWindow' : '{D60EE92F-89A6-40EB-B790-345AA4477A16}',
	'IStringArray' : '{49D98C10-EE7F-422D-8A08-39B62106ED68}',
	'IApplicationObjectEvents' : '{BB208E06-C78F-11D3-91B7-00C04F796327}',
	'IApplicationSettings' : '{6DCF14B7-782B-46FC-998C-648E8446F579}',
	'ILabelTemplates' : '{C788B6D9-F58D-404F-9903-E0D75F641474}',
	'ILabelTemplate' : '{FC615129-17F1-4118-879C-B6DC39182860}',
	'ILabelControls' : '{FD022274-F973-4EFE-B501-820DE68643BB}',
	'IPortLock' : '{8E585DAD-26BD-497C-B74A-3E5BD5ECAA58}',
	'ILmsLicense' : '{73D818D8-05CF-4DA7-A086-8BF048C3CE47}',
	'IAutomationSettings' : '{9221F403-70F8-4243-9440-AF69B527E1E1}',
	'IRegistrySettings' : '{70031A72-A5AC-488D-B5A2-5488D06B6E9D}',
	'IRegistrySetting' : '{E3A6908D-CB68-42EF-987C-A05B099EDD53}',
	'IPartProgramEvents' : '{4725089D-C54A-11D3-91B5-00C04F796327}',
	'IMachineEvents' : '{72555405-EC03-11D1-94C4-0060084043B5}',
	'IAutotrigger' : '{8651944B-1F78-11D3-B39B-00C04F79637E}',
	'IPropertySheetDialog' : '{CD2D3E11-0915-4860-916D-8095446DBBE2}',
	'IApplicationEvents' : '{BB208E07-C78F-11D3-91B7-00C04F796327}',
	'IPCDMessageBox' : '{CF83D545-575C-41F5-A663-DB7EFD5C942C}',
	'ICommentInputDialog' : '{8E2532D0-34DF-422E-9BD8-A0184EACA497}',
	'IQuickFeatureSelection' : '{F2DB4C76-D494-47E3-BE88-24AE5D727179}',
	'Itutorhit' : '{9F997B30-BEBB-49EE-B5CA-421BD953B16D}',
	'IAnalysisWindow' : '{7C32B767-E299-46DD-938E-C80D74BB3FAA}',
	'IHOBPointInfoList' : '{C838CEFB-9F7A-40CC-96FB-328778919190}',
	'IHOBPointInfo' : '{80328CB9-F862-45DE-B655-C0654B349D10}',
	'IPicture' : '{3158BF53-0353-4EED-8E56-649780CFD1EA}',
	'IReportData' : '{709B1A9A-0E64-4255-A9AD-FC6F50508567}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

