#coding=gbk
import logging
# logging.basicConfig(level=logging.INFO) #������־����ֻ��ӡ��debug֮�ϵ���־
# logging.debug("����һ��debug������־")
# logging.warning("����һ��warn������־")
# logging.info("����һ��info������־")
# logging.error("����һ��error������־")
# logging.critical("����һ��critical������־")

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s" #��ʽ����������
actime="%Y-%m-%d %H:%M:%S" #��ʽ��ʱ����ʾ��ʽ
logging.basicConfig(filename="test01.log",level=logging.INFO,format=LOG_FORMAT,datefmt=actime) #������־�����ļ��������ʽ
logging.debug("����һ��debug������־")
logging.warning("����һ��warn������־")
logging.info("����һ��info������־")
logging.error("����һ��error������־")
logging.critical("����һ��critical������־")