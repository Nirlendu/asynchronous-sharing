# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import inspect
import sys

from libs.logger import app_logger as log

from django.db.models import Model as ModelPostgres


##
#
# Channel Primary Manager
#
##
class ChannelPrimaryManager(ModelPostgres):
    def create_channel(
            self,
            channel_name,
            total_followers
        ):
        log.info('IN - ' + sys._getframe().f_code.co_name)
        log.info('FROM - ' + sys._getframe(1).f_code.co_name)
        log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

        try:
            log.debug('Channel create operation')
            channel = self.create(
                channel_name=channel_name,
                total_followers=total_followers,
            )
            return channel.id
        except Exception:
            log.exception('Could not create Channel')
        return

    def create_channel(
            self,
            channel_name,
            total_followers
        ):
        log.info('IN - ' + sys._getframe().f_code.co_name)
        log.info('FROM - ' + sys._getframe(1).f_code.co_name)
        log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

        try:
            log.debug('Channel update operation')
            channel = self.update_or_create(
                channel_name=channel_name,
                total_followers=total_followers,
            )
            return channel.id
        except Exception:
            log.exception('Could not update Channel')
        return

##
#
# Channel Primary
#
##
class ChannelPrimary(ModelPostgres):
    channel_name  = models.CharField(
        max_length=30,
    )
    total_followers = models.IntegerField(
        default=0,
    )
    channel_created = models.DateTimeField(
        auto_now_add=True,
    )
    channel_updated = models.DateTimeField(
        auto_now_add=True,
    )
    object = ChannelPrimaryManager()


##
#
# Channel Channel Relation Manager
#
##
class ChannelChannelRelationManager(ModelPostgres):
    def create_channel_channel_relation(
            self,
            channel_one_id,
            channel_two_id
        ):
        log.info('IN - ' + sys._getframe().f_code.co_name)
        log.info('FROM - ' + sys._getframe(1).f_code.co_name)
        log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

        try:
            log.debug('Channel Channel Relation create operation')
            channel_relation = self.create(
                channel_one_id=channel_one_id,
                channel_two_id=channel_two_id,
            )
            return channel_relation.id
        except Exception:
            log.exception('Could not create Channel Channel Relation')
        return

##
#
# Channel Channel Relation
#
##
class ChannelChannelRelation(ModelPostgres):
    channel_one_id = models.CharField(
        max_length=30,
    )
    channel_two_id = models.CharField(
        max_length=30,
    )

    class Meta:
        unique_together = ('channel_one_id', 'channel_two_id',)

    object = ChannelChannelRelationManager()

##
#
# Channel Person Relation Manager
#
##
class ChannelPersonRelationManager(ModelPostgres):
    def create_channel_channel_relation(
            self,
            channel_id,
            person_id
        ):
        log.info('IN - ' + sys._getframe().f_code.co_name)
        log.info('FROM - ' + sys._getframe(1).f_code.co_name)
        log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

        try:
            log.debug('Channel Person Relation create operation')
            channel_relation = self.create(
                channel_id=channel_id,
                person_id=person_id,
            )
            return channel_relation.id
        except Exception:
            log.exception('Could not create Channel Person Relation')
        return

###
#
# Channel Person Relation
#
##
class ChannelPersonRelation(ModelPostgres):
    channel_id = models.CharField(
        max_length=30,
    )
    person_id = models.CharField(
        max_length=30,
    )

    class Meta:
        unique_together = ('channel_id', 'person_id',)

    object = ChannelPersonRelationManager()