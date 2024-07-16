import ctypes
import os

UINT8 = ctypes.c_uint8
INT16 = ctypes.c_int16
UINT16 = ctypes.c_uint16
INT32 = ctypes.c_int32
UINT32 = ctypes.c_uint32
INT64 = ctypes.c_int64
UINT64 = ctypes.c_uint64


class TRsouresNum(ctypes.Structure):
    _fields_ = [("terminalexist", INT16),
                ("axNum", INT16),
                ("diNum", INT16),
                ("doNum", INT16),
                ("adNum", INT16),
                ("daNum", INT16),
                ("encNum", INT16)]


class TMtPara(ctypes.Structure):
    _fields_ = [("bgVel", ctypes.c_double),
                ("maxVel", ctypes.c_double),
                ("maxAcc", ctypes.c_double),
                ("maxDec", ctypes.c_double),
                ("maxJerk", ctypes.c_double),
                ("stopDec", ctypes.c_double),
                ("eStopDec", ctypes.c_double)]


class TAxAttriPara(ctypes.Structure):
    _fields_ = [("arrivalBand", INT16),
                ("arrivalTime", INT16),
                ("errorLmt", INT32),
                ("softPosLimitPos", INT32),
                ("softNegLimitPos", INT32)]


class TAxCheckEn(ctypes.Structure):
    _fields_ = [("alarmEn", INT16),
                ("softLmtEn", INT16),
                ("hwLmtEn", INT16),
                ("errorLmtEn", INT16)]


class TSamplePara(ctypes.Structure):
    _fields_ = [("interval", INT16),
                ("trigType", INT16),
                ("delay", INT16),
                ("diNo", INT16),
                ("diLevel", INT16)]


class THomingPara(ctypes.Structure):
    _fields_ = [("homeMethod", INT16),
                ("offset", INT32),
                ("highVel", UINT32),
                ("lowVel", UINT32),
                ("acc", UINT32),
                ("overtime", UINT32),
                ("posSrc", INT16)]


class THomingParaInUint(ctypes.Structure):
    _fields_ = [("homeMethod", INT16),
                ("offset", ctypes.c_double),
                ("highVel", ctypes.c_double),
                ("lowVel", ctypes.c_double),
                ("acc", ctypes.c_double),
                ("overtime", UINT32),
                ("posSrc", INT16)]


class TCrdAdvParam(ctypes.Structure):
    _fields_ = [("userVelMode", INT16),
                ("transMode", INT16),
                ("noDataProtect", INT16),
                ("circAccChangeEn", INT16),
                ("noCoplaneCircOptm", INT16),
                ("turnCoef", ctypes.c_double),
                ("tol", ctypes.c_double)]


class TGearParam(ctypes.Structure):
    _fields_ = [("masterScale", ctypes.c_double),
                ("slaveScale", ctypes.c_double),
                ("masterNo", INT16),
                ("masterType", INT16),
                ("dirMode", INT16),
                ("masterSlopeDis", INT32)]


class TEventIO(ctypes.Structure):
    _fields_ = [("inType", INT16 * 2),
                ("inPortNo", INT16 * 2),
                ("inInvert", INT16 * 2),
                ("inOperator", INT16),
                ("outType", INT16),
                ("outPortNo", INT16),
                ("outInvert", INT16),
                ("activeType", INT16),
                ("triggerType", INT16),
                ("delayTime", INT16)]


class TEventDiMotion(ctypes.Structure):
    _fields_ = [("inType", INT16),
                ("inPortNo", INT16),
                ("motionAxNo", INT16),
                ("delay", INT16),
                ("motionType", INT16),
                ("triggerType", INT16),
                ("invertBit", INT16),
                ("tgtPos", ctypes.c_double),
                ("tgtVel", ctypes.c_double),
                ("acc", ctypes.c_double),
                ("dec", ctypes.c_double)]


class TEventCompareOut(ctypes.Structure):
    _fields_ = [("inType", INT16),
                ("portNo", INT16),
                ("outPortNo", INT16),
                ("outVal", INT16),
                ("outType", INT16),
                ("cmpType", INT16),
                ("pulseWidth", INT16),
                ("comparePos", ctypes.c_double)]


class TMultiCmpData(ctypes.Structure):
    _fields_ = [("compareData", INT32 * 3)]


class TSlaveInfo(ctypes.Structure):
    _fields_ = [("device_type", UINT16),
                ("vendor_id", UINT32),
                ("product_code", UINT32),
                ("revisionNo", UINT32),
                ("axis_num", UINT16),
                ("actStation", INT16),
                ("aliasNo", UINT32),
                ("opMode", UINT16)]


class TMasterInfo(ctypes.Structure):
    _fields_ = [("sysHwCfg", UINT16),
                ("cycleTime", UINT32),
                ("alias_mode", UINT16),
                ("stationCnt", UINT16),
                ("svCnt", UINT16),
                ("ioCnt", INT16),
                ("aioCnt", UINT16),
                ("ptCnt", INT16),
                ("glCnt", UINT16),
                ("pdolen", UINT32)]


class PdoEntry_t(ctypes.Structure):
    _fields_ = [("Index", ctypes.c_ushort),
                ("SubIndex", ctypes.c_ubyte),
                ("DevType", ctypes.c_ubyte),
                ("BitOfs", ctypes.c_short),
                ("BitLen", ctypes.c_uint)]


MAX_SL_PDO_ENTRY = 128  # 最大的从站的PDO个数
MAX_GEN_SL_CNT = 32  # 最大的自由协议从站的个数opmode=1


class SlCfg_t(ctypes.Structure):
    _fields_ = [("active", ctypes.c_short),
                ("sl_idx", ctypes.c_short),
                ("RxPdoOfs", ctypes.c_short),
                ("TxPdoOfs", ctypes.c_short),
                ("RxPdoLen", ctypes.c_ushort),
                ("TxPdoLen", ctypes.c_ushort),
                ("RxPdoCnt", ctypes.c_ushort),
                ("TxPdoCnt", ctypes.c_ushort),
                ("RxPdo_entry_list", PdoEntry_t * MAX_SL_PDO_ENTRY),
                ("TxPdo_entry_list", PdoEntry_t * MAX_SL_PDO_ENTRY)]


MAX_CARD_NUM = 4

# ECAT板卡主站状态定义
# 说明：以下枚举针对IMC_GetECATMasterSts函数
EC_MASTER_IDLE = 0  # EtherCat主站尚未初始化
EC_MASTER_INIT = 1  # EtherCat主站初始化
EC_MASTER_SCAN_SLAVE = 2  # EtherCat主站正在扫描从站设备
EC_MASTER_SCAN_SLAVE_END = 3  # EtherCat主站扫描从站设备结束
EC_MASTER_SCAN_MODULES = 4  # EtherCat主站正在扫描从站设备MODULES
EC_MASTER_SCAN_MODULES_END = 5  # EtherCat主站扫描从站设备MODULES结束
EC_MASTER_OP = 6  # EtherCat主站进入OP状态
EC_MASTER_ERR = 7  # EtherCat主站链路状态有错误

# ECAT板卡从站状态定义
# IMC_GetSlaveReqSts函数
EC_SLAVE_STATE_UNKNOWN = 0x00  # EtherCat从站在未知状态
EC_SLAVE_STATE_INIT = 0x01  # EtherCat从站在初始状态
EC_SLAVE_STATE_PREOP = 0x02  # EtherCat从站在PREOP状态
EC_SLAVE_STATE_BOOT = 0x03  # EtherCat从站在BOOT状态
EC_SLAVE_STATE_SAFEOP = 0x04  # EtherCat从站在SAVEOP状态
EC_SLAVE_STATE_OP = 0x08  # EtherCat从站在OP状态
EC_SLAVE_STATE_ACK_ERR = 0x10  # EtherCat从站有错误

