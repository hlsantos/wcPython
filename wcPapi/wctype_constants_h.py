# Auto-created by cpp2constant.py on 2023-01-30 20:55:23.968817
# input file : include\wctype.h
# output file: wcpapi\wctype_constants_h.py

from enum import IntEnum

MAX_PATH                                 = 260

#+ Group: Client Structures

WILDCAT_FRAMEWORK_VERSION                = 1
WILDCAT_MKTG_VERSION                     = 8

WILDCAT_COMPONENT_ICP                    = 0x00000001
WILDCAT_COMPONENT_SSL                    = 0x00000002
WILDCAT_COMPONENT_PCI                    = 0x00000004

#!--------------------------------------------------------------
#! SPECIAL NOTE ABOUT LONG vs SHORT FILE NAMES
#!
#! - v5.5 - File Database Only
#!
#!    MAX_PATH long file name support was implemented in v5.5
#!    Database conversion was required since TFileRecord size
#!    was changed
#!
#! - v6.1.451.9 - Message Database Only (Native storage)
#!
#!   A 80 (79 + 1 null) semi-long file name was implemented
#!   in v6.1.451.9 for TMsgHeader.Attachment.  The old
#!   short file name field was renamed to TMsgHeader.AttachmentSFN
#!
#!   Developers can use a sizeof(TMsgHeader.Header) check to see
#!   what is the current size of the API.
#!
#!--------------------------------------------------------------

SIZE_SHORT_FILE_NAME                     = 16
SIZE_LONG_FILE_NAME                      = MAX_PATH
SIZE_ATTACH_FILE_NAME                    = 80
SIZE_PROGRAM_NAME                        = 64

CHANNEL_MESSAGE_HEADER_SIZE              = 12
NUM_USER_SECURITY                        = 10
MAX_CHANNEL_MESSAGE_SIZE                 = 500
MAX_FILE_LONGDESC_LINES                  = 15
MAX_LANGUAGE_SUBCOMMAND_CHARS            = 100
MAX_MENU_ITEMS                           = 40
MAX_USER_NAME                            = 28
SIZE_CALLTYPE                            = 32
SIZE_COMPUTER_NAME                       = 16
SIZE_CONFERENCEGROUP_NAME                = 32
SIZE_CONFERENCE_ECHOTAG                  = 64
SIZE_CONFERENCE_NAME                     = 60
SIZE_DOMAIN_NAME                         = 64
SIZE_DOOR_NAME                           = 40
SIZE_ENCODED_PASSWORD                    = 20
SIZE_EXTENSION                           = 4
SIZE_FILEAREA_NAME                       = 32
SIZE_FILEGROUP_NAME                      = 32
SIZE_FILE_DESCRIPTION                    = 76
SIZE_FILE_LONGDESC                       = 80
SIZE_LANGUAGE_DESCRIPTION                = 72
SIZE_LANGUAGE_NAME                       = 12
SIZE_MAKEWILD_BBSNAME                    = 52
SIZE_MAKEWILD_CITY                       = 32
SIZE_MAKEWILD_FIRSTCALL                  = 28
SIZE_MAKEWILD_PACKETID                   = 12
SIZE_MAKEWILD_PHONE                      = 28
SIZE_MAKEWILD_REGSTRING                  = 8
SIZE_MENUITEM_COMMAND                    = 48
SIZE_MENUITEM_DESCRIPTION                = 32
SIZE_MENUITEM_SELECTION                  = 16
SIZE_MENU_DESCRIPTION                    = 40
SIZE_MESSAGE_NETWORK                     = 12
SIZE_MESSAGE_SUBJECT                     = 72
SIZE_MODEM_NAME                          = 32
SIZE_MODEM_STRING                        = 64
SIZE_NODECONFIG_COMPUTER                 = 16
SIZE_NODECONFIG_PORTNAME                 = 16
SIZE_NODEINFO_ACTIVITY                   = 32
SIZE_NODEINFO_LASTCALLER                 = 48
SIZE_NODEINFO_SPEED                      = 8
SIZE_PASSWORD                            = 32
SIZE_SASL_NAME                           = 32
SIZE_SECURITY_NAME                       = 24
SIZE_SERVERSTATE_PORT                    = 80
SIZE_SERVICE_NAME                        = 64
SIZE_SYSTEMPAGE_LINES                    = 3
SIZE_SYSTEMPAGE_TEXT                     = 80
SIZE_USER_ADDRESS                        = 32
SIZE_USER_FROM                           = 32
SIZE_USER_NAME                           = 72
SIZE_USER_PHONE                          = 16
SIZE_USER_STATE                          = 16
SIZE_USER_TITLE                          = 12
SIZE_USER_ZIP                            = 12
SIZE_VOLUME_NAME                         = 16

