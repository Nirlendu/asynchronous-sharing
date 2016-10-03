import logging

def log(log_string):
	logging.basicConfig(filename='logs/app.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
	logging.info('###########' + log_string + '###########')
	return
