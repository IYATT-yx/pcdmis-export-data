from customexception import CustomException

import argparse

class CustomArgParse(argparse.ArgumentParser):
    def error(self, message):
        raise CustomException(f"参数错误：{message}", CustomException.ERROR)