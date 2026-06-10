# pcdmis-export-data

PC-DMIS 数据导出工具  
这个项目最初来自同事的提议，他们希望可以批量抓取数据，避免客户需要检测数据的时候花费大量人力去抄录。特别是对于新开发的项目，方便通过汇总数据监管过程。我从 2025 年 1 月中开始构思，当时距离春节还有十几天，主体写于春节几天，后续不断完善。    
![alt text](doc/img/image1.png)  

2026.6.8  
Python 版性能已经难以提升了（受限于 COM 跨进程），我发现通过 PC-DMIS 内置的 BASIC 引擎执行数据读取性能非常好，至少百倍以上的差异。  
最近几天我在[学习 BASIC](https://blog.iyatt.com/?p=24885)，正在重构项目，将读取数据部分改为 BASIC 脚本实现，其它功能用 Python 完成即可。  
旧版纯 Python 方案可见[archive/python-original-version](https://github.com/IYATT-yx/pcdmis-export-data/tree/archive/python-original-version)。  

2026.6.9  
开始重构项目，目前 main 分支不可用，处于半成品阶段。  


## 测试环境

* Python 3.14.5（支持 Windows 10 及以上）  
* MSVC 平台工具集 v145（Visual Studio 2026）
* PC-DMIS 生产环境测试版本：2018 R1、2020 R1、2023.1
* PC-DMIS 开发环境测试版本：2019 R2、2023.1

## 许可证

本项目采用 [MIT 许可证](LICENSE) 进行许可。  