# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import inspect
import sys

from django.db import models
# from neomodel import (StructuredNode, IntegerProperty,
#                       RelationshipTo, RelationshipFrom)

#from app_base.models import Person, Topic
from libs.logger import app_logger as log


# class ExpressionGraph(StructuredNode):
#     expression_id = IntegerProperty(unique_index=True)
#     expression_owner = RelationshipFrom(Person, 'EXPRESSED')
#     broadcast_of = RelationshipTo('ExpressionGraph', 'BROADCAST_OF')
#     upvoter = RelationshipFrom(Person, 'UPVOTED')
#     downvoter = RelationshipFrom(Person, 'DOWNVOTED')
#     in_topic = RelationshipTo(Topic, 'IN_TOPIC')


class ExpressionManager(models.Manager):
    def store_expression(
            self,
            expression_owner_id,
            expression_content,
            expression_link_id=None,
            expression_imagefile=None,
            broadcast_parent_id=None,
            total_upvotes=0,
            total_downvotes=0,
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
                expression_link_id=expression_link_id,
                expression_imagefile=expression_imagefile,
                broadcast_parent_id=broadcast_parent_id,
                total_upvotes=total_upvotes,
                total_downvotes=total_downvotes,
                total_broadcasts=total_broadcasts,
                total_discussions=total_discussions,
            )
            return expression.id
        except Exception:
            log.exception('Could not create Expression')
        return


class Expression(models.Model):
    expression_owner_id = models.CharField(
        max_length=30,
    )
    expression_content = models.CharField(
        max_length=10000,
    )
    expression_link_id = models.CharField(
        max_length=30,
        default=None,
        null=True,
    )
    expression_imagefile = models.CharField(
        max_length=30,
        default=None,
        null=True,
    )
    broadcast_parent_id = models.CharField(
        max_length=30,
        default=None,
        null=True,
    )
    total_upvotes = models.IntegerField(
        default=0,
    )
    total_downvotes = models.IntegerField(
        default=0,
    )
    total_broadcasts = models.IntegerField(
        default=0,
    )
    total_discussions = models.IntegerField(
        default=0,
    )
    expression_updated = models.DateTimeField(
        auto_now_add=True,
    )
    expression_created = models.DateTimeField(
        auto_now_add=True,
    )
    objects = ExpressionManager()


# TODO
# Implement Image upload and URL share
class DiscussionExpressionManager(models.Manager):
    def store_discussion_expression(
            self,
            discussion_parent_id,
            discussion_expression_owner_id,
            discussion_expression_content,
            discussion_expression_link_id=None,
            discussion_expression_imagefile=None,
            total_upvotes=0,
            total_downvotes=0,
    ):

        log.info('IN - ' + sys._getframe().f_code.co_name)
        log.info('FROM - ' + sys._getframe(1).f_code.co_name)
        log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

        try:
            log.debug('Discussion Expression create operation')
            discussion_expression = self.create(
                discussion_parent_id=discussion_parent_id,
                discussion_expression_owner_id=discussion_expression_owner_id,
                discussion_expression_content=discussion_expression_content,
                discussion_expression_link_id=discussion_expression_link_id,
                discussion_expression_imagefile=discussion_expression_imagefile,
                total_upvotes=total_upvotes,
                total_downvotes=total_downvotes,
            )
            return discussion_expression.id
        except Exception:
            log.exception('Could not create Discussion Expression')
        return


class Discussion_Expression(models.Model):
    discussion_parent_id = models.CharField(
        max_length=30,
    )
    discussion_expression_owner_id = models.CharField(
        max_length=30,
    )
    discussion_expression_content = models.CharField(
        max_length=10000,
    )
    discussion_expression_link_id = models.CharField(
        max_length=30,
        default=None,
        null=True,
    )
    discussion_expression_imagefile = models.CharField(
        max_length=30,
        default=None,
        null=True,
    )
    total_upvotes = models.IntegerField(
        default=0,
    )
    total_downvotes = models.IntegerField(
        default=0,
    )
    discussion_expression_updated = models.DateTimeField(
        auto_now_add=True,
    )
    discussion_expression_created = models.DateTimeField(
        auto_now_add=True,
    )
    objects = DiscussionExpressionManager()


class LinkManager(models.Manager):
    def store_link(
            self,
            link_url,
            link_name,
            link_desc=None,
            link_image=None
    ):

        log.info('IN - ' + sys._getframe().f_code.co_name)
        log.info('FROM - ' + sys._getframe(1).f_code.co_name)
        log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
        log.debug('Link create operation')

        try:
            Link.objects.update_or_create(
                link_url=link_url,
                link_name=link_name,
                link_desc=link_desc,
                link_image=link_image,
            )
        except Exception:
            log.exception('Could not insert Link')
        return


class Link(models.Model):
    link_url = models.CharField(
        max_length=150,
        unique=True,
    )
    link_name = models.CharField(
        max_length=150,
        null=False,
    )
    link_desc = models.CharField(
        max_length=200,
        default=None,
        null=True,
    )
    link_image = models.CharField(
        max_length=60,
        default=None,
        null=True,
    )
    link_updated = models.DateTimeField(
        auto_now_add=True,
    )
    link_created = models.DateTimeField(
        auto_now_add=True,
    )
    objects = LinkManager()
