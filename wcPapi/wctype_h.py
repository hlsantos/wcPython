# Created by cpp2py on 2023-02-03 12:40:46.522995

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

class TSecurityName(PropertyStruct):
    _fields_ = [('Name', ctypes.c_char*SIZE_SECURITY_NAME)]
    def __str__(self):
        return self.Name

class TComputerName(PropertyStruct):
    _fields_ = [('Name', ctypes.c_char*SIZE_COMPUTER_NAME)]
    def __str__(self):
        return self.Name


class TShortFileName(PropertyStruct):
    _fields_ = [('Name', ctypes.c_char*SIZE_SHORT_FILE_NAME)]
    def __str__(self):
        return self.Name

class TDoorName(PropertyStruct):
    _fields_ = [('Name', ctypes.c_char*SIZE_DOOR_NAME)]
    def __str__(self):
        return self.Name

class CString(ctypes.c_char_p):
    def __init__(self, string=b''):
        super().__init__(string)
    def from_param(self):
        return self.encode()

class FILETIME(ctypes.Structure):
    _fields_ = [
        ('dwLowDateTime', DWORD),
        ('dwHighDateTime', DWORD),
    ]

class WIN32_FIND_DATA(PropertyStruct):
    _fields_ = [
        ('dwFileAttributes', DWORD),
        ('ftCreationTime', FILETIME),
        ('ftLastAccessTime', FILETIME),
        ('ftLastWriteTime', FILETIME),
        ('nFileSizeHigh', DWORD),
        ('nFileSizeLow', DWORD),
        ('dwReserved0', DWORD),
        ('dwReserved1', DWORD),
        ('cFileName', ctypes.c_char* MAX_PATH ),
        ('cAlternateFileName', ctypes.c_char* 14 ),
    ]

class TChannelMessage(ctypes.Structure):
    _fields_ = [
        ('Channel', DWORD),
        ('SenderId', DWORD),
        ('UserData', WORD),
        ('DataSize', WORD),
        ('Data', BYTE*MAX_CHANNEL_MESSAGE_SIZE),
    ]

class TMessageItem(PropertyStruct):
    _fields_ = [('Item', ctypes.c_char*80)]

class TPageMessage(PropertyStruct):
    _fields_ = [
        ('From', ctypes.c_char*28),
        ('message', TMessageItem*3),
        ('InviteToChat', BOOL),
    ]

class TChatMessage(PropertyStruct):
    _fields_ = [
        ('From', ctypes.c_char*28),
        ('Text', ctypes.c_char*256),
        ('Whisper', BYTE),
    ]

class TObjectName(PropertyStruct):
    _fields_ = [
        ('Status', DWORD),
        ('ObjectId', DWORD),
        ('Number', DWORD),
        ('Name', ctypes.c_char*MAX_PATH),
    ]

class TPackerRec(PropertyStruct):
    _fields_ = [
        ('Letter', DWORD),
        ('Description', ctypes.c_char*SIZE_PACKER_DESCRIPTION),
        ('Extension', ctypes.c_char*SIZE_EXTENSION),
        ('Packer', ctypes.c_char*SIZE_PACKER_COMMAND),
        ('Unpacker', ctypes.c_char*SIZE_PACKER_COMMAND),
    ]

class TWildcatTimeouts(PropertyStruct):
    _fields_ = [
        ('dwVersion', WORD),
        ('dwRevision', WORD),
        ('Web', DWORD),
        ('WebQues', DWORD),
        ('Telnet', DWORD),
        ('TelnetLogin', DWORD),
        ('Ftp', DWORD),
        ('wcPPP', DWORD),
        ('wcNAV', DWORD),
        ('Pop3', DWORD),
        ('Pop3Login', DWORD),
        ('FtpLogin', DWORD),
        ('FtpData', DWORD),
        ('Reserved', ctypes.c_char*76),
    ]

class tagTWildcatLogPeriod(IntEnum):
   wclogNone            = 0
   wclogHourly          = 1
   wclogDaily           = 2
   wclogWeekly          = 3
   wclogMonthly         = 4
   wclogUnlimitedSize   = 5
   wclogMaxSize         = 6
TWildcatLogPeriod = DWORD

class TWildcatLogOptions(ctypes.Structure):
    _fields_ = [
        ('EnableSessionTrace', BOOL),
        ('LogPeriod', TWildcatLogPeriod),
        ('dwMaxSize', DWORD),
        ('dwVerbosity', DWORD),
        ('Reserved', BYTE*16),
    ]

class THttpAuthOptions(ctypes.Structure):
    _fields_ = [
        ('AllowPlainText', BOOL),
        ('AllowPlainTextWithSSL', BOOL),
        ('AllowPlainMD5', BOOL),
        ('AllowDigest', BOOL),
        ('AllowWcChallenge', BOOL),
        ('RequireSSL', BOOL),
    ]