#!--------------------------------------------------------------------
#! Access Profiles Class Object identifiers (COID).
#! COIDS are used to identify a group/class of objects.
#!--------------------------------------------------------------------

MASK_OBJECTCLASS                         = 0xFF000000
OBJECTCLASS_RIGHTS                       = 0x01000000
OBJECTCLASS_CONFERENCE                   = 0x02000000
OBJECTCLASS_CONFERENCEGROUP              = 0x03000000
OBJECTCLASS_FILEAREA                     = 0x04000000
OBJECTCLASS_FILEGROUP                    = 0x05000000
OBJECTCLASS_DOOR                         = 0x06000000
OBJECTCLASS_MENU                         = 0x07000000
OBJECTCLASS_CODE                         = 0x08000000
OBJECTCLASS_CLIENT                       = 0x09000000
OBJECTCLASS_SAPPHIRE_QUERY               = 0x0a000000
OBJECTCLASS_CHAT_CHANNEL                 = 0x0b000000
OBJECTCLASS_RADIUS_CLIENT                = 0x0c000000
OBJECTCLASS_DOMAINS                      = 0x0d000000

#!--------------------------------------------------------------------
#! Access Profiles Object identifiers (OID).
#! Use with GetObjectFlags() during user sessions to determine if
#! logged in user has access to specific functionalities identified
#! by the OIDs
#!--------------------------------------------------------------------

OBJECTID_BULLETINS_OPTIONAL              = OBJECTCLASS_RIGHTS + 1
OBJECTID_CHANGE_PHONE                    = OBJECTCLASS_RIGHTS + 2
OBJECTID_CHANGE_BIRTHDATE                = OBJECTCLASS_RIGHTS + 4
OBJECTID_QWK_ALLOW_BULLETINS             = OBJECTCLASS_RIGHTS + 5
OBJECTID_QWK_ALLOW_NEWS                  = OBJECTCLASS_RIGHTS + 6
OBJECTID_QWK_ALLOW_FILES                 = OBJECTCLASS_RIGHTS + 7
OBJECTID_QWK_DETAIL_DOWNLOAD             = OBJECTCLASS_RIGHTS + 8
OBJECTID_QWK_CHECK_DUPES                 = OBJECTCLASS_RIGHTS + 9
OBJECTID_QWK_SAVE_PACKETS                = OBJECTCLASS_RIGHTS + 10
OBJECTID_MASTER_SYSOP                    = OBJECTCLASS_RIGHTS + 11
OBJECTID_RATIO_ACTION                    = OBJECTCLASS_RIGHTS + 12
OBJECTID_ALLOW_FAST_LOGIN                = OBJECTCLASS_RIGHTS + 13
OBJECTID_ALLOW_OVERWRITE_FILES           = OBJECTCLASS_RIGHTS + 14
OBJECTID_SHOW_PASSWORD_FILES             = OBJECTCLASS_RIGHTS + 15
OBJECTID_ALLOW_OFFLINE_FILE_REQUESTS     = OBJECTCLASS_RIGHTS + 16
OBJECTID_ALLOW_UPLOAD_OVER_TIME          = OBJECTCLASS_RIGHTS + 17
OBJECTID_ALLOW_DOWNLOAD_OVER_TIME        = OBJECTCLASS_RIGHTS + 18
OBJECTID_ALLOW_UPLOADER_MODIFY_FILE      = OBJECTCLASS_RIGHTS + 20
OBJECTID_QWK_NETSTATUS                   = OBJECTCLASS_RIGHTS + 26
OBJECTID_SYSOP_READ_PRIVATE_MAIL         = OBJECTCLASS_RIGHTS + 27
OBJECTID_ALLOW_INTERNET_EMAIL            = OBJECTCLASS_RIGHTS + 28
OBJECTID_ALLOW_ANY_TELNET                = OBJECTCLASS_RIGHTS + 29
OBJECTID_ALLOW_ANY_FTP                   = OBJECTCLASS_RIGHTS + 30
OBJECTID_ALLOW_HTTP_PROXY                = OBJECTCLASS_RIGHTS + 31
OBJECTID_ALLOW_ALL_IP                    = OBJECTCLASS_RIGHTS + 32
OBJECTID_ALLOW_DEFAULT_IP                = OBJECTCLASS_RIGHTS + 33
OBJECTID_ALLOW_PPP                       = OBJECTCLASS_RIGHTS + 34
OBJECTID_IGNORE_TIME_ONLINE              = OBJECTCLASS_RIGHTS + 35
OBJECTID_IGNORE_IDLE_TIME                = OBJECTCLASS_RIGHTS + 36
OBJECTID_ALLOW_SMTP_AUTH                 = OBJECTCLASS_RIGHTS + 37
OBJECTID_ALLOW_NNTP_ACCESS               = OBJECTCLASS_RIGHTS + 38
OBJECTID_USERBIN_ACCESS                  = OBJECTCLASS_RIGHTS + 39
OBJECTID_ALLOW_FTP_ACCESS                = OBJECTCLASS_RIGHTS + 40
OBJECTID_ALLOW_WEB_ACCESS                = OBJECTCLASS_RIGHTS + 41
OBJECTID_ALLOW_TELNET_ACCESS             = OBJECTCLASS_RIGHTS + 42
OBJECTID_CHANGE_EMAILADDRESS             = OBJECTCLASS_RIGHTS + 43
OBJECTID_CHANGE_SMTPFORWARD              = OBJECTCLASS_RIGHTS + 44
OBJECTID_ALLOW_CC_GROUPS                 = OBJECTCLASS_RIGHTS + 45
OBJECTID_ALLOW_IMAP_AUTH                 = OBJECTCLASS_RIGHTS + 37 #// 46

