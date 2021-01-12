# coding:utf-8
# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import logging
import logging.handlers


def init_log(name="LOG",
             file="LOG.log",
             backup_count=7,
             fmt="%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s"):
    __logger = logging.getLogger(name)
    __logger.setLevel(logging.INFO)
    rf_handler = logging.handlers.TimedRotatingFileHandler(file,
                                                           when='MIDNIGHT',
                                                           interval=1,
                                                           backupCount=backup_count)
    formatter = logging.Formatter(fmt=fmt)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    rf_handler.setFormatter(formatter)
    __logger.addHandler(rf_handler)
    __logger.addHandler(ch)
    return logging.getLogger(name)


logger = init_log()
