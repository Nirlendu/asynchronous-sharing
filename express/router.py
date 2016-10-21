class ExpressRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """

    @staticmethod
    def db_for_read(self, model, **hints):
        """
        Attempts to read express models go to cassandra.
        """
        if model._meta.app_label == 'express':
            return 'cassandra'
        return None

    @staticmethod
    def db_for_write(model, **hints):
        """
        Attempts to write express models go to cassandra.
        """
        if model._meta.app_label == 'express':
            return 'cassandra'
        return None

    @staticmethod
    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the express app is involved.
        """
        if obj1._meta.app_label == 'express' or \
           obj2._meta.app_label == 'express':
           return True
        return None

    @staticmethod
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the express app only appears in the 'cassandra'
        database.
        """
        if app_label == 'express':
            return db == 'cassandra'
        return None