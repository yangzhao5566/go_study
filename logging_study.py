# logging模块
import logging   # 默认基本为warning
# logging.warning("222")
# logging.info("bbbb")

#  几个概念
# Logger 记录器， 暴露了应用程序代码能直接使用的接口
# Handler 处理器， 将（记录去产生的）日志记录发送至合适的目的地
# Filter 过滤器，提供了更好的力度控制，它可以决定输出哪些日志记录
# Formatter 格式化器，指明了最终输出中日志记录的布局

# ######### 使用示例 ##############
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
# handler = logging.StreamHandler()
# handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s %(filename)s \
# [line: %(lineno)d] %(levelname)s: %(message)s')
# formatter.datefmt = '%Y%m%d %H:%M:%S'
# handler.setFormatter(formatter)
# logger.addHandler(handler)

"""
logger是一个树形层级结构，是用之前必须创建一个记录器， 
如没创建，则会默认创建一个root logger
"""
logger = logging.getLogger(__name__)

"""创建以后， 可以使用如下方法进行日志级别设置
ogger.setLevel(logging.ERROR) # 设置日志级别为ERROR，即只有日志级别大于等于ERROR的日志才会输出
logger.addHandler(handler_name) # 为Logger实例增加一个处理器
logger.removeHandler(handler_name) # 为Logger实例删除一个处理器
"""
logger.setLevel(logging.debug)  # 设置成debug级别

"""Handler 处理器类型有多种 常用的有 StreamHandler FileHandler NullHandler
创建StreamHandler之后，可以通过使用以下方法设置日志级别，
设置格式化器Formatter，增加或删除过滤器Filter
"""

sh = logging.StreamHandler(stream=None)

# 各种方法
# sh.setLevel(logging.warn) # 指定日志级别
# ch.setFormatter(formatter_name) # 设置一个格式化formatter
# ch.addFilter(filter_name) # 增加一个过滤器，可以增加多个
# ch.removeFilter(filter_name)

# fh = logging.FileHandler(filename, mode='a',encoding=None, delay=False)

"""
Formatter 格式化器
使用Formatter对象设置日志信息最后的规则、结构和内容，默认的时间格式为%Y-%m-%d %H:%M:%S。
"""
formatter = logging.Formatter(fmt=None, datefmt=None)

"""fmt是消息的格式化字符串，datefmt是日期字符串。如果不指明fmt，
将使用'%(message)s'。如果不指明datefmt，将使用ISO8601日期格式
"""


#  一个logger下可以有多个Filter  多个Handler 一个handler 对应一个 Formater