class TWildcatHttpd(PropertyStruct):
    _fields_ = [
        ('dwVersion', WORD),
        ('dwRevision', WORD),
        ('_CommonLogFile', BOOL),
        ('_DeutschIVW', BOOL),
        ('LogOptions', TWildcatLogOptions),
        ('dwOptions', DWORD),
        ('MaximumBandWidth', DWORD),
        ('SendBufferSize1K', DWORD),
        ('RcvdBufferSize1K', DWORD),
        ('TrackPerformance', BOOL),
        ('HttpAuth', THttpAuthOptions),
        ('EnablePCISession', BOOL),
        ('Reserved', ctypes.c_char*20),
    ]

class TWildcatSMTP(PropertyStruct):
    _fields_ = [
        ('dwVersion', WORD),
        ('dwRevision', WORD),
        ('port', DWORD),
        ('sendthreads', WORD),
        ('acceptthreads', WORD),
        ('dwOptions', DWORD),
        ('acceptonly', BOOL),
        ('retries', DWORD),
        ('retrywait', DWORD),
        ('smarthost', ctypes.c_char*52),
        ('sizelimit', DWORD),
        ('localonly', BOOL),
        ('MAPSRBL', BOOL),
        ('MAPSRBLServer', ctypes.c_char*52),
        ('ESMTP', BOOL),
        ('reqauth', BOOL),
        ('VRFY', BOOL),
        ('AllowRelay', BOOL),
        ('CheckRCPT', BOOL),
        ('EnableBadFilter', BOOL),
        ('RequireMX', BOOL),
        ('RequireHostMatch', BOOL),
    ]

class TWildcatNNTP(PropertyStruct):
    _fields_ = [
        ('dwVersion', WORD),
        ('dwRevision', WORD),
        ('dwPort', DWORD),
        ('dwOptions', DWORD),
        ('MaxCrossPost', DWORD),
        ('LogOptions', TWildcatLogOptions),
        ('Reserved', ctypes.c_char*80),
    ]

class TWildcatPOP3(PropertyStruct):
    _fields_ = [
        ('dwVersion', WORD),
        ('dwRevision', WORD),
        ('EnablePopBeforeSmtp', BOOL),
        ('dwPopBeforeSmtpTimeout', DWORD),
        ('dwOptions', DWORD),
        ('LogOptions', TWildcatLogOptions),
        ('MaximumBandWidth', DWORD),
        ('SendBufferSize1K', DWORD),
        ('RcvdBufferSize1K', DWORD),
        ('TrackPerformance', BOOL),
        ('Reserved', ctypes.c_char*64),
    ]

class TWildcatTelnet(PropertyStruct):
    _fields_ = [
        ('dwVersion', WORD),
        ('dwRevision', WORD),
        ('dwOptions', DWORD),
        ('LogOptions', TWildcatLogOptions),
        ('MaximumBandWidth', DWORD),
        ('SendBufferSize1K', DWORD),
        ('RcvdBufferSize1K', DWORD),
        ('TrackPerformance', BOOL),
        ('Reserved', ctypes.c_char*72),
    ]

class tagTFtpListTextFormat(IntEnum):
   listUnixFormat       = 0
   listMSDOSFormat      = 1
TFtpListTextFormat = DWORD

class TWildcatFTP(PropertyStruct):
    _fields_ = [
        ('dwVersion', WORD),
        ('dwRevision', WORD),
        ('AllowAnonymous', BOOL),
        ('ShowFileGroups', BOOL),
        ('UseUnderScore', BOOL),
        ('UseSingleAreaChange', BOOL),
        ('MaxAnonymousConnects', DWORD),
        ('LogOptions', TWildcatLogOptions),
        ('ListFormat', TFtpListTextFormat),
        ('dwOptions', DWORD),
        ('MaximumBandWidth', DWORD),
        ('SendBufferSize1K', DWORD),
        ('RcvdBufferSize1K', DWORD),
        ('TrackPerformance', BOOL),
        ('MaxConnects', DWORD),
        ('Reserved', ctypes.c_char*44),
    ]

