# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import inspect
import sys

from libs.logger import app_logger as log

from django.db import models


##
#
# Channel Primary Manager
#
##
class ChannelPrimaryManager(models.Manager):
    def create_channel(
            self,
            channel_name,
            total_followers,
            channel_weight
        ):
        log.info('IN - ' + sys._getframe().f_code.co_name)
        log.info('FROM - ' + sys._getframe(1).f_code.co_name)
        log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

        try:
            log.debug('Channel create operation')
            channel = self.create(
                channel_name=channel_name,
                total_followers=total_followers,
                channel_weight=channel_weight,
            )
            return channel.id
        except Exception:
            log.exception('Could not create Channel')
        return

    def update_channel(
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
                channel_weight=channel_weight,
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
class ChannelPrimary(models.Model):
    channel_name  = models.CharField(
        max_length=30,
    )
    total_followers = models.IntegerField(
        default=0,
    )
    channel_weight = models.DecimalField (
        default=0,
        max_digits=15,
        decimal_places=10
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
class ChannelChannelRelationManager(models.Manager):
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
class ChannelChannelRelation(models.Model):
    channel_one_id = models.CharField(
        max_length=8,
    )
    channel_two_id = models.CharField(
        max_length=8,
    )

    class Meta:
        unique_together = ('channel_one_id', 'channel_two_id',)

    object = ChannelChannelRelationManager()

##
#
# Channel Person Relation Manager
#
##
class ChannelPersonRelationManager(models.Manager):
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
class ChannelPersonRelation(models.Model):
    channel_id = models.CharField(
        max_length=8,
    )
    person_id = models.CharField(
        max_length=12,
    )

    class Meta:
        unique_together = ('channel_id', 'person_id',)

    object = ChannelPersonRelationManager()


##
#
# Expression Channel Relation Manager
#
##
class ExpressionChannelRelationManager(models.Manager):
    def create_expression_channel_relation(
            self,
            channel_id,
            expression_id
        ):
        log.info('IN - ' + sys._getframe().f_code.co_name)
        log.info('FROM - ' + sys._getframe(1).f_code.co_name)
        log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

        try:
            log.debug('Expression Channel Relation create operation')
            expression_channel_relation = self.create(
                channel_id=channel_id,
                expression_id=expression_id,
            )
            return expression_channel_relation.id
        except Exception:
            log.exception('Could not create Expression Channel Relation')
        return

##
#
# Expression Channel Relation
#
##
class ExpressionChannelRelation(models.Model):
    channel_id = models.CharField(
        max_length=8,
    )
    expression_id = models.CharField(
        max_length=20,
    )

    class Meta:
        unique_together = ('channel_id', 'expression_id',)

    object = ExpressionChannelRelationManager()