OBJECTID_PROTOCOL_ACCESS                 = OBJECTCLASS_RIGHTS + 0x00010000 #// plus protocol number
OBJECTID_NODE_ACCESS                     = OBJECTCLASS_RIGHTS + 0x00020000 #// plus node number

OBJECTFLAGS_CONFERENCE_JOIN              = 0x00000001
OBJECTFLAGS_CONFERENCE_READ              = 0x00000002
OBJECTFLAGS_CONFERENCE_WRITE             = 0x00000004
OBJECTFLAGS_CONFERENCE_SYSOP             = 0x00000008

OBJECTFLAGS_FILEAREA_LIST                = 0x00000001
OBJECTFLAGS_FILEAREA_DOWNLOAD            = 0x00000002
OBJECTFLAGS_FILEAREA_UPLOAD              = 0x00000004
OBJECTFLAGS_FILEAREA_SYSOP               = 0x00000008

#!
#! MessageSearch() search attributes
#!

MSF_FORWARD                              = 0x00000001
MSF_FROM                                 = 0x00000002
MSF_TO                                   = 0x00000004
MSF_SUBJECT                              = 0x00000008
MSF_BODY                                 = 0x00000010

#!
#! wcBASIC Telnet connection options
#!

CONNECT_RAW                              = 0
CONNECT_TELNET_ASCII                     = 1
CONNECT_TELNET_7BIT                      = 2
CONNECT_TELNET_8BIT                      = 3

#!
#! User Database Function Keys
#!

UserIdKey                                = 0
UserNameKey                              = 1
UserLastNameKey                          = 2
UserSecurityKey                          = 3
UserLastCallKey                          = 4 #// 452.1f

#!
#! Files Database Function Keys
#!

FileNameAreaKey                          = 0
FileAreaNameKey                          = 1
FileAreaDateKey                          = 2
FileUploaderKey                          = 3
FileDateAreaKey                          = 4

#!
#! Channel message structure for Callbacks
#!

#!
#! Data structure for Paging Channel Events
#! passed via TChannelMessage.Data field
#!

#!
#! Data structure for Chat Channel Events
#! passed via TChannelMessage.Data field
#!

#!
#! TPackerRec is Obselete
#!

SIZE_PACKER_DESCRIPTION                  = 32
SIZE_PACKER_COMMAND                      = 40
MAX_PACKER_COUNT                         = 10

#!
#! System Operation Type
#!

saOpen                                   = 0 # Open, accounts created
saClosed                                 = 1 # Closed, accounts must exist
saClosedQuestionnaire                    = 2 # Closed, run questionaire
saClosedValidation                       = 3 # Closed, non-validated accounts Created

