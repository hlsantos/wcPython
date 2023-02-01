# Auto-created by cpp2constant.py on 2023-01-30 20:55:23.957202
# input file : include\wcgtype.h
# output file: wcpapi\wcgtype_constants_h.py

from enum import IntEnum

#+ Group: Configuration Gateway Structures

SIZE_GATE_HOST_NAME                      = SIZE_MESSAGE_NETWORK

SIZE_GATE_ORGANIZATION                   = 80

hfAllowHtmlImport                        = 0x00000001
hfDisableEmailImport                     = 0x00000010
hfDisableEmailExport                     = 0x00000020
hfDisableNewsImport                      = 0x00000100
hfDisableNewsExport                      = 0x00000200
hfReserved                               = 0x00001000 #// 451.6
hfLocalHost                              = 0x00002000 #// 451.6 if off, Remote Host
hfRouteSMTP                              = 0x00004000 #// 451.6 if off, Keep in spool

htEmailAndNews                           = 0 # = 0 default (compatible)
htEmailOnly                              = 1
htNewsOnly                               = 2

teBoth                                   = 0
teImport                                 = 1
teExport                                 = 2

