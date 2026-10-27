"""
file: MachineConnectionStatus.py
description: PC-DMIS 2025.1 导出的 MachineConnectionStatus 枚举，用于标识联机类型
author: IYATT-yx
copyright:  Copyright (c) 2026 IYATT-yx.
            Licensed under the MIT License. See LICENSE file in the project root for full license information.
"""
from enum import IntEnum

class MachineConnectionStatus(IntEnum):
	MachineConnected              =2          # from enum MachineConnectionStatus
	MachineConnecting             =1          # from enum MachineConnectionStatus
	MachineDisconnecting          =3          # from enum MachineConnectionStatus
	MachineHoming                 =4          # from enum MachineConnectionStatus
	MachineNotConnected           =0          # from enum MachineConnectionStatus
	NotAvailable                  =-1         # from enum MachineConnectionStatus