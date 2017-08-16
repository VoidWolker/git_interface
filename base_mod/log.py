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

    @staticmethod
    def set_logger():

        mutex = threading.Lock()
        mutex.acquire()

        set_logger = logging.getLogger(log_name)
        set_logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(log_format, date_fmt)

        # info日志格式
        info_filter = logging.Filter()
        info_filter.filter = lambda record: record.levelno == logging.INFO
        info_fh = logging.FileHandler(info_file)
        info_fh.setLevel(logging.INFO)
        info_fh.setFormatter(formatter)
        info_fh.addFilter(info_filter)

        # error日志格式
        error_filter = logging.Filter()
        error_filter.filter = lambda record: record.levelno > logging.INFO
        error_fh = logging.FileHandler(error_file)
        error_fh.setLevel(logging.WARN)
        error_fh.setFormatter(formatter)
        error_fh.addFilter(error_filter)

        set_logger.addHandler(info_fh)
        set_logger.addHandler(error_fh)

        mutex.release()
        return set_logger

logger = LogModule().set_logger()