class TMakewild(PropertyStruct):
    _fields_ = [
        ('Version', DWORD),
        ('BBSName', ctypes.c_char*SIZE_MAKEWILD_BBSNAME),
        ('SysopName', ctypes.c_char*MAX_USER_NAME),
        ('City', ctypes.c_char*SIZE_MAKEWILD_CITY),
        ('Phone', ctypes.c_char*SIZE_MAKEWILD_PHONE),
        ('FirstCall', ctypes.c_char*SIZE_MAKEWILD_FIRSTCALL),
        ('PacketId', ctypes.c_char*SIZE_MAKEWILD_PACKETID),
        ('RegString', ctypes.c_char*SIZE_MAKEWILD_REGSTRING),
        ('SystemAccess', DWORD),
        ('MaxLoginAttempts', DWORD),
        ('FreeFormPhone', BOOL),
        ('HideAnonFtpPassword', BOOL),
        ('LogonLanguagePrompt', BOOL),
        ('Assume8N1', BOOL),
        ('LoginAskLocation', BOOL),
        ('NewUserSecurity', ctypes.c_char*SIZE_SECURITY_NAME),
        ('DefaultExt', ctypes.c_char*SIZE_EXTENSION),
        ('ThumbnailFile', ctypes.c_char*SIZE_SHORT_FILE_NAME),
        ('OldDoorPath', ctypes.c_char*MAX_PATH),
        ('_EnableHttpProxy', BOOL),
        ('SmtpMaxAcceptLoad', DWORD),
        ('DateFormat', ctypes.c_char*24),
        ('TimeFormat', ctypes.c_char*24),
        ('DefaultDomain', ctypes.c_char*SIZE_DOMAIN_NAME),
        ('Reserved', ctypes.c_char*12),
        ('TelnetConfig', TWildcatTelnet),
        ('FTPConfig', TWildcatFTP),
        ('POP3Config', TWildcatPOP3),
        ('MAILLogOptions', TWildcatLogOptions),
        ('Reserved2', ctypes.c_char*32),
        ('Reserved1', ctypes.c_char*32),
        ('SMTPLogOptions', TWildcatLogOptions),
        ('NNTPConfig', TWildcatNNTP),
        ('AllowLogonEmail', BOOL),
        ('CaseSensitivePasswords', BOOL),
        ('MsgHeaderCaseMode', DWORD),
        ('SpamAllowAuth', BOOL),
        ('SMTPConfig', TWildcatSMTP),
        ('HttpdConfig', TWildcatHttpd),
        ('Timeouts', TWildcatTimeouts),
        ('DefaultColors', BYTE*28),
        ('ExcludeBulletins', DWORD*40),
        ('InstalledComponents', DWORD),
        ('_ResolveHostnames', BOOL),
        ('BuildDate', ctypes.c_char*16),
        ('DomainName', ctypes.c_char*SIZE_DOMAIN_NAME),
        ('WindowsCharset', BOOL),
        ('LogonUserNameOnly', BOOL),
    ]

class TWildcatComputerIpPort(ctypes.Structure):
    _fields_ = [
        ('dwPort', DWORD),
        ('dwIpAddress', DWORD),
    ]

class TComputerConfig(PropertyStruct):
    _fields_ = [
        ('Name', ctypes.c_char*SIZE_COMPUTER_NAME),
        ('DoorPath', ctypes.c_char*MAX_PATH),
        ('CgiPath', ctypes.c_char*MAX_PATH),
        ('HttpPort', DWORD),
        ('FtpPort', DWORD),
        ('WWWHostname', ctypes.c_char*80),
        ('Servers', DWORD),
        ('HttpProxyPort', DWORD),
        ('dwVersion', WORD),
        ('dwRevision', WORD),
        ('ipportHttp', TWildcatComputerIpPort),
        ('ipportFtp', TWildcatComputerIpPort),
        ('ipportPop3', TWildcatComputerIpPort),
        ('ipportTelnet', TWildcatComputerIpPort),
        ('ipportSmtp', TWildcatComputerIpPort),
        ('ipportNntp', TWildcatComputerIpPort),
        ('Reserved', BYTE*332),
        ('TelnetPort', DWORD),
        ('Pop3Port', DWORD),
    ]

class TLogonHours(ctypes.Structure):
    _fields_ = [
        ('day', DWORD*7),
    ]

class TSecurityProfile(PropertyStruct):
    _fields_ = [
        ('Name', ctypes.c_char*SIZE_SECURITY_NAME),
        ('ExpiredName', ctypes.c_char*SIZE_SECURITY_NAME),
        ('DisplayFileName', ctypes.c_char*SIZE_SHORT_FILE_NAME),
        ('DoorSysProfileName', ctypes.c_char*SIZE_SECURITY_NAME),
        ('MenuDisplaySet', ctypes.c_char*SIZE_SHORT_FILE_NAME),
        ('DailyTimeLimit', DWORD),
        ('PerCallTimeLimit', DWORD),
        ('VerifyPhoneInterval', DWORD),
        ('VerifyBirthdateInterval', DWORD),
        ('FailedInfoAction', DWORD),
        ('MaxDownloadCountPerDay', DWORD),
        ('DownloadRatioLimit', DWORD),
        ('MaxDownloadKbytesPerDay', DWORD),
        ('DownloadKbytesRatioLimit', DWORD),
        ('UploadTimeCredit', DWORD),
        ('ExpireDays', DWORD),
        ('PasswordOptions', WORD),
        ('PasswordExpireDays', WORD),
        ('FtpSpaceKbytes', DWORD),
        ('EmailDomainName', ctypes.c_char*SIZE_DOMAIN_NAME),
        ('MaximumLogons', DWORD),
        ('RestrictedHours', BOOL),
        ('LogonHours', TLogonHours),
    ]