# EcatErrorCode定义
# 说明：以下宏定义针对IMC_GetEcatErrCode函数, 其他为内部错误
ERROR_CODE_NO_SUCH_SLAVE = 0x0003  # 配置阶段，没有这个从站,处理方法：检查从站是否掉线，重新扫描配置
ERROR_CODE_INVALID_PDO = 0x0004  # 配置阶段，非法PDO,处理方法：检查从站厂家是否更新xml配置文件，与汇川默认配置不一致
ERROR_CODE_INVALID_SDO = 0x0005  # 配置阶段，非法SDO,处理方法：检查从站厂家是否更新xml配置文件，与汇川默认配置不一致
ERROR_CODE_INVALID_ENTRY = 0x0006  # 配置阶段，非法ENTRY,处理方法：检查从站厂家是否更新xml配置文件，与汇川默认配置不一致
ERROR_CODE_PASECFGFAIL = 0x000D  # 解析XML设备配置失败,处理方法：设备配置文件已经被破坏，重新扫描配置
ERROR_CODE_CFGREGISTFAIL = 0x0015  # 配置reg失败,处理方法：检查从站厂家是否更新xml配置文件，与汇川默认配置不一致
ERROR_CODE_CFGDIFFONLINE = 0x0016  # 在线从站与配置不一致,处理方法：检查从站是否掉线，重新扫描配置
ERROR_CODE_AXIS_NUM_BEYOND = 0x0017  # 轴配置数量超过板卡最大支持轴数；
ERROR_CODE_SLAVE_OFFLINE = 0x001a  # 从站掉线错误，高8位为从站号，即bit[15:8]-轴号,处理方法：检查从高8位数字开始从站是否掉线，或者重新扫描配置
ERROR_CODE_SDOBF_NONECAT = 0x001b  # SDO缓冲区收到非ECAT帧错误,处理方法：检查线路是否接错，是否有其他非Ethercat设备接入
ERROR_CODE_PORT0_NOTLINK = 0x001c  # 端口未接ECAT设备错误,处理方法：检查板卡端线路是否正常接线，是否接线不可靠
ERROR_CODE_SET_CYCLETIME_PARA_ERR = 0x001e  # 设置周期时间参数错误,处理方法：错误的DC时钟配置，只支持125us,250us,500us,125us,
# 1000us,2000us,4000us,8000us周期
ERROR_CODE_COE_SDO_INIT_ERR = 0x001f  # 在初始化阶段coe配置错误,处理方法：检查从站厂家是否更新xml配置文件，与汇川默认配置不一致；或者可能例如RTU模块配置错误
ERROR_CODE_SLAVE_STATE_ERR = 0x0020  # 从站状态错误，高8位为轴号，即bit[15:8]-轴号,处理方法：检查从高8位数字从站状态，检查从站设备异常原因。
ERROR_CODE_SLAVE_SII_ERR = 0x0037  # E2ROM 信息有误,处理方法：一般为从站保存的e2rom信息有误，可以使用twincat确认并联系厂家。
ERROR_CODE_SLAVE_NUM_BEYOND = 0x003b  # 从站在线超过最大64个站

# AbortCode定义
# 说明：以下宏定义针对IIMC_GetEcatSdo\IMC_SetEcatSdo函数
ABORT_CODE1 = 0x05030000  # 从站Toggle bit 没有变化
ABORT_CODE2 = 0x05040000  # SDO 访问超时
ABORT_CODE3 = 0x05040001  # 客户端/服务器 命令非法或未知
ABORT_CODE4 = 0x05040005  # 内存溢出
ABORT_CODE5 = 0x06010000  # 不支持访问该对象
ABORT_CODE6 = 0x06010001  # 尝试去读一个只写对象
ABORT_CODE7 = 0x06010002  # 尝试去写一个只读对象
ABORT_CODE8 = 0x06020000  # 对象字典中不存在该对象
ABORT_CODE9 = 0x06040041  # 该对象不能映射成PDO
ABORT_CODE10 = 0x06040042  # 对象映射成PDO超出 PDO长度
ABORT_CODE11 = 0x06040043  # 通用参数非法
ABORT_CODE12 = 0x06040047  # 设备内不兼容
ABORT_CODE13 = 0x06060000  # 由于硬件原因访问失败
ABORT_CODE14 = 0x06070010  # 数据类型不匹配，长度参数
ABORT_CODE15 = 0x06070012  # 数据类型不匹配，长度太大
ABORT_CODE16 = 0x06070013  # 数据类型不匹配，长度太小
ABORT_CODE17 = 0x06090011  # 该对象子索引不存在
ABORT_CODE18 = 0x06090030  # 参数超出范围
ABORT_CODE19 = 0x06090031  # 参数超出范围太大
ABORT_CODE20 = 0x06090032  # 参数超出范围太小
ABORT_CODE21 = 0x06090036  # 最大值小于最小值
ABORT_CODE22 = 0x08000000  # 一般错误
ABORT_CODE23 = 0x08000020  # 数据不能被传输或被保存
ABORT_CODE24 = 0x08000021  # 数据不能被传输或被保存由于本地控制
ABORT_CODE25 = 0x08000022  # 数据不能被传输或被保存由于当前状态
ABORT_CODE26 = 0x08000023  # 缺乏对象字典或者对象字典创建失败

# 伺服操作模式定义
TQ_OP_MODE = 4  # TQ模式
HM_OP_MODE = 6  # 回零模式
CSP_OP_MODE = 8  # CSP模式
CSV_OP_MODE = 9  # CSV模式
CST_OP_MODE = 10  # CST模式

# 回零模式定义
HOMING_MODE_CIA = 0  # CIA402回零模式
HOMING_MODE_TORQ = 1  # 力矩回零模式
HOMING_MODE_ECAT_CSP = 2  # CSP探针回零模式

# 回零状态定义
HOME_IN_PROGRESS = 0  # 正在回零中
HOME_INTERRUPTED_OR_NOT_START = 1  # 回零中断或者没有开始启动
HOME_ATTAINED_BUT_NOT_REACH = 2  # 回零结束，但没有到设定的目标位置
HOME_SUCESS = 3  # 回零成功
HOME_ERR_VEL_NOT_ZERO = 4  # 回零中发生错误，同时速度不为0
HOME_ERR_VEL_ZERO = 5  # 回零中发生错误，同时速度为0

# 端子板专用IO的定义
SPECIAL_IO_RDY = 0  # 准备完成信号
SPECIAL_IO_ARRIV = 1  # 到位信号
SPECIAL_IO_ALARM = 2  # 报警信号
SPECIAL_IO_POSLMT = 3  # 正限位信号
SPECIAL_IO_NEGLMT = 4  # 负限位信号
SPECIAL_IO_CLR = 5  # 清除报警信号
SPECIAL_IO_SV = 6  # 伺服使能信号
SPECIAL_IO_HOME = 7  # 回零输入信号
SPECIAL_IO_INDEX = 8  # 电机Z相信号

# 端子板回零方法定义
HOME_NLIMT_ZINDEX = 1  # 负限位+Z信号
HOME_PLIMT_ZINDEX = 2  # 正限位+Z信号
HOME_PHOME_FEDGE_ZINDEX = 3  # 正原点开关下降沿+Z信号
HOME_PHOME_REDGE_ZINDEX = 4  # 正原点开关上升沿+Z信号
HOME_NHOME_FEDGE_ZINDEX = 5  # 负原点开关下降沿+Z信号
HOME_NHOME_REDGE_ZINDEX = 6  # 负原点开关上升沿+Z信号
HOME_PLIMT_PHOME_FEDGE_ZINDEX = 7  # 正限位+正原点开关下降沿+Z信号
HOME_PLIMT_PHOME_REDGE_ZINDEX = 8  # 正限位+正原点开关上升沿+Z信号
HOME_PLIMT_NHOME_REDGE_ZINDEX = 9  # 正限位+负原点开关上升沿+Z信号
HOME_PLIMT_NHOME_FEDGE_ZINDEX = 10  # 正限位+负原点开关下降沿+Z信号
HOME_NLIMT_NHOME_FEDGE_ZINDEX = 11  # 负限位+负原点开关下降沿+Z信号
HOME_NLIMT_NHOME_REDGE_ZINDEX = 12  # 负限位+负原点开关上升沿+Z信号
HOME_NLIMT_PHOME_REDGE_ZINDEX = 13  # 负限位+正原点开关上升沿+Z信号
HOME_NLIMT_PHOME_FEDGE_ZINDEX = 14  # 负限位+正原点开关下降沿+Z信号
HOME_NLIMT = 17  # 负限位
HOME_PLIMT = 18  # 正限位
HOME_PHOME_FEDGE = 19  # 正原点开关下降沿
HOME_PHOME_REDGE = 20  # 正原点开关上升沿
HOME_NHOME_FEDGE = 21  # 负原点开关下降沿
HOME_NHOME_REDGE = 22  # 负原点开关上升沿
HOME_PLIMT_PHOME_FEDGE = 23  # 正限位+正原点开关下降沿
HOME_PLIMT_PHOME_REDGE = 24  # 正限位+正原点开关上升沿
HOME_PLIMT_NHOME_REDGE = 25  # 正限位+负原点开关上升沿
HOME_PLIMT_NHOME_FEDGE = 26  # 正限位+负原点开关下降沿
HOME_NLIMT_NHOME_FEDGE = 27  # 负限位+负原点开关下降沿
HOME_NLIMT_NHOME_REDGE = 28  # 负限位+负原点开关上升沿
HOME_NLIMT_PHOME_REDGE = 29  # 负限位+正原点开关上升沿
HOME_NLIMT_PHOME_FEDGE = 30  # 负限位+正原点开关下降沿
HOME_NEGZINDEX = 33  # 负向Z信号
HOME_POSZINDEX = 34  # 正向Z信号

# 资源类型宏定义
# 说明：以下宏定义针对IMC_GetResCount函数
MC_ECAT_DO = 0  # ecat的通用do
MC_LOCAL_DO = 1  # localBus的通用do
MC_ECAT_DI = 11  # ecat的通用DI
MC_ECAT_AD = 12  # ecat的通用AD
MC_ECAT_DA = 13  # ecat的通用DA
MC_ECAT_PT = 14  # ecat的通用PT
MC_ECAT_AXIS = 15  # ecat的通用AXIS
RES_LOCAL_DO = 16  # 本地DO数量
MC_AXIS = 30  # 板卡最大轴数
MC_PROFILE = 31  # 板卡规划轴数
MC_CRD_MAX_CNT = 60  # 坐标系最大个数
MC_CRD_BUF_LEN = 61  # 坐标系缓冲区长度