dusNone                                  = 0
dusAsk                                   = 1
dusAllow                                 = 2

mhcUpperCase                             = 0
mhcLowerCase                             = 1
mhcAsIs                                  = 2

#!
#! TMakeWild Structure (Main Configuration File)
#! See GetMakewild() function
#!

#!
#! LogPeriod options
#!

class TWildcatLogPeriod(IntEnum):
	wclogNone                                = 0
	wclogHourly                              = 1
	wclogDaily                               = 2 ## default for most things
	wclogWeekly                              = 3
	wclogMonthly                             = 4
	wclogUnlimitedSize                       = 5
	wclogMaxSize                             = 6

class TFtpListTextFormat(IntEnum):
	listUnixFormat                           = 0
	listMSDOSFormat                          = 1

pNone                                    = 0
pAscii                                   = 1
pXmodem                                  = 2
pXmodemCRC                               = 3
pXmodem1K                                = 4
pXmodem1KG                               = 5
pYmodem                                  = 6
pYmodemG                                 = 7
pKermit                                  = 8
pZmodem                                  = 9
NumProtocols                             = 10

fiaAllow                                 = 0
fiaLogoff                                = 1
fiaLockout                               = 2

ipfilterDeny                             = 0
ipfilterAllow                            = 1
ipfilterNone                             = 2
ipfilterBlock                            = 3

#!
#! TWildcatPOP3.dwOptions Bit Flags
#!

pop3MarkRcvd                             = 0x0001 #! Mark downloads as received
pop3HonorRR                              = 0x0002 #! Honor Return Request
pop3ResolveHost                          = 0x0020 #! 450.9b3 resolve host name

#!
#! TWildcatSMTP.dwOptions Bit Flags
#!

smtpBit0                                 = 0x0001 #! ignore this bit
smtpRcvdBin                              = 0x0002 #! Enable Receiver Bin
smtpNoMXOnce                             = 0x0004 #! Enable RFC821 No MX try once rule
smtpIpFilter                             = 0x0008 #! Enable IP Filter
smtpIncMXTries                           = 0x0010 #! MXs included in total attempts
smtpResolveHost                          = 0x0020 #! 450.9b3 resolve host name
smtpDisableETRN                          = 0x0040 #! 450.9b13
smtpAllowLocal                           = 0x0080 #! 451.3 Allow (auth) Local Email
smtpCheckHello                           = 0x0100 #! 451.4 Enable Helo/Ehlo Check
smtpEnableWCSAP                          = 0x0200 #! 451.5 Enable WCSAP
smtpEnableSFHook                         = 0x0400 #! 451.5 Enable SMTPFILTER Hook
smtpUsePort587                           = 0x0800 #! 451.6 Submit Protocol
smtpReadBadFilter                        = 0x1000 #! 452.7/453.1 Read only BadFilter (don't add)

#!
#! TWildcatFTP.dwOptions Bit Flags
#!

ftpBit0                                  = 0x0001 #! ignore this bit
ftpUnixFileAge                           = 0x0002 #! Use Unix-style File Age Range
ftpUseFtpLimit                           = 0x0004 #! Use Security Profile Limits
ftpCheckForDIZ                           = 0x0008 #! Check for DIZ in zip uploads (450.8)
ftpResolveHost                           = 0x0020 #! 450.9b3 resolve host name
ftpDisableIndex                          = 0x0040 #! 451.4e Disable Index Files

#!
#! Password Bit Options for Security Profile and User Record
#!

pwdChangeForce                           = 0x0001 #// Force change at next logon
pwdChangeDisallow                        = 0x0002 #// Do not allow password change
pwdChangeExpire                          = 0x0004 #// Force Change when pwd expires
pwdExpireLockout                         = 0x0008 #// Lockout account when pwd expires
pwdAttemptsLockout                       = 0x0010 #// (451.3) TBD. Lockout for max pwds. FUTURE.

#!
#! TWildcatNNTP.dwOptions Bit Flags
#!

nntpAllowAnony                           = 0x0001 #! Allow Anonymous
nntpResolveHost                          = 0x0020 #! resolve host name

#!
#! TWildcatHttpd.dwOptions Bit Flags
#!

httpEnableProxy                          = 0x0001 #! Enable http proxy
httpCommonLogFile                        = 0x0002 #! Enable Common Log File
httpDeutschIVW                           = 0x0004 #! Enable DeutschIVW
httpResolveHost                          = 0x0020 #! resolve host name
httpEnableChunking                       = 0x0008 #! resolve host name

