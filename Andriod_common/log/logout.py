#coding=gbk
import logging
# logging.basicConfig(level=logging.INFO) #调整日志级别，只打印该debug之上的日志
# logging.debug("这是一条debug级别日志")
# logging.warning("这是一条warn级别日志")
# logging.info("这是一条info级别日志")
# logging.error("这是一条error级别日志")
# logging.critical("这是一条critical级别日志")

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s" #格式化输入内容
actime="%Y-%m-%d %H:%M:%S" #格式化时间显示样式
logging.basicConfig(filename="test01.log",level=logging.INFO,format=LOG_FORMAT,datefmt=actime) #配置日志内容文件和输出格式
logging.debug("这是一条debug级别日志")
logging.warning("这是一条warn级别日志")
logging.info("这是一条info级别日志")
logging.error("这是一条error级别日志")
logging.critical("这是一条critical级别日志")