# 板卡系统版本类型定义
# 说明：以下宏定义针对IMC_GetImcCardVersion函数
SOFT_VERSION = 0
DSP_VERSION = 1
ARM_VERSION = 2
API_VERSION = 3
FPGA_VERSION = 4
LIB_ECAT_VERSION = 11
LIB_DSP_VERSION = 12

# 轴DI停止类型定义
# 说明：以下宏定义针对IMC_AxSetStopTrigPara、IMC_AxGetStopTrigPara函数
CNST_DI_STOP_TYPE_ECATDI = 0  # EcatDI停止类型
CNST_DI_STOP_TYPE_PROBLE1_RF = 1  # 探针1上升沿或下降沿停止
CNST_DI_STOP_TYPE_PROBLE1_R = 2  # 探针1上升沿停止
CNST_DI_STOP_TYPE_PROBLE1_F = 3  # 探针1下降沿停止

# 轴状态位定义
# 说明：以下宏定义针对IMC_GetAxSts函数
AX_ALARM_BIT = 0x00000001  # 轴驱动报警
AX_SVON_BIT = 0x00000002  # 伺服使能
AX_BUSY_BIT = 0x00000004  # 轴忙状态
AX_ARRIVE_BIT = 0x00000008  # 轴到位状态
AX_POSLMT_BIT = 0x00000010  # 正硬限位报警
AX_NEGLMT_BIT = 0x00000020  # 负硬限位报警
AX_SOFT_POSLMT_BIT = 0x00000040  # 正软限位报警
AX_SOFT_NEGLMT_BIT = 0x00000080  # 负软限位报警
AX_ERRPOS_BIT = 0x00000100  # 轴位置误差越限标志
AX_EMG_STOP_BIT = 0x00000200  # 运动急停标志
AX_ECAT_BIT = 0x00000400  # 总线轴标志
AX_SW_ABNOR_BIT = 0x00000800  # 轴异常报警(龙门)
AX_WARING_BIT = 0x00001000  # 轴警告
AX_HM_BIT = 0x00002000  # 原点信号状态

# 采集数据类型定义
# 单轴数据类型
SAMPLE_ADDRESS_TYPE_AX_PRF_POS = 0x01
SAMPLE_ADDRESS_TYPE_AX_ENC_POS = 0x02
SAMPLE_ADDRESS_TYPE_AX_PRF_VEL = 0x03
SAMPLE_ADDRESS_TYPE_AX_ENC_VEL = 0x04
SAMPLE_ADDRESS_TYPE_AX_PRF_ACC = 0x05
SAMPLE_ADDRESS_TYPE_AX_ENC_ACC = 0x06
SAMPLE_ADDRESS_TYPE_PRF_POS = 0x07
SAMPLE_ADDRESS_TYPE_PRF_CMPPOS = 0x08
SAMPLE_ADDRESS_TYPE_AX_TORQ = 0x0a
SAMPLE_ADDRESS_TYPE_AX_STS = 0x0b

# 资源信号数据类型
SAMPLE_ADDRESS_TYPE_ECAT_DI = 0x30
SAMPLE_ADDRESS_TYPE_ECAT_DO = 0x31
SAMPLE_ADDRESS_TYPE_LOCAL_DI = 0x32
SAMPLE_ADDRESS_TYPE_LOCAL_DO = 0x33
SAMPLE_ADDRESS_TYPE_ECAT_AD = 0x34
SAMPLE_ADDRESS_TYPE_ECAT_DA = 0x35

# 总线对象字典采集
SAMPLE_ADDRESS_TYPE_RXPDO_2 = 0x40  # pdo通用,2字节,写
SAMPLE_ADDRESS_TYPE_RXPDO_4 = 0x41  # pdo通用,4字节，写
SAMPLE_ADDRESS_TYPE_6040 = 0x42  # 控制字
SAMPLE_ADDRESS_TYPE_607A = 0x43  # 目标位置
SAMPLE_ADDRESS_TYPE_60FF = 0x44  # 目标速度
SAMPLE_ADDRESS_TYPE_6071 = 0x45  # 目标力矩
SAMPLE_ADDRESS_TYPE_6060 = 0x46  # 模式控制
SAMPLE_ADDRESS_TYPE_60FE = 0x47  # 数字量输出
SAMPLE_ADDRESS_TYPE_60B8 = 0x48  # 探针控制字

SAMPLE_ADDRESS_TYPE_TXPDO_2 = 0x50  # pdo通用,2字节,读
SAMPLE_ADDRESS_TYPE_TXPDO_4 = 0x51  # pdo通用,4字节,读
SAMPLE_ADDRESS_TYPE_6041 = 0x52  # 状态字
SAMPLE_ADDRESS_TYPE_6064 = 0x53  # 实际位置 6063
SAMPLE_ADDRESS_TYPE_606C = 0x54  # 实际速度
SAMPLE_ADDRESS_TYPE_6077 = 0x55  # 实际力矩
SAMPLE_ADDRESS_TYPE_60F4 = 0x56  # 跟随误差
SAMPLE_ADDRESS_TYPE_603F = 0x57  # 错误码
SAMPLE_ADDRESS_TYPE_60FD = 0x58  # 数字量输入
SAMPLE_ADDRESS_TYPE_60B9 = 0x59  # 探针状态字
SAMPLE_ADDRESS_TYPE_60BA = 0x60  # 探针位置1
SAMPLE_ADDRESS_TYPE_60BB = 0x61  # 探针位置2

# 插补数据类型
SAMPLE_ADDRESS_TYPE_CRD1_POSX = 0x100
SAMPLE_ADDRESS_TYPE_CRD1_POSY = 0x101
SAMPLE_ADDRESS_TYPE_CRD1_POSZ = 0x102
SAMPLE_ADDRESS_TYPE_CRD1_VEL = 0x103
SAMPLE_ADDRESS_TYPE_CRD2_POSX = 0x150
SAMPLE_ADDRESS_TYPE_CRD2_POSY = 0x151
SAMPLE_ADDRESS_TYPE_CRD2_POSZ = 0x152
SAMPLE_ADDRESS_TYPE_CRD2_VEL = 0x153
SAMPLE_ADDRESS_TYPE_CRD3_POSX = 0x200
SAMPLE_ADDRESS_TYPE_CRD3_POSY = 0x201
SAMPLE_ADDRESS_TYPE_CRD3_POSZ = 0x202
SAMPLE_ADDRESS_TYPE_CRD3_VEL = 0x203
SAMPLE_ADDRESS_TYPE_CRD4_POSX = 0x250
SAMPLE_ADDRESS_TYPE_CRD4_POSY = 0x251
SAMPLE_ADDRESS_TYPE_CRD4_POSZ = 0x252
SAMPLE_ADDRESS_TYPE_CRD4_VEL = 0x253

# 采集触发类型
SAMPLE_TRIG_IMMEDIATE = 0  # 立即采集
SAMPLE_TRIG_DELAY = 1  # 延时采集
SAMPLE_TRIG_LOCAL_DI = 2  # 本地DI触发
SAMPLE_TRIG_ECAT_DI = 3  # ECAT 的DI 触发

EXE_SUCCESS = 0x0000  # 指令成功

ERR_TRANSMIT = 0x0001  # 指令传输错误
ERR_UNKNOWN = 0x0002  # 不支持的指令
ERR_PARSE = 0x0003  # 指令解析错误
ERR_PARAM_OUTRANG = 0x0007  # 传入参数不在范围
ERR_PARAM_VALUE = 0x0008  # 传入参数非0或非1