class TConfDesc(PropertyStruct):
    _fields_ = [
        ('ObjectId', DWORD),
        ('Number', DWORD),
        ('Name', ctypes.c_char*SIZE_CONFERENCE_NAME),
        ('Reserved1', ctypes.c_char*16),
        ('ConferenceSysop', ctypes.c_char*MAX_USER_NAME),
        ('EchoTag', ctypes.c_char*SIZE_CONFERENCE_ECHOTAG),
        ('ReplyToAddress', ctypes.c_char*SIZE_USER_NAME),
        ('Distribution', ctypes.c_char*SIZE_USER_NAME),
        ('MailType', DWORD),
        ('PromptToKillMsg', BOOL),
        ('PromptToKillAttach', BOOL),
        ('AllowHighAscii', BOOL),
        ('AllowCarbon', BOOL),
        ('AllowReturnReceipt', BOOL),
        ('LongHeaderFormat', BOOL),
        ('AllowAttach', BOOL),
        ('ShowCtrlLines', BOOL),
        ('ValidateNames', DWORD),
        ('DefaultFileGroup', DWORD),
        ('MaxMessages', DWORD),
        ('DaysToKeepReceivedMail', DWORD),
        ('DaysToKeepPublicMail', DWORD),
        ('RenumberThreshold', DWORD),
        ('DaysToKeepExternalMail', DWORD),
        ('DeleteSMTPDelivered', BOOL),
        ('PublishAsLocalNewsGroup', BOOL),
        ('Options', DWORD),
        ('AuthorType', DWORD),
        ('UnixCreationTime', DWORD),
        ('Reserved', BYTE*6),
        ('DefaultFromAddress', ctypes.c_char*SIZE_USER_NAME),
        ('wVersion', WORD),
    ]

class TShortConfDesc(PropertyStruct):
    _fields_ = [
        ('ObjectId', DWORD),
        ('Name', ctypes.c_char*SIZE_CONFERENCE_NAME),
        ('MailType', DWORD),
    ]

class TConferenceGroup(PropertyStruct):
    _fields_ = [
        ('ObjectId', DWORD),
        ('Number', DWORD),
        ('Name', ctypes.c_char*SIZE_CONFERENCEGROUP_NAME),
        ('Reserved', BYTE*24),
    ]

class TFileArea(PropertyStruct):
    _fields_ = [
        ('ObjectId', DWORD),
        ('Number', DWORD),
        ('Name', ctypes.c_char*SIZE_FILEAREA_NAME),
        ('ExcludeFromNewFiles', BOOL),
        ('PromptForPasswordProtect', BOOL),
        ('FtpDirectoryName', ctypes.c_char*SIZE_FILEAREA_NAME),
        ('Options', DWORD),
    ]

class TShortFileArea(PropertyStruct):
    _fields_ = [
        ('ObjectId', DWORD),
        ('Name', ctypes.c_char*SIZE_FILEAREA_NAME),
    ]

class TFileGroup(PropertyStruct):
    _fields_ = [
        ('ObjectId', DWORD),
        ('Number', DWORD),
        ('Name', ctypes.c_char*SIZE_FILEGROUP_NAME),
        ('Reserved', BYTE*24),
    ]

class TDoorInfo(PropertyStruct):
    _fields_ = [
        ('ObjectId', DWORD),
        ('Name', ctypes.c_char*SIZE_DOOR_NAME),
        ('Batch', ctypes.c_char*SIZE_SHORT_FILE_NAME),
        ('Display', ctypes.c_char*SIZE_SHORT_FILE_NAME),
        ('DoorMenuIndex', DWORD),
        ('MultiUser', BOOL),
        ('SmallDoorSys', BOOL),
        ('DoorType', DWORD),
        ('Reserved', BYTE*36),
    ]

class TLanguageInfo(PropertyStruct):
    _fields_ = [
        ('Name', ctypes.c_char*SIZE_LANGUAGE_NAME),
        ('Description', ctypes.c_char*SIZE_LANGUAGE_DESCRIPTION),
        ('SubcommandChars', ctypes.c_char*MAX_LANGUAGE_SUBCOMMAND_CHARS),
        ('Reserved', BYTE*72),
    ]

class TShortModemProfile(PropertyStruct):
    _fields_ = [
        ('UserDefined', BOOL),
        ('Name', ctypes.c_char*SIZE_MODEM_NAME),
    ]

class TExtrabaudresultsItem(PropertyStruct):
    _fields_ = [('Item', ctypes.c_char*SIZE_MODEM_STRING)]

class TReserved5Item(PropertyStruct):
    _fields_ = [('Item', ctypes.c_char*SIZE_MODEM_STRING)]

