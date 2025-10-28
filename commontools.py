import constants

import os
import sys
import time
import pathlib
import ctypes

class CommonTools:
    @staticmethod
    def getTimeStamp(timeTuple, mode: int = 0) -> str:
        """
        获取当前时间戳

        Params:
            timeTuple: 时间元组 time.localtime()
            mode (int): 时间戳格式，0为完整时间戳，1为日期戳；2为日期戳，带分隔符号；3为时间戳，带分隔符

        Returns:
            str: 时间戳
        """
        match mode:
            case 0:
                return time.strftime("%Y%m%d_%H%M%S", timeTuple)
            case 1:
                return time.strftime("%Y%m%d", timeTuple)
            case 2:
                return time.strftime("%Y-%m-%d", timeTuple)
            case 3:
                return time.strftime("%H:%M:%S", timeTuple)
            case 4:
                return time.strftime("%H%M%S", timeTuple)

    @staticmethod
    def removeFileExtension(path: str) -> str:
        """
        移除文件扩展名
        """
        return pathlib.Path(path).stem
    
    @staticmethod
    def getInitFolder() -> str:
        """获取初始文件夹路径
        """
        try:
            with open(constants.Path.initFolderPath, 'r') as f:
                initFolder = f.read()
        except FileNotFoundError:
            initFolder = constants.Path.programFileDir
        return initFolder
    
    @staticmethod
    def setInitFolder(folderPath: str):
        """设置初始文件夹路径
        """
        os.makedirs(constants.Path.myDataPath, exist_ok=True)
        with open(constants.Path.initFolderPath, 'w') as f:
            f.write(folderPath)

    @staticmethod
    def getInitFileDir() -> str:
        """获取初始文件目录
        """
        try:
            with open(constants.Path.initFileDir, 'r') as f:
                initFileDir = f.read()
        except FileNotFoundError:
            initFileDir = constants.Path.programFileDir
        return initFileDir
    
    @staticmethod
    def setInitFileDir(filePath: str):
        """取输入文件路径的目录设置初始文件目录

        Args:
            filePath (str): 文件路径
        """
        os.makedirs(constants.Path.myDataPath, exist_ok=True)
        with open(constants.Path.initFileDir, 'w') as f:
            f.write(os.path.dirname(filePath))
    
    @staticmethod
    def quotingArgs(args: list[str]) -> str:
        """
        为参数添加双引号并拼接为一个字符串，保证参数可以正确处理

        Params:
            args (list[str]): 参数列表

        Returns:
            str: 拼接后的字符串
        """
        return ' '.join(f' "{arg}"' for arg in args)

    @staticmethod
    def checkAdmin():
        """
        检查是否是管理员

        Returns:
            bool: 是否是管理员
        """
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
        
    @staticmethod
    def runAsAdmin() -> tuple[bool, str]:
        """
        以管理员身份

        Returns:
            (状态, 消息)： 三种状态：None：已经是管理员身份；True 以管理员身份重新运行成功；False 以管理员身份重新运行失败
        """
        if CommonTools.checkAdmin():
            return None, '已经是管理员'
        
        try:
            if constants.Status.packaged:
                params = CommonTools.quotingArgs(sys.argv[1:])
            else:
                params = CommonTools.quotingArgs(sys.argv)
            result = ctypes.windll.shell32.ShellExecuteW(None, "runas", constants.Path.executableFilePath, params, None, 1)
            if result > 32:
                return True, '以管理员运行成功'
            else:
                match result:
                    case 5:
                        error = '访问被拒绝'
                    case _:
                        error = ''
                return False, f'以管理员身份运行失败，错误代码：{result} {error}'
        except Exception as e:
            return False, f'以管理员身份运行时发生错误：{e}'

    @staticmethod
    def setFileReadOnly(filePath: str, readonly: bool = True):
        """
        设置文件只读

        Params:
            filePath (str): 文件路径
            readonly (bool): 是否只读
        """
        if readonly:
            os.chmod(filePath, 0o444)
        else:
            os.chmod(filePath, 0o777)

    @staticmethod
    def longPath(path: str) -> str:
        """
        将路径转换为长路径

        Params:
            path (str): 路径

        Returns:
            str: 长路径
        """
        path = os.path.normpath(path)
        if not path.startswith("\\\\?\\"):
            # 注意：网络路径（\\Server\Share）要特殊处理
            if path.startswith("\\\\"):
                path = "\\\\?\\UNC" + path[1:]
            else:
                path = "\\\\?\\" + path
        return path