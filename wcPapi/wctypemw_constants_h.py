# Auto-created by cpp2constant.py on 2023-01-30 20:55:23.945158
# input file : include\wctypemw.h
# output file: wcpapi\wctypemw_constants_h.py

from enum import IntEnum

MAX_PATH                                 = 260

#+ Group: Configuration Structures

#!---------------------------------------------------------
#! TConferencePaths provides the various directory setups
#! per mail confeference
#!---------------------------------------------------------

#!---------------------------------------------------------
#! TWildcatServerPrivateConfig is the configuration "MakeWild"
#! structure. The public field is exposed to normal
#! SDK clients.
#!---------------------------------------------------------

srvFingerServer                          = 0x00000001 #! Enable Finger Server
srvWcxMwLogin                            = 0x00000002 #! Allow WCX MwLogin
srvWcxIpCheck                            = 0x00000004 #! Check WCX Peer Address
srvOnlyLocalRPC                          = 0x00000008 #! Local RPC Only (v5.7)
srvEnableGeoIP                           = 0x00000010 #! Open GeoIP database

#!---------------------------------------------------------
#! TWildcatServerPrivateConfDesc defines a mail conference
#! setup.
#!---------------------------------------------------------

#!---------------------------------------------------------
#! TWildcatServerPrivateConfDesc defines a mail conference
#! setup.
#!---------------------------------------------------------

#!---------------------------------------------------------
#! TWildcatServerPrivateFileVolumec provides CD volume
#! setup information.
#!---------------------------------------------------------

