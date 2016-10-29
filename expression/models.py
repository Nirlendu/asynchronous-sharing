# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############

from __future__ import unicode_literals

import inspect
import sys

from django.db import models

from libs.logger import app_logger as log


class ExpressionPrimaryManager(models.Manager):
    def create_expression(
            self,
            expression_owner_id,
            expression_content,
            expression_content_url=None,
            expression_imagefile=None,
            broadcast_parent_id=None,
            expression_weight=0,
            total_upvotes=0,
            total_collects=0,
            total_broadcasts=0,
            total_discussions=0,
    ):

        log.info('IN - ' + sys._getframe().f_code.co_name)
        log.info('FROM - ' + sys._getframe(1).f_code.co_name)
        log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

        log.debug('Expression create operation')
        expression = self.create(
            expression_owner_id=expression_owner_id,
            expression_content=expression_content,
            expression_content_url=expression_content_url,
            expression_imagefile=expression_imagefile,
            broadcast_parent_id=broadcast_parent_id,
            expression_weight=expression_weight,
            total_upvotes=total_upvotes,
            total_collects=total_collects,
            total_broadcasts=total_broadcasts,
            total_discussions=total_discussions,
        )
        return expression.id

    def update_expression(
            self,
            expression_owner_id,
            expression_content,
            expression_content_url=None,
            expression_imagefile=None,
            expression_weight=0,
            broadcast_parent_id=None,
            total_upvotes=0,
            total_collects=0,
            total_broadcasts=0,
            total_discussions=0,
    ):

        log.info('IN - ' + sys._getframe().f_code.co_name)
        log.info('FROM - ' + sys._getframe(1).f_code.co_name)
        log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

        expression = self.update_or_create(
            expression_owner_id=expression_owner_id,
            expression_content=expression_content,
            expression_content_url=expression_content_url,
            expression_imagefile=expression_imagefile,
            broadcast_parent_id=broadcast_parent_id,
            expression_weight=expression_weight,
            total_upvotes=total_upvotes,
            total_collects=total_collects,
            total_broadcasts=total_broadcasts,
            total_discussions=total_discussions,
        )
        return expression.id


class ExpressionPrimary(models.Model):
    expression_owner_id = models.CharField(
        max_length=12,
    )
    expression_content = models.CharField(
        max_length=10000,
    )
    expression_content_url = models.CharField(
        max_length=100,
        default=None,
        null=True,
    )
    expression_imagefile = models.CharField(
        max_length=100,
        default=None,
        null=True,
    )
    expression_weight = models.DecimalField (
        default=0,
        max_digits=15,
        decimal_places=10
    )
    broadcast_parent_id = models.CharField(
        max_length=20,
        default=None,
        null=True,
    )
    total_upvotes = models.IntegerField(
        default=0,
    )
    total_broadcasts = models.IntegerField(
        default=0,
    )
    total_discussions = models.IntegerField(
        default=0,
    )
    total_collects = models.IntegerField(
        default=0,
    )
    expression_updated = models.DateTimeField(
        auto_now_add=True,
    )
    expression_created = models.DateTimeField(
        auto_now_add=True,
    )
    objects = ExpressionPrimaryManager()