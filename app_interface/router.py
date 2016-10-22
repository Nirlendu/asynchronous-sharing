class app_interfaceRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read app_interface models go to cassandra.
        """
        if model._meta.app_label == 'app_interface':
            return 'cassandra'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write app_interface models go to cassandra.
        """
        if model._meta.app_label == 'app_interface':
            return 'cassandra'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the app_interface app is involved.
        """
        if obj1._meta.app_label == 'app_interface' or \
           obj2._meta.app_label == 'app_interface':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the app_interface app only appears in the 'cassandra'
        database.
        """
        if app_label == 'app_interface':
            return db == 'cassandra'
        return None