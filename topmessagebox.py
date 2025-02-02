import tkinter as tk
from tkinter import messagebox

class TopMessagebox:
    INFO = 0
    WARNING = 1
    ERROR = 2

    @staticmethod
    def show(title: str, msg: str, level: int = INFO):
        """
        顶层消息框

        Params:
            title: 消息框标题
            msg: 消息内容
            level: 消息框级别，默认为INFO
        """
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)

        match level:
            case TopMessagebox.WARNING:
                messagebox.showwarning(title, msg)
            case TopMessagebox.ERROR:
                messagebox.showerror(title, msg)
            case _:
                messagebox.showinfo(title, msg)

        root.destroy()