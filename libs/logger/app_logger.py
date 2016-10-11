# -*- coding: utf-8 -*-

import logging


def init():
    filename = 'logs/app.log'
    logging.basicConfig(filename=filename,
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)
    return


def info(log_string):
    try:
        init()
        logging.info('########### ' + log_string + ' ###########')
    except:
       pass
    return


def debug(log_string):
    try:
        init()
        logging.debug('########### ' + log_string + ' ###########')
    except:
        pass
    return


def exception(log_string):
    try:
        init()
        logging.exception('########### ' + log_string + ' ###########')
    except:
        pass
    return