#!
#! TWildcatTelnet.dwOptions Bit Flags
#!

telnetEnableRLogin                       = 0x0001 #! Enable rlogin
telnetResolveHost                        = 0x0020 #! resolve host name

#!
#! Structure and constants used for User's Logon Hours
#! Profile Data
#!

lh12am                                   = 0x00000001
lh1am                                    = 0x00000002
lh2am                                    = 0x00000004
lh3am                                    = 0x00000008
lh4am                                    = 0x00000010
lh5am                                    = 0x00000020
lh6am                                    = 0x00000040
lh7am                                    = 0x00000080
lh8am                                    = 0x00000100
lh9am                                    = 0x00000200
lh10am                                   = 0x00000400
lh11am                                   = 0x00000800
lh12pm                                   = 0x00001000
lh1pm                                    = 0x00002000
lh2pm                                    = 0x00004000
lh3pm                                    = 0x00008000
lh4pm                                    = 0x00010000
lh5pm                                    = 0x00020000
lh6pm                                    = 0x00040000
lh7pm                                    = 0x00080000
lh8pm                                    = 0x00100000
lh9pm                                    = 0x00200000
lh10pm                                   = 0x00400000
lh11pm                                   = 0x00800000
lhAllHours                               = 0x00FFFFFF
lhSun                                    = 0x01
lhMon                                    = 0x02
lhTue                                    = 0x04
lhWed                                    = 0x08
lhThu                                    = 0x10
lhFri                                    = 0x20
lhSat                                    = 0x40
lhAllDays                                = 0x7F
lhStartofWeek                            = lhSun #// based on Win32 Sun = 0
lhEndofWeek                              = lhSat

mtNormalPublicPrivate                    = 0
mtNormalPublic                           = 1
mtNormalPrivate                          = 2
mtFidoNetmail                            = 3
mtEmailOnly                              = 4
mtUsenetNewsgroup                        = 5
mtUsenetNewsgroupModerated               = 6
mtInternetMailingList                    = 7
# 449.4 02/24/01
mtFidoEcho                               = 8
mtListServeForum                         = 9
# 449.5 05/14/01
# mtUserEmail is similar to mtInternetMailingList for single user email
mtUserEmail                              = 10
mtEND                                    = 256

vnYes                                    = 0
vnNo                                     = 1
vnPrompt                                 = 2

#!
#! 449.5
#! The following maXXXXXXXXX bit flags are used in the
#! TConfDesc.Options field.
#!

maAllowMailSnooping                      = 0x00000001 #// non-sysop can snoop mail
maPreserveMime                           = 0x00000002 #// Conference raw storage
maAllowReplyOnly                         = 0x00000004 #// 451.6, User can reply only
maAllowMacros                            = 0x00000008 #// 452.1, Allow User macros
maAllowMsgDelete                         = 0x00000010 #// 452.2, Allow User delete
maAllowDupes                             = 0x00000020 #// 452.3, No Conference dupe checking

#!
#! 449.5
#! Option for TConfDesc.AuthorType field. This will define the
#! conference option for how the From field will be defined when
#! a message is created.
#!

authorDefaultName                        = 0 # default logic
authorForceUserName                      = 1 # force the user name
authorForceAliasName                     = 2 # force the user's alias (profile string)
authorAllowBoth                          = 3 # allow either the user or alias
authorAnonymousName                      = 4 # anonymous from name (any name allowed)

#!
#! 449.5
#! TFileArea.Options attributes
#!

faIsVolume                               = 0x00000001 #// Readonly: Set by server for GetFileArea()
faAllowPrivateFiles                      = 0x00000002 #// Allow files with PrivateUserId != 0
faAllowFolderWatch                       = 0x00000004 #// 450.7, Watch physical folders (see wcfwatch)
faAllowFileComments                      = 0x00000008 #// 453.2, Allow File Comments

dtGeneric16                              = 0
dtDoor32                                 = 1
dtDoorway                                = 2

LSC_YES                                  = 0
LSC_NO                                   = 1

aRing                                    = 0
aResult                                  = 1
aAutoAnswer                              = 2

