/**
 * @file      main.cpp
 * @brief     全局加载英语（美国）布局，并强制将当前活跃窗口切换至该布局。
 * @author    IYATT-yx
 * @copyright Copyright (c) 2026 IYATT-yx.
 * Licensed under the MIT License. See LICENSE file in the project root for full license information.
 */

#include <Windows.h>
#include <iostream>

int wmain(int argc, wchar_t* argv[])
{
    // 支持控制台正确显示宽字符
    std::wcout.imbue(std::locale("chs"));
    std::wcout << L"正在检查并强制构建纯英语(美国)输入法布局..." << std::endl;

    // 动态加载美式英语键盘布局 ("00000409")
    // KLF_ACTIVATE: 瞬间激活
    HKL hKlEnglish = ::LoadKeyboardLayoutW(L"00000409", KLF_ACTIVATE);

    if (hKlEnglish != nullptr)
    {
        // 改变系统未来新窗口的默认语言
        ::SystemParametersInfoW(SPI_SETDEFAULTINPUTLANG, 0, &hKlEnglish, SPIF_SENDCHANGE);

        // 获取当前真正处于活跃状态的顶层窗口
        HWND hWndFore = ::GetForegroundWindow();

        if (hWndFore != nullptr)
        {
            // 向当前活跃窗口直接投递语言切换请求
            // INPUTLANGCHANGE_FORWARD 表示向前切换布局，这能瞬间逼迫 Windows 输入法管理器刷新当前窗口状态
            ::SendMessageW(hWndFore, WM_INPUTLANGCHANGEREQUEST, INPUTLANGCHANGE_FORWARD, reinterpret_cast<LPARAM>(hKlEnglish));

            // 同时激活当前小工具自身进程的布局，双重保险
            ::ActivateKeyboardLayout(hKlEnglish, KLF_SETFORPROCESS);

            std::wcout << L"成功：已向当前活动窗口发送英语切换请求，并刷新全局默认设置。" << std::endl;
        }
        else
        {
            std::wcout << L"警告：未捕获到有效的前台活跃窗口。" << std::endl;
        }
    }
    else
    {
        std::wcout << L"错误：无法加载美式英语键盘布局。" << std::endl;
        return 1;
    }

    return 0;
}