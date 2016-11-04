# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############
"""
    This module contains functions that are for core interface.

    :Copyright: (c) 2016 by Nirlendu Saha
"""

import urllib, uuid, os


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
    """New person

    :param user_name:
    :param person_name:
    :param total_followers:
    :param person_weight:
    :param person_channel_followee_list:
    :param person_person_followee_list:
    :param person_expression_list:
    :return:
    """
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
    """New channel

    :param channel_name:
    :param channel_unique_name:
    :param channel_weight:
    :param total_followers:
    :param channel_expression_list:
    :return:
    """
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
    """New Channel Person Relation

    :param channel_id:
    :param person_id:
    :return:
    """
    log.debug('Channel Person Relation interface..')

    return core.channel_person_relation_logic(
        channel_id=channel_id,
        person_id=person_id,
    )

def get_expressions(
            person_id,
        ):
    """Get expressions

    :param person_id:
    :return:
    """
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
    """New expression creation

    :param expression_owner_id:
    :param expression_content:
    :param expression_content_url:
    :param expression_imagefile:
    :param expression_weight:
    :param broadcast_parent_id:
    :param total_upvotes:
    :param total_collects:
    :param total_broadcasts:
    :param total_discussions:
    :param channels:
    :return:
    """
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
    """New URL

    :param url:
    :param url_title:
    :param url_desc:
    :param url_imagefile:
    :param url_weight:
    :return:
    """
    log.debug('New URL INSERT')

    return core.store_url_logic(
        url=url,
        url_title=url_title,
        url_desc=url_desc,
        url_imagefile=url_imagefile,
        url_weight=url_weight,
    )


def find_url_id(url):
    """Find URL ID

    :param url:
    :return:
    """
    log.debug('Find URL')

    return core.find_url_id_logic(url=url)
