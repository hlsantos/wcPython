# Created by cpp2py on 2023-02-03 12:40:46.585019

import ctypes
from ctypes import wintypes
from ctypes.wintypes import *
from enum import IntEnum
from wcpapi.wctype_h import *
from wcpapi.wctype_constants_h import *


class PropertyStruct(ctypes.Structure):
    def __getattribute__(self, name):
        val = object.__getattribute__(self, name)
        if isinstance(val, bytes):
            try:
              _val = val.decode('ISO-8859-1','ignore')
            except:
                try:
                  _val = val.decode('UTF-8','ignore')
                except:
                  _val = hex(val)
            return _val
        return val
    def __setattr__(self, name, value):
        if isinstance(value, str):
            value = value.encode('UTF-8','ignore')
        object.__setattr__(self, name, value)

class TAutoResponseName(PropertyStruct):
    _fields_ = [
        ('name', ctypes.c_char*SIZE_USER_NAME),
    ]

class TGateQwkHost(PropertyStruct):
    _fields_ = [
        ('Name', ctypes.c_char*SIZE_GATE_HOST_NAME),
        ('QwkPath', ctypes.c_char*MAX_PATH),
        ('RepPath', ctypes.c_char*MAX_PATH),
        ('AttachmentSizeLimit', DWORD),
        ('Packer', DWORD),
        ('AtFilter', BOOL),
        ('GateTag', BOOL),
        ('AppendRepPackets', BOOL),
        ('Index', DWORD),
        ('Reserved', BYTE*84),
    ]

class TGateQwkConf(ctypes.Structure):
    _fields_ = [
        ('Conference', DWORD),
        ('HubConference', DWORD),
        ('TaglineId', DWORD),
        ('ExportPrivateMail', BOOL),
    ]

class TGateUucpConfig(PropertyStruct):
    _fields_ = [
        ('AdministratorName', ctypes.c_char*SIZE_USER_NAME),
        ('LocalDomain', ctypes.c_char*SIZE_DOMAIN_NAME),
        ('LocalSiteName', ctypes.c_char*SIZE_DOMAIN_NAME),
        ('AlternateDomain', ctypes.c_char*SIZE_DOMAIN_NAME),
        ('Organization', ctypes.c_char*SIZE_GATE_ORGANIZATION),
        ('NewsRequestName', ctypes.c_char*SIZE_USER_NAME),
        ('PrimaryProvider', ctypes.c_char*SIZE_GATE_HOST_NAME),
        ('Reserved1', DWORD),
        ('BounceInvalidMessages', BOOL),
        ('MaxExportMessageCount', DWORD),
        ('Reserved', BYTE*72),
    ]

class TGateUucpHost(PropertyStruct):
    _fields_ = [
        ('Name', ctypes.c_char*SIZE_GATE_HOST_NAME),
        ('Administrator', ctypes.c_char*SIZE_USER_NAME),
        ('Domain', ctypes.c_char*SIZE_DOMAIN_NAME),
        ('SiteName', ctypes.c_char*SIZE_DOMAIN_NAME),
        ('AttachmentSizeLimit', DWORD),
        ('DeleteFiles', BOOL),
        ('AllowNewsRequests', BOOL),
        ('SpoolPath', ctypes.c_char*MAX_PATH),
        ('AdditionalSpoolPath', ctypes.c_char*MAX_PATH),
        ('dwHostFlags', DWORD),
        ('EmailConference', DWORD),
        ('HostType', DWORD),
        ('Reserved', BYTE*12),
    ]

class TGateTranslateEntry(PropertyStruct):
    _fields_ = [
        ('TranslateType', DWORD),
        ('LocalName', ctypes.c_char*SIZE_USER_NAME),
        ('ExternalName', ctypes.c_char*SIZE_USER_NAME),
    ]

class TGateMailingList(PropertyStruct):
    _fields_ = [
        ('Name', ctypes.c_char*SIZE_USER_NAME),
        ('Conference', DWORD),
        ('Reserved', BYTE*52),
    ]

class TRpcTextData(ctypes.Structure):
    _fields_ = [
        ('size', DWORD),
    ]