class TModemProfile(PropertyStruct):
    _fields_ = [
        ('Version', DWORD),
        ('UserDefined', BOOL),
        ('Name', ctypes.c_char*SIZE_MODEM_NAME),
        ('InitBaud', DWORD),
        ('LockDTE', BOOL),
        ('HardwareFlow', BOOL),
        ('ExitOffHook', BOOL),
        ('CarrierDelay', DWORD),
        ('RingDelay', DWORD),
        ('DropDtrDelay', DWORD),
        ('PrelogDelay', DWORD),
        ('ResultDelay', DWORD),
        ('ResetDelay', DWORD),
        ('AnswerMethod', DWORD),
        ('EnableCallerId', DWORD),
        ('ResetCommand', ctypes.c_char*SIZE_MODEM_STRING),
        ('AnswerCommand', ctypes.c_char*SIZE_MODEM_STRING),
        ('Reserved1', ctypes.c_char*SIZE_MODEM_STRING),
        ('OffHook', ctypes.c_char*SIZE_MODEM_STRING),
        ('RingResult', ctypes.c_char*SIZE_MODEM_STRING),
        ('ConnectResult', ctypes.c_char*SIZE_MODEM_STRING),
        ('Reserved2', ctypes.c_char*SIZE_MODEM_STRING),
        ('ErrorFreeResult', ctypes.c_char*SIZE_MODEM_STRING),
        ('ExtraBaudResults', TExtrabaudresultsItem*10),
        ('ExtraBaudResultNumbers', DWORD*10),
        ('Reserved3', ctypes.c_char*SIZE_MODEM_STRING),
        ('InitCommand', ctypes.c_char*SIZE_MODEM_STRING),
        ('Reserved4', ctypes.c_char*SIZE_MODEM_STRING),
        ('Reserved5', TReserved5Item*3),
        ('Reserved6', ctypes.c_char*256),
        ('Reserved', BYTE*128),
    ]

class TNodeConfig(PropertyStruct):
    _fields_ = [
        ('CallTypesAllowed', DWORD),
        ('ModemName', ctypes.c_char*SIZE_MODEM_NAME),
        ('Computer', ctypes.c_char*SIZE_NODECONFIG_COMPUTER),
        ('Port', ctypes.c_char*SIZE_NODECONFIG_PORTNAME),
        ('PermanentLineID', DWORD),
        ('VirtualDoorPort', ctypes.c_char*8),
        ('NodeDisabled', BOOL),
        ('CarrierCheckMethod', DWORD),
        ('Reserved', BYTE*40),
    ]

class TServerState(PropertyStruct):
    _fields_ = [
        ('OwnerId', DWORD),
        ('Computer', ctypes.c_char*SIZE_NODECONFIG_COMPUTER),
        ('Port', ctypes.c_char*SIZE_SERVERSTATE_PORT),
        ('State', DWORD),
    ]

class TwcMenuItem(PropertyStruct):
    _fields_ = [
        ('Selection', ctypes.c_char*SIZE_MENUITEM_SELECTION),
        ('Description', ctypes.c_char*SIZE_MENUITEM_DESCRIPTION),
        ('Command', ctypes.c_char*SIZE_MENUITEM_COMMAND),
        ('Parameters', ctypes.c_char*SIZE_MENUITEM_COMMAND),
        ('Reserved', BYTE*4),
    ]

class TMenu(PropertyStruct):
    _fields_ = [
        ('ObjectId', DWORD),
        ('Description', ctypes.c_char*SIZE_MENU_DESCRIPTION),
        ('DisplayName', ctypes.c_char*SIZE_SHORT_FILE_NAME),
        ('Flags', DWORD),
        ('Count', DWORD),
        ('Items', TwcMenuItem*MAX_MENU_ITEMS),
        ('FastLoginChar', DWORD),
        ('SecurityEntryName', ctypes.c_char*SIZE_SECURITY_NAME),
        ('Reserved', BYTE*128),
    ]

class TUserInfo(PropertyStruct):
    _fields_ = [
        ('Id', DWORD),
        ('Name', ctypes.c_char*SIZE_USER_NAME),
        ('Title', ctypes.c_char*SIZE_USER_TITLE),
    ]

class TwcNodeInfo(PropertyStruct):
    _fields_ = [
        ('NodeStatus', DWORD),
        ('ServerState', DWORD),
        ('ConnectionId', DWORD),
        ('LastCaller', ctypes.c_char*SIZE_NODEINFO_LASTCALLER),
        ('User', TUserInfo),
        ('UserFrom', ctypes.c_char*SIZE_USER_FROM),
        ('UserPageAvailable', BOOL),
        ('Reserved1', BOOL),
        ('Activity', ctypes.c_char*SIZE_NODEINFO_ACTIVITY),
        ('Speed', ctypes.c_char*SIZE_NODEINFO_SPEED),
        ('TimeCalled', FILETIME),
        ('CurrentTime', FILETIME),
        ('Reserved2', DWORD),
        ('NodeNumber', DWORD),
        ('MinutesLeft', DWORD),
    ]

