# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
import logging
import logging.handlers


def init_log(name=""):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    rf_handler = logging.handlers.TimedRotatingFileHandler('all.log',when='MIDNIGHT',interval=1,backupCount=7)
    rf_handler.setFormatter(logging.Formatter(fmt='%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'))
    logger.addHandler(rf_handler)
