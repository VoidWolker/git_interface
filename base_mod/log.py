#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
log module
create by VoidWalker in 2017.8.3
"""

import logging
import threading
from config.log_config import info_file
from config.log_config import error_file
from config.log_config import log_format
from config.log_config import log_name
from config.log_config import date_fmt


class LogModule:

    def __init__(self):
        pass

    def set_logger(self):

        mutex = threading.Lock()
        mutex.acquire()

        logger = logging.getLogger(log_name)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(log_format, date_fmt)

        # info日志格式
        info_fh = logging.FileHandler(info_file)
        info_fh.setLevel(logging.DEBUG)
        info_fh.setFormatter(formatter)

        # error日志格式
        error_fh = logging.FileHandler(error_file)
        error_fh.setLevel(logging.WARN)
        error_fh.setFormatter(formatter)

        logger.addHandler(info_fh)
        logger.addHandler(error_fh)

        mutex.release()
        return logger

logger = LogModule().set_logger()