class TSecurityItem(PropertyStruct):
    _fields_ = [('Item', ctypes.c_char*SIZE_SECURITY_NAME)]

class TUser(PropertyStruct):
    _fields_ = [
        ('Status', DWORD),
        ('Info', TUserInfo),
        ('From', ctypes.c_char*SIZE_USER_FROM),
        ('Password', ctypes.c_char*SIZE_PASSWORD),
        ('Security', TSecurityItem*NUM_USER_SECURITY),
        ('Reserved1', DWORD),
        ('AllowMultipleLogins', BOOL),
        ('LogonHoursOverride', BOOL),
        ('RealName', ctypes.c_char*SIZE_USER_NAME),
        ('PhoneNumber', ctypes.c_char*SIZE_USER_PHONE),
        ('Company', ctypes.c_char*SIZE_USER_ADDRESS),
        ('Address1', ctypes.c_char*SIZE_USER_ADDRESS),
        ('Address2', ctypes.c_char*SIZE_USER_ADDRESS),
        ('City', ctypes.c_char*SIZE_USER_ADDRESS),
        ('State', ctypes.c_char*SIZE_USER_STATE),
        ('Zip', ctypes.c_char*SIZE_USER_ZIP),
        ('Country', ctypes.c_char*SIZE_USER_ADDRESS),
        ('Sex', DWORD),
        ('Editor', DWORD),
        ('HelpLevel', DWORD),
        ('Protocol', DWORD),
        ('TerminalType', DWORD),
        ('FileDisplay', DWORD),
        ('MsgDisplay', DWORD),
        ('PacketType', DWORD),
        ('LinesPerPage', DWORD),
        ('HotKeys', BOOL),
        ('QuoteOnReply', BOOL),
        ('SortedListings', BOOL),
        ('PageAvailable', BOOL),
        ('EraseMorePrompt', BOOL),
        ('Reserved3', BOOL),
        ('Language', ctypes.c_char*SIZE_LANGUAGE_NAME),
        ('LastCall', FILETIME),
        ('LastNewFiles', FILETIME),
        ('ExpireDate', FILETIME),
        ('FirstCall', FILETIME),
        ('BirthDate', FILETIME),
        ('Conference', DWORD),
        ('MsgsWritten', DWORD),
        ('Uploads', DWORD),
        ('TotalUploadKbytes', DWORD),
        ('Downloads', DWORD),
        ('TotalDownloadKbytes', DWORD),
        ('DownloadCountToday', DWORD),
        ('DownloadKbytesToday', DWORD),
        ('TimesOn', DWORD),
        ('TimeLeftToday', DWORD),
        ('MinutesLogged', DWORD),
        ('SubscriptionBalance', LONG),
        ('NetmailBalance', LONG),
        ('AccountLockedOut', BOOL),
        ('PreserveMimeMessages', BOOL),
        ('ShowEmailHeaders', BOOL),
        ('LastUpdate', FILETIME),
        ('SystemFlags', WORD),
        ('UserFlags', WORD),
        ('Validation', DWORD),
        ('PasswordOptions', WORD),
        ('PasswordExpireDays', WORD),
        ('PasswordChangeDate', FILETIME),
        ('AnonymousOnly', BOOL),
        ('AllowUserDirectory', BOOL),
    ]

class TFidoAddress(ctypes.Structure):
    _fields_ = [
        ('Zone', WORD),
        ('Net', WORD),
        ('Node', WORD),
        ('Point', WORD),
    ]

class TMsgHeader(PropertyStruct):
    _fields_ = [
        ('Status', DWORD),
        ('Conference', DWORD),
        ('Id', DWORD),
        ('Number', DWORD),
        ('From', TUserInfo),
        ('To', TUserInfo),
        ('Subject', ctypes.c_char*SIZE_MESSAGE_SUBJECT),
        ('PostedTimeGMT', FILETIME),
        ('MsgTime', FILETIME),
        ('ReadTime', FILETIME),
        ('Private', BOOL),
        ('Received', BOOL),
        ('ReceiptRequested', BOOL),
        ('Deleted', BOOL),
        ('Tagged', BOOL),
        ('Reference', DWORD),
        ('ReplyCount', DWORD),
        ('FidoFrom', TFidoAddress),
        ('FidoTo', TFidoAddress),
        ('FidoFlags', DWORD),
        ('MsgSize', DWORD),
        ('PrevUnread', DWORD),
        ('NextUnread', DWORD),
        ('Network', ctypes.c_char*SIZE_MESSAGE_NETWORK),
        ('AttachmentSFN', ctypes.c_char*SIZE_SHORT_FILE_NAME),
        ('AllowDisplayMacros', BOOL),
        ('AddedByUserId', DWORD),
        ('Exported', BOOL),
        ('MailFlags', DWORD),
        ('NextAttachment', DWORD),
        ('ReadCount', DWORD),
        ('Attachment', ctypes.c_char*SIZE_ATTACH_FILE_NAME),
        ('ExtraCRC32', DWORD),
        ('Reserved', DWORD*7),
    ]