ERR_BGVEL_OUTRANG = 0x0010  # 起始速度设置超出范围
ERR_MAXVEL_OUTRANG = 0x0011  # 最大速度设置超出范围
ERR_MAXACC_OUTRANG = 0x0012  # 最大加速度设置超出范围
ERR_MAXDEC_OUTRANG = 0x0013  # 最大减速度设置超出范围
ERR_MAXJERK_OUTRANG = 0x0014  # 最大加加速度设置超出范围
ERR_STOPDEC_OUTRANG = 0x0015  # 平滑停止速度设置超出范围
ERR_ESTOPDEC_OUTRANG = 0x0016  # 急停速度设置超出范围
ERR_VEL_OUTRANG = 0x0017  # 运行速度设置超出范围
ERR_ACC_OUTRANG = 0x0018  # 运行加速度设置超出范围
ERR_DEC_OUTRANG = 0x0019  # 运行减速度设置超出范围
ERR_RATIO_OUTRANG = 0x001a  # 倍率设置超出范围
ERR_TGTPOS_OUTRANG = 0x001b  # 目标位置设置超出范围
ERR_INDEX_OUTRANG = 0x001c  # 索引号设置超出范围
ERR_DIMDL_NUM_OUTRANG = 0x001d  # 设置ECAT的DI超出DI模块数量范围
ERR_DOMDL_NUM_OUTRANG = 0x001e  # 设置ECAT的DO超出DO模块数量范围
ERR_AIMDL_NUM_OUTRANG = 0x001f  # 设置ECAT的AI超出AI模块数量范围
ERR_AOMDL_NUM_OUTRANG = 0x0020  # 设置ECAT的AO超出AO模块数量范围
ERR_NO_ECAT_DO = 0x0021  # ECAT未配置DO模块
ERR_NO_ECAT_DI = 0x0022  # ECAT未配置DI模块
ERR_NO_ECAT_AO = 0x0023  # ECAT未配置AO模块
ERR_NO_ECAT_AI = 0x0024  # ECAT未配置AI模块
ERR_NO_ECAT_ENC = 0x0025  # ECAT未配置ENC模块
ERR_TYPE_PARA = 0x0026  # 指令中类型参数错误
ERR_OUTCHN_PARA = 0x0027  # 输出通道参数错误
ERR_ALRM_ENABLE = 0x0028  # 报警使能参数非0或1
ERR_SOFTLMT_ENABLE = 0x0029  # 软限位使能参数非0或1
ERR_HWLMT_ENABLE = 0x002a  # 硬限位使能参数非0或1
ERR_ERRLMT_ENABLE = 0x002b  # 跟随误差报警使能参数非0或1
ERR_COUNT_OUTRANG = 0x002c  # 数量的参数超出规定范围
ERR_HOME_FLTTIME = 0x002e  # HOME滤波参数错误
ERR_LIMIT_FLTTIME = 0x002f  # LIMIT滤波参数错误
ERR_PROBE_FLTTIME = 0x0030  # PROBE滤波参数错误
ERR_INVERSE_PARA = 0x0031  # 取反参数非0或1
ERR_MODE_PARA = 0x0032  # 指令中模式参数错误
ERR_LEVEL_PARA = 0x0033  # 指令电平参数非0或1
ERR_SRC_PARA = 0x0034  # 指令源参数错误，不在规定范围
ERR_TRIG_SNS = 0x0035  # 触发电平参数非0或1
ERR_CYCTIME = 0x0036  # 设置规划周期参数不在规定范围
ERR_FLAG_PARA = 0x0037  # 标志参数设置非0或1
ERR_ONOFF_PARA = 0x0038  # 开关参数设置非0或1
ERR_SV_ALARM = 0x0039  # 伺服报警
ERR_SV_OFF = 0x003a  # 掉使能报警
ERR_TERMINAL_NOLINK = 0x003b  # 端子板通讯失败
ERR_AX_BUSY = 0x003c  # 轴正处于规划中
ERR_ST_HOMING = 0x003d  # 启动回零错误，该轴配置成了虚轴
ERR_SAMPLE_COUNT = 0x003e  # 采样数据的个数不对
ERR_SAMPLE_BUSY = 0x003f  # 采样正忙，不能配置参数
ERR_SAMPLE_DATATYPE = 0x0040  # 采样数据的类型不存在
ERR_SAMPLE_INDEX = 0x0041  # 采样数据的下标越界
ERR_SAMPLE_DRAW_DATA = 0x0042  # 读取采样数据失败
ERR_HOMING_AX_TYPE = 0x0043  # 回零的轴类型不对，非端子板轴
ERR_HOMING_MODE = 0x0044  # 回零的模式不对，不在回零范围内
ERR_HOMING_POS_SRC = 0x0045  # 端子板轴回零的位置来源参数设置不在范围内
ERR_HOMING_MAXTIME = 0x0046  # 判断回零等待超时最短时间不能小于1s
ERR_HOMING_NO_READY = 0x0047  # 回零参数未设置好错误
ERR_HANDWHEEL_BUSY = 0x0048  # 手轮处于忙状态
ERR_HANDWHEEL_M_INDEX = 0x0049  # 手轮主跟随编码器的序号不在范围内
ERR_NO_HANDWHEEL_MODE = 0x004a  # 非手轮模式
ERR_HANDWHEEL_M_MOVE = 0x004b  # 手轮主跟随编码器的在进入手轮前就在运动
ERR_COMP_DIMENS = 0x004c  # 位置比较的维数错误
ERR_COMP_SRC_NO = 0x004d  # 位置比较的位置源端口号超出范围
ERR_COMP_SRC_TYPE = 0x004e  # 位置比较的源类型错误
ERR_COMP_PULSE_WIDTH = 0x004f  # 位置比较的脉冲输出宽度
ERR_COMP_OUTVAL = 0x0050  # 位置比较的立即输出值不在范围内
ERR_COMP_CTRLMODE = 0x0051  # 位置比较输出的控制模式参数设置错误
ERR_COMP_INTERVAL = 0x0052  # 位置等距比较输出的间距值小于1个pulse
ERR_COMP_REPEATTIME = 0x0053  # 位置等距比较输出的次数小于1次
ERR_COMP_BUSY = 0x0054  # 位置比较输出忙
ERR_ECAT_CAPT_DISEN = 0x0055  # ECAT捕获未使能
ERR_PARA_LESS_ZERO = 0x0056  # 参数设置小于0
ERR_PWM_DUTY_OUTRANG = 0x0057  # PWM设置的占空比超限
ERR_PWM_FRQ_LESS_ZERO = 0x0058  # PWM设置的频率小于0
ERR_PWM_NO_RIGHT_MODE = 0x0059  # PWM模式错误
ERR_BACKLASH_CMPVAL = 0x005a  # 反向间隙总补偿量设置小于0
ERR_BACKLASH_CMPVEL = 0x005b  # 反向间隙补偿量速度小于0
ERR_BACKLASH_CMPDIR = 0x005c  # 反向间隙补偿方向错误
ERR_AX_NO_BOND = 0x005d  # 轴未绑定物理输出端
ERR_AX_BOND_SAME_CHN = 0x005e  # 轴绑定了相同的一个物理轴
ERR_LOCAL_DI_FLTTIME = 0x005f  # DI滤波参数错误
ERR_COUNT_IS_BONDED = 0x0060  # 清除的内部计数通道被绑定轴上了
ERR_ENC_IS_BONDED = 0x0061  # 清除的编码器计数通道被绑定轴上了
ERR_AX_IS_MASKED_TO_CRD = 0x0062  # 轴已映射至插补坐标系
ERR_PRF_IN_WRONG_MODE = 0x0063  # 在错误模式下执行
ERR_CRD_NOT_EXIST = 0x0064  # 坐标系不存在
ERR_TOL_OUTRANG = 0x0065  # 坐标系精度参数设置错误
ERR_CRD_COPLAN_PARA = 0x0066  # 坐标系异面过渡参数设置错误
ERR_CRD_TURN_PARA = 0x0067  # 坐标系拐弯系数设置错误
ERR_CRD_TRANSMODE_PARA = 0x0068  # 坐标系过渡模式设置错误
ERR_CRD_NODATA_PROTECT_PARA = 0x0069  # 坐标系数据断流保护参数错误
ERR_CRD_ARC_ACC_PARA = 0x006a  # 坐标系圆弧变加速参数设置错误
ERR_CRD_TRAJ_TYPE_PARA = 0x006b  # 坐标系速度规划类型参数设置错误
ERR_CRD_FATAL_DATA_ERR = 0x006c  # 坐标系压入数据致命错误
ERR_CRD_DO_TYPE = 0x006d  # 坐标系压入的DO类型错误
ERR_CRD_AX_POS_ERR = 0x006e  # 插补轴当前的位置与插补数据第一段运行前的位置相差太大[SGQ]23.10.13
ERR_CRD_LOOKAHEAD_LEN = 0x006f  # 坐标系前瞻长度设置错误
ERR_CRD_SGL_FLT_DEPTH = 0x0070  # 坐标系单轴滤波参数错误
ERR_CRD_SGL_CTRL_TOL = 0x0071  # 坐标系单轴控制精度参数错误
ERR_CRD_TCQ_OVERWRITE = 0x0072  # 插补数据恢复功能中，插补数据段产生覆盖[SGQ]23.10.16
ERR_CRD_MASK_SAME_AXNO = 0x0073  # 坐标系输出轴映射到相同端口错误
ERR_CRD_MASK_AXNO_OUTRANG = 0x0074  # 坐标系输出轴映射号超出范围
ERR_CRD_REPEATED_CREATED = 0x0075  # 坐标系重复创建
ERR_CRD_CREATE_FAILED = 0x0076  # 坐标系创建失败
ERR_CRD_BUSY = 0x0077  # 坐标系正处于规划中
ERR_CRD_SMOOTH_COEF = 0x0078  # 坐标系平滑系数设置错误
ERR_CRD_BUF_FULL = 0x0079  # 坐标系数据缓冲区满
ERR_CRD_BUF_DATA_PARA = 0x007a  # 坐标系缓冲区指令参数错误
ERR_CRD_BUF_DATA_GEOM = 0x007b  # 坐标系缓冲区指令几何构造错误
ERR_CRD_DOWNLOAD_DATA = 0x007c  # 坐标系缓冲区指令下发底层失败
ERR_CRD_PAUSE_POS_CHANGE = 0x007d  # 坐标系暂停后，位置被改变
ERR_FORBID_SVON = 0x007e  # 禁止使能报警
ERR_AX_CRD_CONFLICT = 0x007f  # 单轴和插补运动冲突报警
ERR_DIS_ERR = 0x0080  # 坐标系输入线段弧长过短
ERR_CRD_EXT_AX_CONFLICT = 0x0081  # 缓存同步事件设置轴号运动冲突
ERR_CRD_RUN_ERR = 0x0082  # 坐标系运行报警错误，需要清除才能再次启动或者压入数据
ERR_CRD_ARC_DIR_PARA = 0x0083  # 坐标系中圆弧运动的方向参数错误
ERR_CRD_SYNC_ERROR = 0x0084  # 坐标系中同步运动无法完成
ERR_CRD_BUF_NOT_EPMTY = 0x0085  # 坐标系参数设置未满足缓冲区数据为空要求
ERR_CRD_MODE_UNMACHED = 0x0086  # 坐标系不匹配的插补模式，如：非用户规划模式
ERR_CRD_ALL_BUSY = 0x0087  # 坐标系所有均繁忙
ERR_AX_NOT_EXIST = 0x0088  # 单轴未参与任何一个插补坐标系
ERR_CRDIN_GEOM_ERR = 0x0089  # 立即插补几何错误
ERR_CRD_INLINE = 0x008a  # 圆弧三点共线
ERR_CRD_NORMAL_TOO_SHORT = 0x008b  # 圆弧输入的法向量太短
ERR_CRD_RADIUS_TOO_SHORT = 0x008c  # 圆弧输入的半径太短
ERR_CRD_NORMAL_ANGLE = 0x008d  # 圆弧输入的法向量角度错误
ERR_CRD_RADIUS_ERR = 0x008e  # 特指圆弧半径输入模式下，半径小于首点到末点长度的一半
ERR_CRD_TC_BUF_EMPTY = 0x008f  # 底层插补队列为空[SGQ]23.10.12

