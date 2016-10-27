# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############

import inspect
import sys
import urllib
import uuid

import os
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

import core_logic as core
from libs.image_processor import compressimages
from libs.logger import app_logger as log



def new_person(
        user_name,
        person_name,
        total_followers=0,
        person_weight=0,
        person_channel_followee_list=[],
        person_person_followee_list=[],
        person_expression_list=[],
    ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('new person interface..')

    return core.new_person_logic(
        user_name=user_name,
        person_name=person_name,
        total_followers=total_followers,
        person_weight=person_weight,
        person_channel_followee_list=person_channel_followee_list,
        person_person_followee_list=person_person_followee_list,
        person_expression_list=person_expression_list,
    )


def new_channel(
    channel_name,
    channel_unique_name,
    channel_weight=0,
    total_followers=0,
    channel_expression_list=[],
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New Channel interface..')

    return core.new_channel_logic(
        channel_name=channel_name,
        channel_unique_name=channel_unique_name,
        channel_weight=channel_weight,
        total_followers=total_followers,
        channel_expression_list=channel_expression_list,
    )

def channel_person_relation(
        channel_id,
        person_id,
    ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Channel Person Relation interface..')

    return core.channel_person_relation_logic(
        channel_id=channel_id,
        person_id=person_id,
    )

def get_expressions(
            person_id,
        ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Fetching expressions interface..')

    return core.get_expressions_logic(
        person_id=person_id,
    )


def new_expression(
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
        channels=[],
    ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New Expression Interface')

    # TODO
    # 1) Parse the contents and do some stuff
    # 2) Determine appropriate topics not provided
    return core.new_expression_logic(
        expression_owner_id=expression_owner_id,
        expression_content=expression_content,
        expression_content_url=expression_content_url,
        expression_imagefile=expression_imagefile,
        expression_weight=expression_weight,
        broadcast_parent_id=broadcast_parent_id,
        total_upvotes=total_upvotes,
        total_collects=total_collects,
        total_broadcasts=total_broadcasts,
        total_discussions=total_discussions,
        channels=channels,
    )


def store_url_interface(
        url,
        url_title,
        url_desc=None,
        url_imagefile=None,
        url_weight=0,
):
    # TODO
    # Some checks on the url
    # Some data about the url

    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New URL INSERT')

    return core.store_url_logic(
        url=url,
        url_title=url_title,
        url_desc=url_desc,
        url_imagefile=url_imagefile,
        url_weight=url_weight,
    )


def find_url_id(url):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Find URL')

    return core.find_url_id_logic(url=url)


# def new_broadcast(
#         broadcast_owner_id,
#         broadcast_content,
#         broadcast_parent_id,
#         expression_link_id=None,
#         expression_imagefile=None,
#         total_upvotes=0,
#         total_downvotes=0,
#         total_broadcasts=0,
#         total_discussions=0,
#         topics=[],
# ):
#     log.info('IN - ' + sys._getframe().f_code.co_name)
#     log.info('FROM - ' + sys._getframe(1).f_code.co_name)
#     log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
#     log.debug('New Broadcast Interface')
#
#     return core.new_broadcast_logic(
#         broadcast_owner_id=broadcast_owner_id,
#         broadcast_content=broadcast_content,
#         expression_link_id=expression_link_id,
#         expression_imagefile=expression_imagefile,
#         broadcast_parent_id=broadcast_parent_id,
#         total_upvotes=total_upvotes,
#         total_downvotes=total_downvotes,
#         total_broadcasts=total_broadcasts,
#         total_discussions=total_discussions,
#         topics=topics,
#     )
#
#
# def new_discussion_expression(
#         discussion_parent_id,
#         discussion_expression_owner_id,
#         discussion_expression_content,
#         discussion_expression_link_id=None,
#         discussion_expression_imagefile=None,
#         total_upvotes=0,
#         total_downvotes=0,
# ):
#     log.info('IN - ' + sys._getframe().f_code.co_name)
#     log.info('FROM - ' + sys._getframe(1).f_code.co_name)
#     log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
#     log.debug('New discussion expression Interface')
#
#     return core.new_discussion_expression_logic(
#         discussion_parent_id=discussion_parent_id,
#         discussion_expression_owner_id=discussion_expression_owner_id,
#         discussion_expression_content=discussion_expression_content,
#         discussion_expression_link_id=discussion_expression_link_id,
#         discussion_expression_imagefile=discussion_expression_imagefile,
#         total_upvotes=total_upvotes,
#         total_downvotes=total_downvotes,
#     )
#
#
# def upvote_expression(
#         upvoter,
#         expression_id,
# ):
#     log.info('IN - ' + sys._getframe().f_code.co_name)
#     log.info('FROM - ' + sys._getframe(1).f_code.co_name)
#     log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
#     log.debug('Upvote expression Interface')
#
#     return core.upvote_expression_logic(
#         upvoter=upvoter,
#         expression_id=expression_id,
#     )
#
#
# def downvote_expression(
#         downvoter,
#         expression_id,
# ):
#     log.info('IN - ' + sys._getframe().f_code.co_name)
#     log.info('FROM - ' + sys._getframe(1).f_code.co_name)
#     log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
#     log.debug('Downvote expression Interface')
#
#     return core.downvote_expression_logic(
#         downvoter=downvoter,
#         expression_id=expression_id,
#     )