class TFileComment(ctypes.Structure):
    _fields_ = [
        ('area', DWORD),
        ('id', DWORD),
    ]

class TFileRecord(PropertyStruct):
    _fields_ = [
        ('Status', DWORD),
        ('Area', DWORD),
        ('SFName', ctypes.c_char*SIZE_SHORT_FILE_NAME),
        ('Description', ctypes.c_char*SIZE_FILE_DESCRIPTION),
        ('Password', ctypes.c_char*SIZE_PASSWORD),
        ('FileFlags', DWORD),
        ('Size', DWORD),
        ('FileTime', FILETIME),
        ('LastAccessed', FILETIME),
        ('NeverOverwrite', BOOL),
        ('NeverDelete', BOOL),
        ('FreeFile', BOOL),
        ('CopyBeforeDownload', BOOL),
        ('Offline', BOOL),
        ('FailedScan', BOOL),
        ('FreeTime', BOOL),
        ('Downloads', DWORD),
        ('Cost', DWORD),
        ('Uploader', TUserInfo),
        ('UserInfo', DWORD),
        ('HasLongDescription', BOOL),
        ('PostTime', FILETIME),
        ('PrivateUserId', DWORD),
        ('FirstComment', TFileComment),
        ('Reserved', BYTE*24),
        ('Name', ctypes.c_char*SIZE_LONG_FILE_NAME),
        ('Reserved2', BYTE*100),
    ]

class TLongdescriptionItem(PropertyStruct):
    _fields_ = [('Item', ctypes.c_char*SIZE_FILE_LONGDESC)]

class TFullFileRecord(PropertyStruct):
    _fields_ = [
        ('Info', TFileRecord),
        ('StoredPath', ctypes.c_char*MAX_PATH),
        ('LongDescription', TLongdescriptionItem*MAX_FILE_LONGDESC_LINES),
    ]

class TFileSearchRecord(ctypes.Structure):
    _fields_ = [
        ('ref', DWORD),
        ('area', DWORD),
    ]

class TFileRecord5(PropertyStruct):
    _fields_ = [
        ('Status', DWORD),
        ('Area', DWORD),
        ('Name', ctypes.c_char*SIZE_SHORT_FILE_NAME),
        ('Description', ctypes.c_char*SIZE_FILE_DESCRIPTION),
        ('Password', ctypes.c_char*SIZE_PASSWORD),
        ('Reserved1', DWORD),
        ('Size', DWORD),
        ('FileTime', FILETIME),
        ('LastAccessed', FILETIME),
        ('NeverOverwrite', BOOL),
        ('NeverDelete', BOOL),
        ('FreeFile', BOOL),
        ('CopyBeforeDownload', BOOL),
        ('Offline', BOOL),
        ('FailedScan', BOOL),
        ('FreeTime', BOOL),
        ('Downloads', DWORD),
        ('Cost', DWORD),
        ('Uploader', TUserInfo),
        ('UserInfo', DWORD),
        ('HasLongDescription', BOOL),
        ('Reserved', BYTE*44),
    ]

class TLongdescriptionItem(PropertyStruct):
    _fields_ = [('Item', ctypes.c_char*SIZE_FILE_LONGDESC)]

class TFullFileRecord5(PropertyStruct):
    _fields_ = [
        ('Info', TFileRecord5),
        ('StoredPath', ctypes.c_char*MAX_PATH),
        ('LongDescription', TLongdescriptionItem*MAX_FILE_LONGDESC_LINES),
    ]

class TWordsItem(PropertyStruct):
    _fields_ = [('Item', ctypes.c_char*32)]

class TSpellSuggestList(PropertyStruct):
    _fields_ = [
        ('Words', TWordsItem*10),
    ]

class TSystemEventFileInfo(PropertyStruct):
    _fields_ = [
        ('FileArea', DWORD),
        ('ConnectionId', DWORD),
        ('TimeStamp', FILETIME),
        ('szFileName', ctypes.c_char*SIZE_LONG_FILE_NAME),
    ]

class TTextItem(ctypes.Structure):
    _fields_ = [('Item', WORD*80)]

class TSystemControlViewMsg(ctypes.Structure):
    _fields_ = [
        ('Line', WORD),
        ('Count', WORD),
        ('Text', TTextItem*3),
        ('CursorX', WORD),
        ('CursorY', WORD),
        ('MinutesLeft', WORD),
    ]

class TSystemPageNewMessage(PropertyStruct):
    _fields_ = [
        ('Conference', DWORD),
        ('ConferenceName', ctypes.c_char*SIZE_CONFERENCE_NAME),
        ('Id', DWORD),
        ('From', TUserInfo),
        ('Subject', ctypes.c_char*SIZE_MESSAGE_SUBJECT),
    ]

