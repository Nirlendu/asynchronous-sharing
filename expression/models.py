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

        try:
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
        except Exception:
            log.exception('Could not create Expression')
        return

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

        try:
            log.debug('Expression Update operation')
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
        except Exception:
            log.exception('Could not Update Expression')
        return


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


# # TODO
# # Implement Image upload and URL share
# class DiscussionExpressionManager(models.Manager):
#     def store_discussion_expression(
#             self,
#             discussion_parent_id,
#             discussion_expression_owner_id,
#             discussion_expression_content,
#             discussion_expression_link_id=None,
#             discussion_expression_imagefile=None,
#             total_upvotes=0,
#             total_downvotes=0,
#     ):
#
#         log.info('IN - ' + sys._getframe().f_code.co_name)
#         log.info('FROM - ' + sys._getframe(1).f_code.co_name)
#         log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
#
#         try:
#             log.debug('Discussion Expression create operation')
#             discussion_expression = self.create(
#                 discussion_parent_id=discussion_parent_id,
#                 discussion_expression_owner_id=discussion_expression_owner_id,
#                 discussion_expression_content=discussion_expression_content,
#                 discussion_expression_link_id=discussion_expression_link_id,
#                 discussion_expression_imagefile=discussion_expression_imagefile,
#                 total_upvotes=total_upvotes,
#                 total_downvotes=total_downvotes,
#             )
#             return discussion_expression.id
#         except Exception:
#             log.exception('Could not create Discussion Expression')
#         return
#
#
# class Discussion_Expression(models.Model):
#     discussion_parent_id = models.CharField(
#         max_length=30,
#     )
#     discussion_expression_owner_id = models.CharField(
#         max_length=30,
#     )
#     discussion_expression_content = models.CharField(
#         max_length=10000,
#     )
#     discussion_expression_link_id = models.CharField(
#         max_length=30,
#         default=None,
#         null=True,
#     )
#     discussion_expression_imagefile = models.CharField(
#         max_length=30,
#         default=None,
#         null=True,
#     )
#     total_upvotes = models.IntegerField(
#         default=0,
#     )
#     total_downvotes = models.IntegerField(
#         default=0,
#     )
#     discussion_expression_updated = models.DateTimeField(
#         auto_now_add=True,
#     )
#     discussion_expression_created = models.DateTimeField(
#         auto_now_add=True,
#     )
#     objects = DiscussionExpressionManager()
#
#
#
#
#
#
#
#
#
#
# class LinkManager(models.Manager):
#     def store_link(
#             self,
#             link_url,
#             link_name,
#             link_desc=None,
#             link_image=None
#     ):
#
#         log.info('IN - ' + sys._getframe().f_code.co_name)
#         log.info('FROM - ' + sys._getframe(1).f_code.co_name)
#         log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
#         log.debug('Link create operation')
#
#         try:
#             Link.objects.update_or_create(
#                 link_url=link_url,
#                 link_name=link_name,
#                 link_desc=link_desc,
#                 link_image=link_image,
#             )
#         except Exception:
#             log.exception('Could not insert Link')
#         return
#
#
# class Link(models.Model):
#     link_url = models.CharField(
#         max_length=150,
#         unique=True,
#     )
#     link_name = models.CharField(
#         max_length=150,
#         null=False,
#     )
#     link_desc = models.CharField(
#         max_length=200,
#         default=None,
#         null=True,
#     )
#     link_image = models.CharField(
#         max_length=100,
#         default=None,
#         null=True,
#     )
#     link_updated = models.DateTimeField(
#         auto_now_add=True,
#     )
#     link_created = models.DateTimeField(
#         auto_now_add=True,
#     )
#     objects = LinkManager()