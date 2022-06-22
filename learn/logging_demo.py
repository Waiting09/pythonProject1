import logging

# logging.debug()  细节信息，仅当诊断问题时使用
# logging.info()   确认程序按预期运行
# logging.warning() 表明有已经或即将发生的意外（例如：磁盘空间不足）。程序仍按预期进行
# logging.error()  由于严重的问题，程序的某些功能已经不能正常执行
# logging.critical() 严重的错误，表明程序已不能继续执行

# 设置日志级别,设置成为哪个级别，就会打印这个级别及以上级别的日志
# logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
#
# logging.debug("这是debug级别的日志")
# logging.info("这是info级别的日志")
# logging.warning("这是warning级别的日志")
# logging.error("这是error级别的日志")
# logging.critical("这是critical级别的日志")

# 记录日志到文件  filename="example.log"
# 时间  format='%(asctime)s %(message)s'
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s', filename="example.log", )
logging.debug("这是debug级别的日志")
logging.info("这是info级别的日志")
logging.warning("这是warning级别的日志")
logging.error("这是error级别的日志")
logging.critical("这是critical级别的日志")
