#!/usr/bin/env python
import sys

import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.local")
    if os.environ['DJANGO_SETTINGS_MODULE'] == 'core.settings.local':
        try:
            os.environ['GRAPH_DATABASE_URL']
        except:
            os.environ['GRAPH_DATABASE_URL'] = 'http://localhost:7474/'
        try:
            os.environ['DATABASE_URL']
        except:
            os.environ['DATABASE_URL'] = 'localhost'
    if os.environ['DJANGO_SETTINGS_MODULE'] == 'core.settings.heroku':
        try:
            os.environ['GRAPH_DATABASE_URL']
        except:
            try:
                os.environ['GRAPH_DATABASE_URL'] = os.environ['GRAPHENEDB_URL']
            except:
                raise Exception
        if not os.environ['DATABASE_URL']:
            raise Exception
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