ERR_LENGTH_OUTRANG = 0x0090  # 设置的长度单位不在范围
ERR_SOFTLMT_POS_LESS_NEG = 0x0091  # 软正限位设置比软负限位小错误
ERR_SAMPLE_INTERVAL = 0x0092  # 数据采样配置间隔参数错误
ERR_SAMPLE_TRIG_TYPE = 0x0093  # 数据采样配置触发采样类型参数错误
ERR_SAMPLE_DELAY_PARA = 0x0094  # 数据采样配置启动延时参数错误
ERR_SAMPLE_DI_NO = 0x0095  # 数据采样配置DI触发端口错误
ERR_SAMPLE_DI_LEVEL = 0x0096  # 数据采样配置DI触发电平错误
ERR_RESET_IS_PERMIT = 0x0097  # 系统复位条件不足，检查是否还在使能
ERR_GANTRY_IS_USING = 0x0098  # 龙门正在使用中
ERR_GANTRY_ERRORLMT_LESS_ZERO = 0x0099  # 龙门主从轴误差极限值小于0
ERR_GANTRY_ERROR_OUT_LIMIT = 0x009a  # 龙门主从轴误差大于设定极限
ERR_GANTRY_SLAVE_FORBID_PRF = 0x009b  # 龙门从轴禁止规划
ERR_GANTRY_AX_EQU_DIFF = 0x009c  # 龙门主从轴的当量不一致
ERR_GANTRY_AX_SV_STS_DIFF = 0x009d  # 龙门主从轴的伺服状态不一致
ERR_ECAT_DA_VAL = 0x009e  # ECAT总线的DA值设置范围超限
ERR_GANTRY_AXNO_CONFLICT = 0x009f  # 配置龙门的轴号各组有冲突

ERR_SYNCMOVE_NOT_EXIST = 0x00a0  # 多轴系统未建立
ERR_SYNCMOVE_HAVE_EXISTED = 0x00a1  # 多轴系统重复创建
ERR_SYNCMOVE_COUNT = 0x00a2  # 多轴系统轴映射总数量不在范围内
ERR_SYNCMOVE_MAP = 0x00a3  # 多轴系统轴映射错误
ERR_SYNCMOVE_RATIO = 0x00a4  # 多轴系统比率设定范围错误
ERR_SYNCMOVE_AXNO_REPEATED = 0x00a5  # 多轴系统的映射轴有重复
ERR_SYNCMOVE_AXNO_OUTRANG = 0x00a6  # 多轴系统的映射轴不在系统范围
ERR_AX_MULTI_SYNC_CONFLICT = 0x00a7  # 多轴系统中的轴与单轴运动冲突
ERR_AX_IS_SET_MULTI_PRF = 0x00a8  # 当前轴已设置为多轴或插补规划模式，不能再次设置
ERR_SYNCMOVE_PAUSE_POS_CHANGE = 0x00a9  # 多轴系统暂停后，位置被改变
ERR_SYNCMOVE_ALARM = 0x00aa  # 多轴系统有报警，不允许启动

ERR_HOMING_METHOD = 0x00b0  # 回零方式错误
ERR_NO_ECAT_SV = 0x00b1  # 非ECAT伺服轴
ERR_CST_GANTRY_FORBID = 0x00b2  # 龙门控制，不允许伺服为转矩模式
ERR_CTRL_MODE = 0x00b3  # 错误控制模式
ERR_TGTTRQ_OUTRANG = 0x00b4  # 目标转矩设置超出范围
ERR_TRQ_CHANGE_TIME_LESS_ZERO = 0x00b5  # 目标转矩的改变时间参数小于0
ERR_FORBID_POS_PRF_IN_CST = 0x00b6  # 禁止在CST模式下进行位置规划
ERR_SV_MODE_PDO_NO_CFG = 0x00b7  # ECAT伺服的模式PDO对象未配置
ERR_AX_IS_IN_HOMING = 0x00b8  # 轴正处于回零状态
ERR_HW_ESTP_IS_TRIG = 0x00b9  # 硬件急停信号触发
ERR_ACT_TORQ_PDO_NO_CFG = 0x00ba  # ECAT伺服的实际转矩PDO对象未配置
ERR_TOUCH_PROBE_PDO_NO_CFG = 0x00bb  # ECAT伺服的探针捕获相关PDO对象未配置
ERR_AX_MV_DIR_LIMT_TRIG = 0x00bc  # 轴运动方向的限位触发
ERR_AX_FOLLOW_ERROR = 0x00bd  # 轴跟随误差报警
ERR_AX_STATUS_ERROR = 0x00be  # 轴状态错误，调用查询轴状态指令获取具体信息
ERR_TOUCH_PROBE2_UNSUPPORT = 0x00bf  # 不支持探针2

ERR_SET_TIME = 0x00c0  # 时间类参数设置错误
ERR_PVT_LIST = 0x00c1  # PVT表参数设置错误
ERR_PVT_LOOP = 0x00c2  # PVT循环次数参数设置错误
ERR_PVT_PARAM = 0x00c3  # PVT数据参数输入错误
ERR_PVT_TABLE_BUSY = 0x00c4  # PVT当前表被占用
ERR_PVT_TABLE_INVALID = 0x00c5  # PVT当前表类型不匹配
ERR_PVT_TABLE_FULL = 0x00c6  # PVT表FIFO数据满
ERR_PVT_TABLE_NULL = 0x00c7  # PVT表数据为NULL
ERR_NOT_PVT_MODE = 0x00c8  # 非PVT模式下，不能访问

ERR_FOL_SCALE = 0x00d1  # FOL齿数输入有误
ERR_FOL_MASTER_NO = 0x00d2  # FOL主轴轴号输入有误
ERR_FOL_LMT_POS = 0x00d3  # FOL从轴跟随位置有误
ERR_PTPC_MOVE_PARAM = 0x00d4  # PTP缓存模式运动参数有误
ERR_EDVEL_OUTRANG = 0x00d5  # 结束速度有问题
ERR_FIFO_FULL = 0x00d6  # 队列数据满
ERR_FIFO_EMPTY = 0x00d7  # 队列数据空
ERR_FIFO_STPOS_DIFF_CURPOS = 0x00d8  # 队列起始位置与当前位置不一致
ERR_NOT_HOMING_MODE = 0x00d9  # 非回零规划模式
ERR_GEAR_UPDATE_SCALE = 0x00da  # 电子齿轮更新比例失败
ERR_FOL_SLOPE_LEES_ZERO = 0x00db  # FOL的主轴离合区值小于0
ERR_PROBE_BIT_OUTRANGE = 0x00dc  # 设置轴ECAT探针对应bit不在0~31中

ERR_ENC_FILTER_DEPTH = 0x00e0  # 编码器滤波深度参数错误
ERR_ENC_FILTER_COEF = 0x00e1  # 编码器滤波系数参数错误
ERR_COMPARE_BUF_EMPTY = 0x00e2  # 位置比较缓冲区数据为空
ERR_COMPARE_DATA_INVERSE = 0x00e3  # 位置比较设置的比较数据出现反向
ERR_COMPARE_POS_TYPE = 0x00e4  # 等距比较数据不允许在绝对位置比较类型下压入
ERR_COMPARE_DATA_TYPE = 0x00e5  # 等距比较数据不允许在动态数据类型下压入
ERR_AX_HW_NOT_EXIST = 0x00e6  # 设置的物理轴不存在
ERR_TGTPOS_OVER_SOFTLMT = 0x00e7  # 目标位置超出了软限位范围
ERR_BACKLASH_VAL_NOT_ZERO = 0x00e8  # 当前反向间隙补偿的值不为0，不能再次修改设置反向间隙值
ERR_WRONG_HOMING_MODE = 0x00e9  # 调用错误回零完成指令
ERR_AX_COMPEN_BUSY = 0x00ea  # 轴补偿进行中
ERR_MULTI_COMPARE_UNSUPPORTED = 0x00eb  # 多维位置比较不支持错误

