import sys
from datetime import datetime
from pathlib import Path
from loguru import logger
from config.path_conf import output_path
from threading import Lock


class Logger:
    instance = None
    lock = Lock()

    """日志锁"""

    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if cls.instance is None:
                cls.instance = super().__new__(cls)
                cls.instance._initialized = False
            return cls.instance


    def __init__(self):
        with self.lock:
            if not self._initialized:
                # 移除默认配置
                logger.remove()
                self._lg = logger
                # 配置新的日志
                ## 初始化日志批次目录
                self.current_date = None
                self.current_round = None
                self.current_round_log_storage_path = None
                self.log_name = None

                self.initialize()
                self._initialized = True


    def initialize(self):
        # 配置新的 logger
        # {time: YYYY - MM - DD HH: mm: ss} | {level} | {file} | {function} | {line} | {message}
        log_format = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"

        ## 输出到终端
        self._lg.add(sys.stdout, level="DEBUG", format=log_format)

        ## 输出到文件
        ### 当天日志目录，如果此目录不存在则创建目录，使用 pathlib 实现而不是 os
        self.current_date = datetime.now().strftime("%Y-%m-%d")
        current_day_log_storage_path = output_path.joinpath(self.current_date)
        current_day_log_storage_path.mkdir(parents=True, exist_ok=True)

        ### 当前轮次日志目录
        self.current_round = datetime.now().strftime("%H-%M-%S")
        self.current_round_log_storage_path = current_day_log_storage_path.joinpath(self.current_round)
        self.current_round_log_storage_path.mkdir(parents=True, exist_ok=True)

        ### 日志文件路径
        self.log_name = datetime.now().strftime("%Y%m%d-%H%M%S")
        log_file_path = self.current_round_log_storage_path.joinpath(self.log_name + ".log")
        self._lg.add(log_file_path, level="DEBUG", rotation="00:00", retention="7 days", compression="zip",
                     format=log_format)


    def get_logger(self):

        """返回日志对象实例"""

        return self._lg


    def get_current_date(self):

        """获取档期日期字符串"""

        return self.current_date


    def get_current_round(self):

        """获取当日轮次，日期时间字符串"""

        return self.current_round


    def get_the_datetime_of_the_log_name(self):

        """获取日志名称的日期时间部分"""

        return self.log_name

    def get_current_round_log_storage_path(self) -> Path:

        """获取当前轮次日志存储路径"""

        return self.current_round_log_storage_path