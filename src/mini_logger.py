#!/usr/bin/env python3

# Copyright 2025 (author: lamnt45)


# common
import os


# technical
import logging
from booleanify import booleanify



### FUNCTIONS
def getLogger(
    name      : str,
    log_level : int | str | None = None,
    log_time  : bool | None = None,
) -> logging.Logger:

    logger = logging.Logger(name)
    logger_sole_handler = logging.StreamHandler()

    log_level = log_level or os.environ.get('LOG_LEVEL', 'INFO')
    logger.setLevel(log_level)

    if log_time is None:
        log_time = booleanify(os.environ.get('HU_LOG_TIME', True))

    if log_time:
        log_time_str_fmt = r'%(asctime)s '
    else:
        log_time_str_fmt = ''

    process_level = int(os.environ.get('PROCESS_LEVEL', 0))
    format_str = r'{0}{1}<%(name)s> {2}{3}%(message)s'.format(
        '\033' + '[38;5;243m',
        log_time_str_fmt,
        '└───' * process_level,
        '\033' + '[0m',
    )

    logger_sole_handler.setFormatter(logging.Formatter(format_str))
    logger.handlers = [logger_sole_handler]

    return logger
