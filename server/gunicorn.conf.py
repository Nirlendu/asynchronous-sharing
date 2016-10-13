# BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
bind = '127.0.0.1:8000'  # Don't use port 80 becaue nginx occupied it already. Don't change it even in prod

# errorlog = os.path.join(os.path.dirname(__file__), 'server_logs/gunicorn-error.log')
errorlog = '/Users/nirlendu/Documents/Codes/myApp/server/server_logs/gunicorn-error.log'  # Make sure you have the log folder create

# accesslog = os.path.join(os.path.dirname(__file__), 'server_logs/gunicorn-access.log')
accesslog = '/Users/nirlendu/Documents/Codes/myApp/server/server_logs/gunicorn-access.log'

loglevel = 'debug'

workers = 1  # the number of recommended workers is '2 * number of CPUs + 1'