CALLTYPE_LOCAL                           = 0x00000001 #// Local mode
CALLTYPE_DIALUP                          = 0x00000002 #// Ansi/TTY Direct Dialup Client
CALLTYPE_TELNET                          = 0x00000004 #// Ansi/TTY Telnet Client
CALLTYPE_FTP                             = 0x00000008 #// FTP client
CALLTYPE_HTTP                            = 0x00000010 #// Web client
CALLTYPE_FRONTEND                        = 0x00000020 #// Connection Hook
CALLTYPE_POP3                            = 0x00000040 #// POP3 client
CALLTYPE_SMTP                            = 0x00000080 #// !!! SMTP client
CALLTYPE_PPP                             = 0x00000100 #// !!! PPP client
CALLTYPE_RADIUS                          = 0x00000200 #// !!! RADIUS client
CALLTYPE_NNTP                            = 0x00000400 #// !!! NNTP client
CALLTYPE_HTTPS                           = 0x00000800 #// !!! HTTPS client (v5.5.450.3)
CALLTYPE_IMAP                            = 0x00001000 #// !!! IMAP client

ccAuto                                   = 0
ccRLSD                                   = 1
ccDSR                                    = 2

SERVERSTATE_OFFLINE                      = 0 #// remove server from list
SERVERSTATE_DOWN                         = 1 #// red
SERVERSTATE_REFUSE                       = 2 #// yellow
SERVERSTATE_UP                           = 3 #// green

MENU_TOPLEVEL                            = 0x00000002

clSessionNone                            = 0
clSessionUser                            = 1
clSessionSystem                          = 2
clSessionConfig                          = 3

nsDown                                   = 0
nsUp                                     = 1
nsSigningOn                              = 2
nsLoggedIn                               = 3

ucstNone                                 = 0
ucstPersonal                             = 1
ucstPersonalAll                          = 2
ucstAll                                  = 3

ucstMask                                 = 0x0F
ucfReserved1                             = 0x10
ucfReserved2                             = 0x20
ucfReserved3                             = 0x40
ucfAllAttach                             = 0x80

sNotDisclosed                            = 0
sMale                                    = 1
sFemale                                  = 2

ePrompt                                  = 0
eLine                                    = 1
eFullScreen                              = 2

hlNovice                                 = 0
hlRegular                                = 1
hlExpert                                 = 2

ttAuto                                   = 0
ttTTY                                    = 1
ttAnsi                                   = 2

fdSingle                                 = 0
fdDouble                                 = 1
fdFull                                   = 2
fdAnsi                                   = 3

mdScroll                                 = 0
mdClear                                  = 1
mdKeepHeader                             = 2

ptText                                   = 0
ptQwk                                    = 1
ptOPX                                    = 2

#!
#! User validation states for ssClosedValidation setup
#!

vsNone                                   = 0 # No validation required
vsValidationRequired                     = 1 # Validation required
vsPrevalidated                           = 2 # User has been prevalidated
vsValidated                              = 3 # User is validated

#!
#! The following mfXXXXXXXXX bit flags are used in the
#! TMsgHeader.MailFlags field.  Bits are defined as required
#! for unique/special mail processing.
#!

mfPOP3Received                           = 0x01000000 #// msg was received by a POP3 client
mfReceiptCreated                         = 0x02000000 #// Return Receipt was created
mfSmtpDelivered                          = 0x04000000 #// Message was sent by smtp
mfNNTPPost                               = 0x08000000 #// Message was posted by wcNNTP
mfIMAPPost                               = 0x10000000 #// Message was posted by wcIMAP
mfMimeSaved                              = 0x00000001 #// Mime Preserved
mfNoDupeChecking                         = 0x00000002 #// No dupe checking when adding msg (450.6)
mfNoReplying                             = 0x00000004 #// No Comments/Replies allowed (451.4)

ffAbortedUpload                          = 0x00000001 #// signifies incomplete file.
ffAllowFileComments                      = 0x00000002 #// 453.2, allows file comments

#! 453.2
#! File Comment
#!

#!
#! TFileRecord
#!

#!
#! TFullFileRecord
#!

#!---------------------------------------------------------
#! 454.8
#! TFileSearchRecord is a helper structure to be used with the
#! SDK function, FileSearch().  FileSearch() returns an array
#! of TFileSearchRecord representing the file area and file
#! database record number.
#!---------------------------------------------------------

#!---------------------------------------------------------
#! TFullFileRecord5 and TFileRecord5 is made available
#! here for SDK java/foxpro conversion purposes only
#!---------------------------------------------------------

