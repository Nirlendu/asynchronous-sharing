class SqlBackupRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """

    @staticmethod
    def db_for_read(self, model, **hints):
        """
        Attempts to read sql_backup models go to postgres.
        """
        if model._meta.app_label == 'sql_backup':
            return 'postgres'
        return None

    @staticmethod
    def db_for_write(model, **hints):
        """
        Attempts to write sql_backup models go to postgres.
        """
        if model._meta.app_label == 'sql_backup':
            return 'postgres'
        return None

    @staticmethod
    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the sql_backup app is involved.
        """
        if obj1._meta.app_label == 'sql_backup' or \
           obj2._meta.app_label == 'sql_backup':
           return True
        return None

    @staticmethod
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the sql_backup app only appears in the 'postgres'
        database.
        """
        if app_label == 'sql_backup':
            return db == 'postgres'
        return None