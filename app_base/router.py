class AppBaseRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read app_base models go to postgres.
        """
        if model._meta.app_label == 'app_base':
            return 'postgres'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write app_base models go to postgres.
        """
        if model._meta.app_label == 'app_base':
            return 'postgres'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the app_base app is involved.
        """
        if obj1._meta.app_label == 'app_base' or \
           obj2._meta.app_label == 'app_base':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the app_base app only appears in the 'postgres'
        database.
        """
        if app_label == 'app_base':
            return db == 'postgres'
        return None