class TTextItem(PropertyStruct):
    _fields_ = [('Item', ctypes.c_char*SIZE_SYSTEMPAGE_TEXT)]

class TSystemPageInstantMessage(PropertyStruct):
    _fields_ = [
        ('From', ctypes.c_char*MAX_USER_NAME),
        ('Text', TTextItem*SIZE_SYSTEMPAGE_LINES),
        ('InviteToChat', BOOL),
    ]

class TWildcatService(PropertyStruct):
    _fields_ = [
        ('Name', ctypes.c_char*SIZE_SERVICE_NAME),
        ('Vendor', ctypes.c_char*SIZE_SERVICE_NAME),
        ('Version', DWORD),
        ('Address', DWORD),
        ('Port', DWORD),
    ]

class TConnectionInfo(PropertyStruct):
    _fields_ = [
        ('ConnectionId', DWORD),
        ('Node', DWORD),
        ('Time', DWORD),
        ('IdleTime', DWORD),
        ('Calls', DWORD),
        ('WindowsUserName', ctypes.c_char*80),
        ('Computer', ctypes.c_char*SIZE_COMPUTER_NAME),
        ('IpAddress', DWORD),
        ('ProgramName', ctypes.c_char*SIZE_PROGRAM_NAME),
        ('Domain', ctypes.c_char*SIZE_DOMAIN_NAME),
        ('Reserved1', BYTE*132),
        ('RefCount', DWORD),
        ('User', TUserInfo),
        ('HandlesOpen', DWORD),
        ('ChannelsOpen', DWORD),
        ('CurrentTid', DWORD),
        ('PeerAddress', DWORD),
        ('CallType', DWORD),
        ('Status', ctypes.c_char*SIZE_NODEINFO_ACTIVITY),
        ('Reserved', BYTE*60),
    ]

class TWildcatServerInfo(ctypes.Structure):
    _fields_ = [
        ('TotalCalls', DWORD),
        ('TotalUsers', DWORD),
        ('TotalMessages', DWORD),
        ('TotalFiles', DWORD),
        ('MemoryUsage', DWORD),
        ('MemoryLoad', DWORD),
        ('LastMessageId', DWORD),
        ('LastUserId', DWORD),
        ('ServerVersion', DWORD),
        ('ServerBuild', DWORD),
        ('Reserved', BYTE*84),
    ]

class TWildcatProcessTimes(ctypes.Structure):
    _fields_ = [
        ('ftSystem', FILETIME),
        ('ftStart', FILETIME),
        ('ftExit', FILETIME),
        ('ftKernel', FILETIME),
        ('ftUser', FILETIME),
        ('Reserved', BYTE*24),
    ]

class TWildcatSASLContext(PropertyStruct):
    _fields_ = [
        ('szSaslMethod', ctypes.c_char*SIZE_SASL_NAME),
        ('szChallenge', ctypes.c_char*256),
        ('dwOptions', DWORD),
        ('dwState', DWORD),
        ('dwUserid', DWORD),
        ('Data', BYTE*4096),
        ('szUsername', ctypes.c_char*SIZE_USER_NAME),
        ('szRealm', ctypes.c_char*MAX_PATH),
        ('szDomain', ctypes.c_char*MAX_PATH),
        ('szNonce', ctypes.c_char*MAX_PATH),
        ('szCNonce', ctypes.c_char*MAX_PATH),
        ('dwCNonceCount', DWORD),
        ('szURI', ctypes.c_char*MAX_PATH),
        ('szMethod', ctypes.c_char*20),
        ('szAlg', ctypes.c_char*64),
        ('szQop', ctypes.c_char*64),
    ]

class TwcOpenFileInfo(ctypes.Structure):
    _fields_ = [
        ('hFile', DWORD),
        ('dwSize', DWORD),
        ('ftWriteTime', FILETIME),
        ('dwAttributes', DWORD),
        ('dwSizeHigh', DWORD),
        ('reserved', BYTE*232),
    ]

class TWildcatServerGuid(PropertyStruct):
    _fields_ = [
        ('Time', FILETIME),
        ('Count', DWORD),
        ('szGuid', ctypes.c_char*MAX_PATH),
    ]

class TWildcatGeoIP(PropertyStruct):
    _fields_ = [
        ('has_data', BOOL),
        ('ipaddr', ctypes.c_char*16),
        ('city', ctypes.c_char*32),
        ('continent', ctypes.c_char*52),
        ('country', ctypes.c_char*52),
        ('latitude', ctypes.c_char*16),
        ('longitude', ctypes.c_char*16),
        ('metro_code', ctypes.c_char*16),
        ('tzone', ctypes.c_char*52),
        ('postal', ctypes.c_char*16),
        ('country_code', ctypes.c_char*8),
        ('region_code', ctypes.c_char*16),
        ('region_name', ctypes.c_char*52),
    ]

