class AppBaseRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """

    @staticmethod
    def db_for_read(self, model, **hints):
        """
        Attempts to read app_base models go to cassandra.
        """
        if model._meta.app_label == 'app_base':
            return 'cassandra'
        return None

    @staticmethod
    def db_for_write(model, **hints):
        """
        Attempts to write app_base models go to cassandra.
        """
        if model._meta.app_label == 'app_base':
            return 'cassandra'
        return None

    @staticmethod
    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the app_base app is involved.
        """
        if obj1._meta.app_label == 'app_base' or \
           obj2._meta.app_label == 'app_base':
           return True
        return None

    @staticmethod
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the app_base app only appears in the 'cassandra'
        database.
        """
        if app_label == 'app_base':
            return db == 'cassandra'
        return None