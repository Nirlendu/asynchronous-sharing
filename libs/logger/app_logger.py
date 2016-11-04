# -*- coding: utf-8 -*-

import os, logging, sys, inspect


def init():
    filename = 'logs/app.log'
    logging.basicConfig(filename=filename,
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)
    return


def info(log_string):
    if os.environ['DJANGO_SETTINGS_MODULE'] == 'core.settings.local':
        try:
            init()
            logging.info('IN - ' + sys._getframe(1).f_code.co_name)
            logging.info('FROM - ' + sys._getframe(2).f_code.co_name)
            logging.info('HAS - ' + str(inspect.getargvalues(sys._getframe(1))))
            logging.info('########### ' + log_string + ' ###########')
        except:
           pass
    return


def debug(log_string):
    if os.environ['DJANGO_SETTINGS_MODULE'] == 'core.settings.local':
        try:
            init()
            logging.info('IN - ' + sys._getframe(1).f_code.co_name)
            logging.info('FROM - ' + sys._getframe(2).f_code.co_name)
            logging.info('HAS - ' + str(inspect.getargvalues(sys._getframe(1))))
            logging.debug('########### ' + log_string + ' ###########')
        except:
            pass
    return


def exception(log_string):
    if os.environ['DJANGO_SETTINGS_MODULE'] == 'core.settings.local':
        try:
            init()
            logging.info('IN - ' + sys._getframe(1).f_code.co_name)
            logging.info('FROM - ' + sys._getframe(2).f_code.co_name)
            logging.info('HAS - ' + str(inspect.getargvalues(sys._getframe(1))))
            logging.exception('########### ' + log_string + ' ###########')
        except:
            pass
    return
