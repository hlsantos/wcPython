# Created by cpp2py on 2023-02-03 12:40:46.569018

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

class TConferencePaths(PropertyStruct):
    _fields_ = [
        ('Display', ctypes.c_char*MAX_PATH),
        ('Bulletin', ctypes.c_char*MAX_PATH),
        ('Help', ctypes.c_char*MAX_PATH),
        ('Menu', ctypes.c_char*MAX_PATH),
        ('Questionnaire', ctypes.c_char*MAX_PATH),
        ('MsgDatabase', ctypes.c_char*MAX_PATH),
        ('Attach', ctypes.c_char*MAX_PATH),
    ]

class TWildcatServerPrivateConfig(PropertyStruct):
    _fields_ = [
        ('Public', TMakewild),
        ('FileDatabasePath', ctypes.c_char*MAX_PATH),
        ('UserDatabasePath', ctypes.c_char*MAX_PATH),
        ('DefaultConferencePaths', TConferencePaths),
        ('SystemPassword', ctypes.c_char*SIZE_ENCODED_PASSWORD),
        ('MakewildPassword', ctypes.c_char*SIZE_ENCODED_PASSWORD),
        ('LanguagePath', ctypes.c_char*MAX_PATH),
        ('BatchFilePath', ctypes.c_char*MAX_PATH),
        ('dwServerOptions', DWORD),
    ]

class TWildcatServerPrivateConfDesc(ctypes.Structure):
    _fields_ = [
        ('Public', TConfDesc),
        ('Paths', TConferencePaths),
    ]

class TWildcatServerInternalConfDesc(ctypes.Structure):
    _fields_ = [
        ('Public', TConfDesc),
        ('DisplayPathIndex', DWORD),
        ('BulletinPathIndex', DWORD),
        ('HelpPathIndex', DWORD),
        ('MenuPathIndex', DWORD),
        ('QuestionnairePathIndex', DWORD),
        ('MsgDatabasePathIndex', DWORD),
        ('AttachPathIndex', DWORD),
    ]

class TWildcatServerPrivateFileArea(PropertyStruct):
    _fields_ = [
        ('Public', TFileArea),
        ('Path', ctypes.c_char*MAX_PATH),
        ('Reserved', BYTE*40),
    ]

class TWildcatServerPrivateFileVolume(PropertyStruct):
    _fields_ = [
        ('Name', ctypes.c_char*SIZE_SHORT_FILE_NAME),
        ('VolumeLabel', ctypes.c_char*SIZE_SHORT_FILE_NAME),
        ('UniqueFile', ctypes.c_char*MAX_PATH),
        ('Path', ctypes.c_char*MAX_PATH),
        ('Offline', BOOL),
        ('Reserved', BYTE*84),
    ]

