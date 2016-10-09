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
    except:
        touch 'logs/app.log'
    logging.info('########### ' + log_string + ' ###########')
    return


def debug(log_string):
    try:
        init()
    except:
        touch 'logs/app.log'
    logging.debug('########### ' + log_string + ' ###########')
    return


def exception(log_string):
    try:
        init()
    except:
        touch 'logs/app.log'
    logging.exception('########### ' + log_string + ' ###########')
    return