ERR_WAIT_TIME_PARA = 0x00f2  # 等待事件类型参数错误
ERR_CYCMV_PARA_NOT_SET = 0x00f3  # 周期运动的参数未设置，不能启动
ERR_NOT_CYCMV_MODE = 0x00f4  # 非周期模式下操作
ERR_HOMING_DIR_PARA = 0x00f5  # 回零方向参数错误
ERR_HOMING_LEVEL_PARA = 0x00f6  # 回零触发沿参数错误
ERR_CSV_PRF_NOT_START = 0x00f7  # CSV规划没有启动
ERR_CSV_IN_PRFING = 0x00f8  # CSV在规划中，不允许切换到CSP下
ERR_NO_TERMINAL_CFG = 0x00f9  # 端子板没有配置，不允许访问
ERR_OFFSET_PARA = 0x00fa  # 偏置参数不在范围
ERR_PTP_NOT_PAUSE = 0x00fb  # PTP无暂停动作
ERR_PTP_STOPPED = 0x00fc  # PTP运动已停止，不能调用Pause指令

ERR_VERSION_TOO_LOW = 0x0100  # dll库版本比控制器版本低
ERR_CST_HANDWHEEL_FORBID = 0x0101  # 手轮控制，不允许伺服为转矩模式
ERR_GANTRY_NOT_SETUP = 0x0102  # 龙门关系尚未建立
ERR_WATCHDOG_TIME_LESS_ZERO = 0x0103  # 看门狗设置时间小于0
ERR_MULTI_PTP_AXNUM = 0x0104  # 多轴同时启动PTP的个数错误
ERR_MULTI_JOG_AXNUM = 0x0105  # 多轴同时启动JOG的个数错误
ERR_WATCHDOG_NOT_OPENED = 0x0106  # 看门狗未开启
ERR_WRONG_MODE_OPERATIONG = 0x0107  # 错误模式下操作
ERR_NO_SYS_INT_SIGNAL = 0x0108  # 系统中断没有起来，请检查总线是否处于OP状态
ERR_GET_SYS_HW_RES = 0x0109  # 获取系统硬件资源失败：如端子板资源或ECAT资源
ERR_TORQ_SLP_PDO_NO_CFG = 0x0110  # ECAT伺服的转矩斜坡PDO对象未配置
ERR_TGT_TORQ_PDO_NO_CFG = 0x0111  # ECAT伺服的目标转矩PDO对象未配置
ERR_PRESS_CTRL_PDO_NO_CFG = 0x0112  # ECAT伺服中的压合控制对象未配置（SV510）
ERR_PRESS_STS_PDO_NO_CFG = 0x0113  # ECAT伺服中的压合状态对象未配置（SV510）
ERR_PRESS_VAL_PDO_NO_CFG = 0x0114  # ECAT伺服中的压力反馈对象未配置（SV510）
ERR_AI1_VOLT_PDO_NO_CFG = 0x0115  # ECAT伺服中的电压1输入对象未配置（SV510）
ERR_AI2_VOLT_PDO_NO_CFG = 0x0116  # ECAT伺服中的电压2输入对象未配置（SV510）
ERR_NO_ECAT_PT = 0x0117  # ECAT未配置PT模块
ERR_PRESS_SETVAL_PDO_NO_CFG = 0x0118  # ECAT伺服中的目标压合力设置对象未配置（SV510）
ERR_MAXVEL_PDO_NO_CFG = 0x0119  # ECAT伺服中的最大速度限制设置对象未配置
ERR_POS_TORQ_LMT_PDO_NO_CFG = 0x011a  # ECAT伺服中的正向转矩限制设置对象未配置
ERR_NEG_TORQ_LMT_PDO_NO_CFG = 0x011b  # ECAT伺服中的负向转矩限制设置对象未配置
ERR_MAX_TORQ_LMT_PDO_NO_CFG = 0x011c  # ECAT伺服中的最大转矩限制设置对象未配置
ERR_MPG_NOT_CFG = 0x011d  # ECAT的手轮模块没有配置对象
ERR_MPG_NOT_ENABLE = 0x011e  # ECAT的手轮模块没有使能
ERR_AX_DO_CFG = 0x011f  # ECAT轴的do输出没有配置

ERR_EVENT_IO_INTYPE = 0x0120  # IO事件的输入类型错误
ERR_EVENT_IO_INPORT = 0x0121  # IO事件的输入端口错误
ERR_EVENT_IO_IN_INVERT = 0x0122  # IO事件的输入取反值错误
ERR_EVENT_IO_OPERTOR = 0x0123  # IO事件的输入操作符错误
ERR_EVENT_IO_OUTTYPE = 0x0124  # IO事件的输出类型错误
ERR_EVENT_IO_OUT_INVERT = 0x0125  # IO事件的输出取反值错误
ERR_EVENT_IO_OUTPORT = 0x0126  # IO事件的输出端口号错误
ERR_EVENT_IO_TRIG_TYPE = 0x0127  # IO事件的触发类型错误
ERR_EVENT_IO_DELAY = 0x0128  # IO事件的延时值小于0
ERR_EVENT_IO_ACTIVE_TYPE = 0x0129  # IO事件的激活类型错误
ERR_EVENT_IO_PARA_NO_SET = 0x012a  # IO事件的参数没有设置，不能使能

ERR_EVENT_DIMT_INTYPE = 0x0130  # DI触发运动事件的输入类型错误
ERR_EVENT_DIMT_INPORT = 0x0131  # DI触发运动事件的输入端口错误
ERR_EVENT_DIMT_AXNO = 0x0132  # DI触发运动事件的触发轴号超出范围
ERR_EVENT_DIMT_DELAY = 0x0133  # DI触发运动事件的延时值小于0
ERR_EVENT_DIMT_TGTVEL = 0x0134  # DI触发运动事件设置的目标速度小于0
ERR_EVENT_DIMT_ACC = 0x0135  # DI触发运动事件设置的加速度小于0
ERR_EVENT_DIMT_DEC = 0x0136  # DI触发运动事件设置的减速度小于0
ERR_EVENT_DIMT_TGTPOS = 0x0137  # DI触发运动事件设置的目标位置超限
ERR_EVENT_DIMT_INVERTBIT = 0x0138  # DI触发运动事件设置的取反标志非0和1
ERR_EVENT_DIMT_MOTION_TYPE = 0x0139  # DI触发运动事件设置的运动类型错误
ERR_EVENT_DIMT_TRIGGER_TYPE = 0x013a  # DI触发运动事件设置的触发类型错误
ERR_EVENT_DIMT_PARA_NO_SET = 0x013b  # DI触发运动事件的参数没有设置，不能使能

ERR_EVENT_CMPOUT_INTYPE = 0x0140  # 比较位置输出事件的输入类型错误
ERR_EVENT_CMPOUT_PORT = 0x0141  # 比较位置输出事件的输出源端口号超出范围
ERR_EVENT_CMPOUT_OUTPORT = 0x0142  # 比较位置输出事件的输出DO端口超出范围
ERR_EVENT_CMPOUT_OUTTYPE = 0x0143  # 比较位置输出事件的输出类型错误
ERR_EVENT_CMPOUT_OUTVAL = 0x0144  # 比较位置输出事件的输出值错误
ERR_EVENT_CMPOUT_CMPTYPE = 0x0145  # 比较位置输出事件的比较类型参数错误
ERR_EVENT_CMPOUT_PLSWIDTH = 0x0146  # 比较位置输出事件的脉冲输出脉宽小于0
ERR_EVENT_CMPOUT_CMPPOS = 0x0147  # 比较位置输出事件的比较位置超出范围
ERR_EVENT_VIRTUAL_IO_VAL = 0x0148  # 事件虚拟IO的值设置错误
ERR_EVENT_VIRTUAL_IO_DISABLE = 0x0149  # 事件虚拟被禁用，不能作为输出使用
ERR_EVENT_CMPOUT_PARA_NO_SET = 0x014a  # 比较位置输出事件的参数没有设置，不能使能

ERR_PSO_DIMENS = 0x0150  # PSO的维数参数错误
ERR_PSO_PULSE_WIDTH = 0x0151  # PSO的脉冲输出宽度错误
ERR_PSO_SRC_NO = 0x0152  # PSO的位置源序号错误
ERR_PSO_SRC_TYPE = 0x0153  # PSO的位置源类型错误
ERR_PSO_SYN_POS = 0x0154  # PSO的同步比较输出间距错误

