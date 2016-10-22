# -*- coding: utf-8 -*-

class channelRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read channel models go to postgres.
        """
        if model._meta.app_label == 'channel':
            return 'postgres'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write channel models go to postgres.
        """
        if model._meta.app_label == 'channel':
            return 'postgres'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the channel app is involved.
        """
        if obj1._meta.app_label == 'channel' or \
           obj2._meta.app_label == 'channel':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the channel app only appears in the 'postgres'
        database.
        """
        if app_label == 'channel':
            return db == 'postgres'
        return None