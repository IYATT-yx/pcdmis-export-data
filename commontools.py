import os
import sys
import time
import pathlib
import ctypes

class CommonTools:
    @staticmethod
    def getHomePath() -> str:
        """
        获取家目录

        Returns:
            str: 家目录路径
        """
        return os.path.expanduser("~")
    
    @staticmethod
    def getPackagedStatus():
        """
        获取打包状态

        Returns:
            bool: 是否为打包状态
        """
        return getattr(sys, 'frozen', False)
    
    @staticmethod
    def checkFileExist(filePath: str) -> bool:
        """
        检查文件或文件夹是否已经存在

        Params:
            filePath (str): 文件路径

        Returns:
            bool: 是否存在
        """
        return os.path.exists(filePath)
    
    @staticmethod
    def getTimeStamp(mode: int = 0) -> str:
        """
        获取当前时间戳

        Params:
            mode (int): 时间戳格式，0为完整时间戳，1为日期戳；2为日期戳，带分隔符号；3为时间戳，带分隔符

        Returns:
            str: 时间戳
        """
        match mode:
            case 0:
                return time.strftime("%Y%m%d_%H%M%S", time.localtime())
            case 1:
                return time.strftime("%Y%m%d", time.localtime())
            case 2:
                return time.strftime("%Y-%m-%d", time.localtime())
            case 3:
                return time.strftime("%H:%M:%S", time.localtime())

            
    @staticmethod
    def getAbsPath(filePath: str) -> str:
        """
        获取绝对路径

        Params:
            filePath (str): 文件路径

        Returns:
            str: 绝对路径
        """
        return os.path.abspath(filePath)
    
    @staticmethod
    def getMyPath() -> str:
        """
        获取当前文件路径

        Returns:
            str: 当前文件路径
        """
        if CommonTools.getPackagedStatus():
            return os.path.dirname(CommonTools.getAbsPath(sys.executable))
        else:
            return os.path.dirname(CommonTools.getAbsPath(__file__))
        
    @staticmethod
    def removeFileExtension(path: str) -> str:
        """
        移除文件扩展名
        """
        return pathlib.Path(path).stem
    
    # @staticmethod
    # def setFileReadOnly(filePath: str, readonly: bool = True):
    #     """
    #     设置文件只读

    #     Params:
    #         filePath (str): 文件路径
    #         readonly (bool): 是否只读
    #     """
    #     if readonly:
    #         os.chmod(filePath, 0o444)
    #     else:
    #         os.chmod(filePath, 0o777)

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
            if CommonTools.getPackagedStatus():
                params = CommonTools.quotingArgs(sys.argv[1:])
            else:
                params = CommonTools.quotingArgs(sys.argv)
            result = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
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

    