ERR_SCREWCMP_DIR = 0x0200  # 螺距补偿方向设置错误
ERR_SCREWCMP_INTERVAL = 0x0201  # 螺距补偿间隔为负
ERR_SCREWCMP_TABLE_NUM = 0x0202  # 螺距补偿的数据表数量超限
ERR_SCREWCMP_ST_BIGGER_END = 0x0203  # 螺距补偿的正向补偿起始位置大于终止位置
ERR_SCREWCMP_CALC_INTERVAL = 0x0204  # 螺距补偿设置的起始和终止位置以及点数计算的间隔距离非整数

ERR_BANDPT_COUNT = 0x0210  # 绑定PT轴映射总数量不在范围内
ERR_BANDPT_AXNO_OUTRANG = 0x0211  # 绑定PT轴超过范围
ERR_BANDPT_AXNO_REPEATED = 0x0212  # 绑定PT轴重复
ERR_AX_IS_SET_BANDPT_PRF = 0x0213  # 轴已经设成绑定PT模式
ERR_BANDPT_NOT_EXIST = 0x0214  # 绑定PT系统轴没有建立
ERR_BANDPT_BEYOND_MAXCNT = 0x0215  # 绑定PT输入数据量超过最大限制
ERR_BANDPT_ERR = 0x0216  # 绑定PT处于错误状态

# 电子凸轮错误
ERR_ECAM_TABLE_FULL = 0x0250  # 电子凸轮数据表满
ERR_ECAM_POS = 0x0251  # 凸轮位置错误
ERR_ECAM_TABLE_BUSY = 0x0252  # 凸轮表被占用
ERR_ECAM_TABLE_NULL = 0x0253  # 凸轮表无数据
ERR_ECAM_EVENT_MASTER_POS = 0x0254  # 凸轮表事件输入主轴位置错误
ERR_ECAM_LIST_TABLE = 0x0255  # 凸轮表list中的表号有误
ERR_ECAM_LIST_FULL = 0x0256  # 凸轮表list表号已放满
ERR_ECAM_MASTER_SLAVE_PARAM = 0x0257  # 凸轮表设置参数主从属性参数设置错误
ERR_ECAM_TABLE_PARAM = 0x0258  # 凸轮表设置参数错误
ERR_ECAM_START_CONDITION = 0x0259  # 凸轮启动条件参数设置错误
ERR_ECAM_NOT_START = 0x025a  # 凸轮还未启动
ERR_ECAM_ALARM = 0x025b  # 凸轮报警
ERR_ECAM_LIST_TABLE_NULL = 0x025c  # 凸轮list无表
ERR_ECAM_LIST_BUSY = 0x025d  # 凸轮list被占用
ERR_ECAM_LIST_TABLE_DATA_FORMAT = 0x025e  # 凸轮list模式中表格式错误

ERR_AX_TYPE_DIFF = 0x0270  # 轴类型不一致错误
ERR_ECAT_ERRCODE_PDO_NO_CFG = 0x0271  # ECAT轴错误码PDO对象未配置
ERR_NO_LOCAL_AXIS = 0x0272  # 非端子板轴通道

ERR_ECAT_AXIS_PDO_NO_CFG = 0x0300  # ECAT轴PDO对象未配置

ERR_MUTI_AX_CMP_BUSY = 0x0500  # 多轴位置比较进行中
ERR_MUTI_AX_CMP_BUF_FULL = 0x0501  # 多轴位置比较缓冲区空间已满
ERR_MUTI_AX_CMP_AX_CNT = 0x0502  # 多轴位置比较轴数小于1
ERR_MUTI_AX_CMP_REPEATED = 0x0503  # 多轴位置比较相邻点重复
ERR_MUTI_AX_CMP_BUF_EMPTY = 0x0504  # 多轴位置比较缓冲区为空

ERR_COMP_MODE = 0x0516  # 位置比较输出比较模式错误
ERR_COMP_OUTTYPE = 0x0517  # 位置比较输出输出类型错误

# 非标错误


ERR_READGCODE_DU = 0x7000  # 重复检测
ERR_READGCODE_REACH_MAXLINE = 0x7001  # 文件行数过多
ERR_READGCODE_NO_FILE = 0x7002  # 文件不存在
ERR_ESTIMATE_INACTIVE = 0x7003  # 时间估算未激活

ERR_DEVICE = 0x8000  # 错误参数输入
ERR_INPUT = 0x8001  # 错误指针参数输入
ERR_CARDNO = 0x8002  # 错误卡号
ERR_MEM1ALLOC = 0x8003  # 分配全局内存1错误
ERR_MEM2ALLOC = 0x8004  # 分配全局内存2错误
ERR_MEM3ALLOC = 0x8005  # 分配全局内存3错误
ERR_OPENDEV = 0x8006  # 打开PCI设备错误
ERR_GETDEVATTR = 0x8007  # 获取PCI设备属性错误
ERR_READ_LEN = 0x8008  # 读取数据长度错误
ERR_READ_CHECKSUM = 0x8009  # 读取校验和错误
ERR_WRITE_BLOCK = 0x800A  # 写块数据失败
ERR_READ_BLOCK = 0x800B  # 读块数据失败
ERR_BLOCK_FIFO_FULL = 0x800C  # 块数据FIFO已经满
ERR_OPEN_CHANNEL = 0x800D  # 打开数据通道失败
ERR_CLOSE_CHANNEL = 0x800E  # 关闭数据通道错误
ERR_DSP_BUSY = 0x800F  # DSP一直处于忙状态
ERR_LOCK_ERROR = 0x8010  # 获取锁资源失败
ERR_WAIT_TIMEOUT = 0x8011  # 等待数据超时
ERR_EXECUTE = 0x8012  # 执行命令错误
ERR_PARAMETER = 0x8013  # 传入参数错误
ERR_OPEN_XML = 0x8014  # 打开XML文件失败
ERR_CREATE_XML = 0x8015  # 创建XML文件失败
ERR_MALLOC_MEM = 0x8016  # 分配文件内存失败
ERR_UNKOWN_AXTYPE = 0x8017  # 不能识别的轴类型
ERR_CARD_HANDLE = 0x8018  # cardhandle错误
ERR_PARSER_XML = 0x8019  # 解析系统参数配置错误
ERR_CHECK_USER_CODE = 0x801A  # 用户密码校验错误
ERR_NOT_ECAT_AX = 0x801B  # 非ECAT轴
ERR_CARD_NUM_OUTRANG = 0x801C  # 扫描板卡数量超限
ERR_PCI2ARMWRDATA = 0x801D  # PCI向ARM侧写数据异常
ERR_PCI2ARMRDDATA = 0x801E  # PCI向ARM侧读数据异常
ERR_CARD_BUSY = 0x801F  # 板卡正上次初始化尚未结束，请稍等
ERR_OPEN_CARD_ERR = 0x8020  # 创建线程错误
ERR_PCI2ARM_CHN = 0x8021  # PCI到ARM通道异常
ERR_PCI2DSP_CHN = 0x8022  # PCI到DSP通道异常

ERR_ARM_ECAT_SHM = 0x9000  # 共享内存错误
ERR_ARM_ECAT_LINK = 0x9001  # EtherCat连接错误
ERR_ARM_ECAT_INIT_STEP0 = 0x9002  # EtherCat初始化阶段STEP0错误
ERR_ARM_SCAN_MODULE = 0x9003  # EtherCat初始化阶段扫描MODULE错误
ERR_ARM_ECAT_INIT_STEP2 = 0x9004  # EtherCat初始化阶段STEP2错误
ERR_ARM_ECAT_INIT_STEP3 = 0x9005  # EtherCat初始化阶段STEP3错误
ERR_ARM_INIT_SYNC_DSP = 0x9006  # EtherCat配置信息同步到DSP错误
ERR_ARM_DEL_MASTER = 0x9007  # 删除EtherCat主站状态机错误
ERR_ARM_SCAN_SLAVES = 0x9008  # 扫描从站设备状态发生错误
ERR_ARM_ECAT_SHM_ADDR = 0x9009  # 共享内存地址非法
ERR_ARM_INUPUT_PARA = 0x900A  # 输入参数错误
ERR_ARM_ECAT_ENTER_HOME_MODE = 0x900B  # EtherCat轴进入回零模式错误
ERR_ARM_ECAT_SET_HOME_PAR = 0x900C  # 设置EtherCat轴回零参数错误
ERR_ARM_ECAT_START_HOME = 0x900D  # 设置EtherCat轴开始回零错误
ERR_ARM_ECAT_STOP_HOME = 0x900E  # 停止EtherCat轴回零错误
ERR_ARM_ECAT_GET_HOME_STATUS = 0x900F  # 获取EtherCat轴回零状态错误
ERR_ARM_ECAT_SET_HOME_FINISH = 0x9010  # 设置完成EtherCat轴回零错误
ERR_ARM_ECAT_EXIT_HOME_MODE = 0x9011  # 退出EtherCat轴回零模式错误
ERR_ARM_FILE_BEYOND_MAX = 0x9012  # 文件太大，超出buffer长度
ERR_ARM_FILE_OPEN = 0x9013  # 打开文件失败
ERR_ARM_FILE_MMAP = 0x9014  # 文件映射失败
ERR_ARM_FILE_MUNMMAP = 0x9015  # 文件反映射失败
ERR_ARM_GET_ECAT_RESOUCE = 0x9016  # 获取EtherCat资源失败
ERR_ARM_SDO_UPLOAD = 0x9017  # 上传EtherCatSDO失败
ERR_ARM_SDO_DOWNLOAD = 0x9018  # 下载EtherCatSDO失败
ERR_ARM_SEND_MSG = 0x9019  # 发送消息失败
ERR_ARM_EXE_FUN = 0x901a  # 执行调用函数异常
ERR_ARM_CK_DEV_XML = 0x901b  # 校验设备配置XML异常
ERR_ARM_NOT_EXIST_STATION = 0x901c  # 不存在该站点
ERR_ARM_SUBBOARD_LINK = 0x901d  # 端子板连接错误
ERR_ARM_CMP_ENCRY_CHIP = 0x901e  # 板卡权限验证不通过
NO_ENCRY_CHIP = 0x901f  # 板卡没有加密芯片
ERR_EEPROM_INFO = 0x9020  # 板卡上板载信息有误
ERR_PDO_OBJ_NOT_SUPPORTED = 0x9021  # 自由访问PDO对象不支持
ERR_STATION_NOT_ALLOWED = 0x9022  # 自由访问PDO的站点不允许访问
ERR_ECAT_STS_NOT_OP_STS = 0x9023  # 主站未处于OP状态
ERR_ECAT_NOT_ALIAS_MODE = 0x9024  # 主站未处于别名模式
ERR_SLAVE_NOT_AXIS_STATION = 0x9025  # 当前站为非轴从站
ERR_SLAVE_OPMODE_STATION = 0x9026  # 当前站为自由协议从站
ERR_SLAVE_NOT_EXIST_SLOT = 0x9027  # 不存在该站点Slot


