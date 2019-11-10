# Copyright (C)
# Author: I
# Contact: 12157724@qq.com


import logging.handlers

from cn.i.xportal.logg import logger_creater

if __name__ == '__main__':
    logger_creater.init_log()
    logger_creater.init_log("mylogger")
    logger = logging.getLogger()
    logger.info("xx")
    logging.info("my name is %s","icesx")
    logging.getLogger("mylogger").info("yy")