#!---------------------------------------------------------

#!
#! System.Control or System.Control.# Signals
#!

SC_WATCH_REQUEST                         = 0 #// Used by WcView Monitor
SC_DISPLAY_UPDATE                        = 1 #// Used by WcView Monitor
SC_PUSH_KEY                              = 2 #// Used by WcView Monitor
SC_SECURITY_CHANGE                       = 3 #// user security changed
SC_DISCONNECT                            = 4 #// disconnect the user
SC_TIME_CHANGE                           = 5 #// user time online changed
SC_USER_RECORD_CHANGE                    = 6 #// user record was updated

#!
#! System.Page Signals
#!

SP_USER_PAGE                             = 0 #// page user (send short message)
SP_SYSOP_CHAT                            = 1 #// sysop chat request
SP_NEW_MESSAGE                           = 2 #// signal user of new direct message
SP_ALT_NUMBER_FILE                       = 3 #// display disp\alt##.bbs

#!
#! System.Event Signals: File Database Signals
#!

SE_FILE_UPLOAD                           = 10 #// file uploaded
SE_FILE_DOWNLOAD                         = 11 #// file downloaded
SE_FILE_DELETE                           = 12 #// file deleted
SE_FILE_UPDATE                           = 13 #// file was updated/moved

#!
#! System.Event Signals: Miscellaneous Client Control Signals
#! Note: Currently, there is no implementation. However, the
#! signals are defined to begin a standard signal number set.
#!

SE_SHUTDOWN_REQUEST                      = 20 #// request to shutdown
SE_RESTART                               = 21 #// request to restart
SE_CONFIG_CHANGE                         = 22 #// Makewild has changed, minimum
SE_POPCONNECT                            = 23 #// POP3 Client has connected, 450.3

#!
#! System.Event Signals: Server Status Change
#!

SE_SERVER_STATE_CHANGE                   = 30 #// server state has changed
SE_NODE_STATE_CHANGE                     = 31 #// node state has changed

#!
#! System.MailServer Signals: This channel is specifically
#! designed for events between wcmail/wcsmtp and configuration
#! components so that wcmail/wcsmtp can automatically reread
#! internal data.  NOTE: wcSMTP port info changes requires
#! a restart. Only non-essential data is reread
#!

SE_MAILSERVER_UPDATE                     = 40 #// signals for wcmail/wcsmtp, 450.6

#!
#! Data Structure used for SE_FILE_xxxxxx channel signals.
#!

#!
#! Structure used by WCVIEW to display screen data sent by
#! Host clients.  WCVIEW will send SC_WATCH_REQUEST to clients
#! asking them to provide screen data. If the clients are listening,
#! they can fill in the structure and send the data with the
#! SC_DISPLAY_UPDATE channel signal which will then signal WCVIEW
#! to update its display screens.
#!

#!
#! Data Structure used for SP_xxxxxx channel signals
#!

#!
#! Data Structure used for instant messages, channel "System.Page"
#!

#!
#! Structure for Wildcat! Service Creations
#!

#!
#! Structure for Connection Information
#! Set GetConnectionInfo() SDK function
#!

#!
#! Structure for GetWildcatServerInfo() function
#! Combines multiple server calls to get server totals in 1 call
#!

#!
#! v5.5.450.3
#! Structure for WcGetProcessTimes()
#! Returns server process running times information
#!

#! v5.5.450.3
#! Options and structures for Wildcat! SASL Authentication functions.
#!

WCSASL_SUCCESS                           = 0
WCSASL_AUTH_OK                           = WCSASL_SUCCESS
WCSASL_AUTH_FAIL                         = 1
WCSASL_INVALID_METHOD                    = 2
WCSASL_GET_RESPONSE                      = 3
WCSASL_GET_PASSWORD                      = 4
WCSASL_LOOKUPUSER                        = 5

#!
#! TWildcatSASLContext.dwOptions Bit Flags
#!

saslTranslate                            = 0x00000001 #! Undot user name
saslTranslateBoth                        = 0x00000011 #! Check Dot/Undot name

#!
#! TWildcatSASLContext is used to store any context specific
#! data we need in SASL based connections
#!

#! v6.0.451.2
#! Structure for wcCreateFileEx() function
#!

#! v6.3.453.5
#! Structure for WcGetWildcatServerGuid() function
#!

#!
#! v7.0.454.6
#! Structure for WcGetGeoIP()
#!