class ImcLib:
    def __init__(self):
        dll_path = os.path.join(os.path.dirname(__file__), 'IMC_API_x64.dll')
        self.imc_dll = ctypes.CDLL(dll_path)
        # declare function parameters
        self.imc_dll.IMC_GetCardsNum.argtypes = [ctypes.POINTER(INT32)]
        self.imc_dll.IMC_GetCardsNum.restype = UINT32
        self.imc_dll.IMC_OpenCardHandle.argtypes = [INT32, ctypes.POINTER(UINT64)]
        self.imc_dll.IMC_OpenCardHandle.restype = UINT32
        self.imc_dll.IMC_DownLoadDeviceConfig.argtypes = [UINT64, ctypes.c_char_p]
        self.imc_dll.IMC_DownLoadDeviceConfig.restype = UINT32
        self.imc_dll.IMC_ScanCardECAT.argtypes = [UINT64, INT32]
        self.imc_dll.IMC_ScanCardECAT.restype = UINT32
        self.imc_dll.IMC_GetECATMasterSts.argtypes = [UINT64, ctypes.POINTER(UINT32)]
        self.imc_dll.IMC_GetECATMasterSts.restype = UINT32
        self.imc_dll.IMC_DownLoadSystemConfig.argtypes = [UINT64, ctypes.c_char_p]
        self.imc_dll.IMC_DownLoadSystemConfig.restype = UINT32
        self.imc_dll.IMC_CloseCardHandle.argtypes = [UINT64]
        self.imc_dll.IMC_CloseCardHandle.restype = UINT32

    def get_cards_num(self, p_cards_num) -> ctypes.c_uint32:
        try:
            result = self.imc_dll.IMC_GetCardsNum(p_cards_num)
        except Exception as e:
            raise ValueError(f"Failed to execute IMC_GetCardsNum(): {e}")
        return result

    def open_card_handle(self, card_number, p_card_handle) -> ctypes.c_uint32:
        try:
            result = self.imc_dll.IMC_OpenCardHandle(card_number, p_card_handle)
        except Exception as e:
            raise ValueError(f"Failed to execute IMC_OpenCardHandle(): {e}")
        return result

    def download_device_config(self, card_handle, p_path_name) -> ctypes.c_uint32:
        try:
            result = self.imc_dll.IMC_DownLoadDeviceConfig(card_handle, p_path_name)
        except Exception as e:
            raise ValueError(f"Failed to execute IMC_DownLoadDeviceConfig(): {e}")
        return result

    def scan_card_ecat(self, card_handle, block_flag):
        try:
            result = self.imc_dll.IMC_ScanCardECAT(card_handle, block_flag)
        except Exception as e:
            raise ValueError(f"Failed to execute IMC_ScanCardECAT(): {e}")
        return result

    def get_ecatMaster_status(self, card_handle, p_status):
        try:
            result = self.imc_dll.IMC_GetECATMasterSts(card_handle, p_status)
        except Exception as e:
            raise ValueError(f"Failed to execute IMC_ScanCardECAT(): {e}")
        return result

    def download_system_config(self, card_handle, p_path_name):
        try:
            result = self.imc_dll.IMC_DownLoadSystemConfig(card_handle, p_path_name)
        except Exception as e:
            raise ValueError(f"Failed to execute IMC_DownLoadSystemConfig(): {e}")
        return result

    def close_card_handle(self, card_handle):
        try:
            result = self.imc_dll.IMC_CloseCardHandle(card_handle, card_handle)
        except Exception as e:
            raise ValueError(f"Failed to execute IMC_CloseCardHandle(): {e}")
        return result


class IMCpy(ImcLib):
    def __init__(self):
        super().__init__()
        self.total_card_num = 0

    def IMCpy_board_startup(self, cardno):
        self.total_card_num = self.IMCpy_GetCardsNum()
        card_handle = self.IMCpy_OpenCardHandle(cardno)
        self.IMCpy_ScanCardECAT(card_handle, 1)

    def IMCpy_GetCardsNum(self) -> int:
        cardsNum = ctypes.c_int32(0)
        try:
            ret = self.get_cards_num(ctypes.byref(cardsNum))
            if not ret & 0xFFFF == EXE_SUCCESS:
                raise ValueError(f"GetCardsNum failed, ret:{ret}")
            val = cardsNum.value
            if val > 4 or val < 1:
                raise ValueError(f"Invalid cards number:{val}")
            return cardsNum.value
        except Exception as e:
            raise ValueError(f"ERROR:{e}")

    def IMCpy_OpenCardHandle(self, cardno) -> int:
        cardHandle = ctypes.c_uint64(0)
        try:
            ret = self.open_card_handle(ctypes.c_int32(cardno), ctypes.byref(cardHandle))
            cmd = ret & 0xFFFF0000
            resp = ret & 0xFFFF
            if cmd & 0xFFFF0000 != 0x80040000:
                raise ValueError(f"Unknown Command Code:{cmd}")
            if not resp == EXE_SUCCESS:
                if resp == ERR_CARDNO:
                    raise ValueError(f"OpenCardHandle failed, Wrong card number")
                else:
                    raise ValueError(f"OpenCardHandle failed, ret:{ret}")
            return cardHandle.value
        except Exception as e:
            raise ValueError(f"ERROR:{e}")

    def IMCpy_DownLoadDeviceConfig(self, cardhandle, pathname: str):
        pathname_tmp = pathname.encode('utf-8')
        try:
            ret = self.download_device_config(ctypes.c_uint64(cardhandle), ctypes.c_char_p(pathname_tmp))
            if not ret == EXE_SUCCESS:
                raise ValueError(f"DownLoadDeviceConfig failed, ret:{ret}")
            return
        except Exception as e:
            raise ValueError(f"ERROR:{e}")

    def IMCpy_ScanCardECAT(self, cardhandle, blockflag):
        try:
            ret = self.scan_card_ecat(ctypes.c_uint64(cardhandle), ctypes.c_int32(blockflag))
            if not ret & 0xFFFF == EXE_SUCCESS:
                raise ValueError(f"ScanCardECAT failed, ret:{ret}")
            return
        except Exception as e:
            raise ValueError(f"ERROR:{e}")

    def IMCpy_GetECATMasterSts(self, cardhandle) -> int:
        status = ctypes.c_uint32(-1)
        try:
            ret = self.get_ecatMaster_status(ctypes.c_uint64(cardhandle), ctypes.byref(status))
            if not ret == EXE_SUCCESS:
                raise ValueError(f"GetECATMasterSts failed, ret:{ret}")
            val = status.value
            if val < 0 or val > 7:
                raise ValueError(f"Invalid master status: {val}")
            return val
        except Exception as e:
            raise ValueError(f"ERROR:{e}")

    def IMCpy_DownLoadSystemConfig(self, cardhandle, pathname: str):
        pathname_tmp = pathname.encode('utf-8')
        try:
            ret = self.download_system_config(ctypes.c_uint64(cardhandle), ctypes.c_char_p(pathname_tmp))
            if not ret == EXE_SUCCESS:
                raise ValueError(f"DownLoadSystemConfig failed, ret:{ret}")
            return
        except Exception as e:
            raise ValueError(f"ERROR:{e}")


if __name__ == '__main__':
    new = IMCpy()
    new.IMCpy_board_startup(1)
