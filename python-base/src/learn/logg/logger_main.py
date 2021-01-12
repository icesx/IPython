# Copyright (C)
# Author: I
# Contact: 12157724@qq.com


import logging.handlers

from learn.logg.logger_creater import logger

if __name__ == '__main__':
    logger.info("xx")
    logger.info("my name is %s", "icesx")
    logger.info("my name is 2 %s" % "icesx")
