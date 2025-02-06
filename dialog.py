import constants
from topmessagebox import TopMessagebox

import logging
import inspect

class Dialog:
    DEBUG: int = logging.DEBUG
    INFO: int = logging.INFO
    WARNING: int = logging.WARNING
    ERROR: int = logging.ERROR
    CRITICAL: int = logging.CRITICAL

    def __init__(self):
        """
        日志记录器初始化
        """
        # 用上级调用者所在的模块名称作为日志记录器名称
        loggerName = inspect.getmodule(inspect.currentframe().f_back).__name__
        logger = logging.getLogger(loggerName)
        if logger.hasHandlers():
            return
        # 文件输出日志
        fileHandler = logging.FileHandler(constants.Dialog.dialogPath, encoding=constants.Dialog.dialogEncoding)
        # 控制台输出日志
        streamHandler = logging.StreamHandler()
        formatter = logging.Formatter(constants.Dialog.dialogFormat, constants.Dialog.dateFormat)
        fileHandler.setFormatter(formatter)
        streamHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.addHandler(streamHandler)
        logger.setLevel(constants.Dialog.dialogLevel)

    @staticmethod
    def log(message: str, dialogLevel: int = DEBUG):
        """
        写日志

        Params:
            message: 日志信息
            dialogLevel: 日志类型
        """
        loggerName = inspect.getmodule(inspect.currentframe().f_back).__name__
        logger = logging.getLogger(loggerName)
        if not logger.hasHandlers():
            TopMessagebox.show('错误', '日志记录器未初始化，请初始化后使用！', TopMessagebox.ERROR)
            return
        callerFrame = inspect.currentframe().f_back
        callerFunctionName = callerFrame.f_code.co_name
        callerLineno = callerFrame.f_lineno
        messageDetail = f'行号：{callerLineno:<3} 函数名：{callerFunctionName} -> {message}'
        logger.log(dialogLevel, messageDetail)
        match  dialogLevel:
            case Dialog.DEBUG:
                pass
            case Dialog.INFO:
                TopMessagebox.show('信息', message)
            case Dialog.WARNING:
                TopMessagebox.show('警告', message, TopMessagebox.WARNING)
            case Dialog.ERROR:
                TopMessagebox.show('错误', message, TopMessagebox.ERROR)
            case Dialog.CRITICAL:
                TopMessagebox.show('严重错误', message, TopMessagebox.ERROR)