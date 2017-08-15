#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

"""
log config
created by VoidWalker in 2017.8.15
"""

info_file = r"../log/infoLog.txt"
error_file = r"../log/errorLog.txt"
debug_file = r"../log/debugLog.txt"
warning_file = r"../log/warningLog.txt"
critical_file = r"../log/criticalLog.txt"

log_format = r"%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s : %(message)s"

date_fmt = "%Y-%m-%d %H:%M:%S"

log_name = "test_logger"
