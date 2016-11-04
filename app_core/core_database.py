# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############

"""
    This module contains functions that are for core database.

    :Copyright: (c) 2016 by Nirlendu Saha
"""

import os, re

from django.conf import settings
from django.db import transaction

from libs.logger import app_logger as log

from expression import database as express
from channel import database as channel
from app_interface import database as interface
from web import database as web
from people import database as people

from discover import database as discover


@transaction.atomic
def get_expressions_channel_database(
                person_id,
            ):
    """Get a list of expressions related to channel

    :param person_id:
    :return: list
    """
    log.debug('Get Expression Channel Core Database')

    return interface.get_channel_person_list(
                person_id=person_id,
    )


@transaction.atomic
def get_expression_people_database(
                person_id,
            ):
    """Get a list of expressions related to person

    :param person_id:
    :return: list
    """

    log.debug('Get Expression Channel Core Database')

    return interface.get_person_person_list(
                person_id=person_id
    )


@transaction.atomic
def new_person_database(
        user_name,
        person_name,
        total_followers,
        person_weight,
        person_channel_followee_list,
        person_person_followee_list,
        person_expression_list,
    ):
    """New person registration - core database

    :param user_name:
    :param person_name:
    :param total_followers:
    :param person_weight:
    :param person_channel_followee_list:
    :param person_person_followee_list:
    :param person_expression_list:
    :return: person_id
    """

    log.debug('New Person Core Database')

    person_primary_id = people.new_person(
                            user_name=user_name,
                            person_name=person_name,
                            total_followers=total_followers,
                            person_weight=person_weight,
                        )

    if not person_primary_id:
        return None

    person_secondary_id = interface.new_person(
        user_name=user_name,
        person_name=person_name,
        person_primary_id=str(person_primary_id),
        total_followers=total_followers,
        person_weight=person_weight,
        person_channel_followee_list=person_channel_followee_list,
        person_person_followee_list=person_person_followee_list,
        person_expression_list=person_expression_list,
    )

    if not person_secondary_id:
        return None

    return person_primary_id



@transaction.atomic
def new_channel_database(
    channel_name,
    channel_unique_name,
    channel_weight,
    total_followers,
    channel_expression_list,
):
    """New channel creation

    :param channel_name:
    :param channel_unique_name:
    :param channel_weight:
    :param total_followers:
    :param channel_expression_list:
    :return: channel_id
    """

    log.debug('New Channel Core Database')

    channel_primary_id = channel.new_channel(
                            channel_name=channel_name,
                            channel_unique_name=channel_unique_name,
                            channel_weight=channel_weight,
                            total_followers=total_followers,
                        )

    if not channel_primary_id:
        return None

    channel_secondary_id = interface.new_channel(
        channel_primary_id=str(channel_primary_id),
        channel_name=channel_name,
        channel_unique_name=channel_unique_name,
        channel_weight=channel_weight,
        total_followers=total_followers,
        channel_expression_list=channel_expression_list,
    )

    if not channel_secondary_id:
        return None

    return channel_primary_id



@transaction.atomic
def channel_person_relation_database(
    channel_id,
    person_id,
):
    """New channel person relationship

    :param channel_id:
    :param person_id:
    :return: channel_person_id
    """
    log.debug('New Channel Core Database')

    channel_person_primary_id = channel.channel_person_relation(
                            channel_id=channel_id,
                            person_id=person_id,
                        )

    if not channel_person_primary_id:
        return None

    channel_person_secondary_id = interface.channel_person_relation(
                            channel_id=str(channel_id),
                            person_id=str(person_id),
                        )

    if not channel_person_secondary_id:
        return None

    return channel_person_primary_id



@transaction.atomic
def get_expression_json(
            expression_list,
        ):
    """Get expression json from a list of expression ids

    :param expression_list:
    :return: expression_json
    """
    log.debug('Get Expression JSON Core Database')

    expression_content_list = []

    for expression_id in expression_list:
        expression_content = {}

        if expression_id.find('D') != -1:
            expression_content = discover.get_discovery_json(ids=expression_id)
            expression_content_list.append(expression_content)
            continue

        expression_object = interface.get_expression_objects(
            expression_id=expression_id,
        )

        expression_content['EXPRESSION_ID'] = expression_object.expression_primary_id
        expression_content['EXPRESSION_OWNER'] = interface.get_expression_owner_name(
                                                    person_id=expression_object.expression_owner_id,
                                                )
        expression_content['EXPRESSION_CONTENT'] = expression_object.expression_content
        expression_content['EXPRESSION_IMAGE'] = expression_object.expression_imagefile
        expression_content['CHANNEL'] = interface.get_expression_channel_name(
                                                    channel_list=expression_object.expression_channel,
                                                )
        expression_content['TIME'] = expression_object.expression_time
        expression_content['TOTAL_UPVOTES'] = expression_object.total_upvotes
        expression_content['TOTAL_BROADCASTS'] = expression_object.total_broadcasts
        expression_content['TOTAL_DISCUSSIONS'] =expression_object.total_discussions
        expression_content['TOTAL_COLLECTS'] = expression_object.total_collects

        if expression_object.expression_content_url != 'None':
            url_contents = interface.get_url_objects(
                url_primary_id=str(expression_object.expression_content_url),
            )
            expression_content['URL'] = url_contents.url
            expression_content['URL_TITLE'] = url_contents.url_title
            expression_content['URL_IMAGEFILE'] = url_contents.url_imagefile
            expression_content['URL_DOMAIN'] = re.findall(
                '^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)',
                url_contents.url,
            )[0]

        if expression_object.broadcast_parent_id is not None:
            broadcast_object = interface.get_expression_objects(
                expression_id=expression_object.broadcast_parent_id,
            )
            expression_content['BROADCAST_PARENT_OWNER'] = broadcast_object.expression_owner_id
            expression_content['BROADCAST_CONTENT'] = broadcast_object.expression_content
            expression_content['BROADCAST_IMAGE'] = broadcast_object.expression_imagefile
            expression_content['BROADCAST_CHANNEL'] = broadcast_object.expression_channel
            expression_content['BROADCAST_TIME'] = broadcast_object.expression_time

            if not (broadcast_object.expression_content_url is None):
                url_contents = interface.get_url_objects(
                    url_primary_id=broadcast_object.expression_content_url,
                )
                expression_content['BROADCAST_URL'] = url_contents.url
                expression_content['BROADCAST_URL_TITLE'] = url_contents.url_title
                expression_content['BROADCAST_URL_IMAGEFILE'] = url_contents.url_imagefile
                expression_content['BROADCAST_URL_DOMAIN'] = re.findall(
                    '^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)',
                    url_contents.url_title,
                )[0]

        expression_content_list.append(expression_content)

    return expression_content_list



@transaction.atomic
def new_expression_database(
        expression_owner_id,
        expression_content,
        expression_content_url,
        expression_imagefile,
        expression_weight,
        broadcast_parent_id,
        total_upvotes,
        total_collects,
        total_broadcasts,
        total_discussions,
        channels,
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
    :return: expression id
    """
    log.debug('New Expression Core Database')

    expression_primary_id = express.new_expresssion(
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

    if not expression_primary_id:
        return None

    channel_list = interface.get_channel_list(
                        expression_id=str(expression_primary_id),
                        channels=channels,
                    )

    channel.channel_expression_relation(
        channels=channel_list,
        expression_id=expression_primary_id,
    )

    expression_upvote_list = []
    expression_broadcast_list = []
    expression_discussion_list = []
    expression_collection_list = []

    expression_secondary_id = interface.new_expression(
        expression_primary_id=str(expression_primary_id),
        expression_owner_id=expression_owner_id,
        expression_content=expression_content,
        expression_content_url=str(expression_content_url),
        expression_imagefile=expression_imagefile,
        expression_weight=expression_weight,
        broadcast_parent_id=broadcast_parent_id,
        expression_channel=channels,
        total_upvotes=total_upvotes,
        total_broadcasts=total_broadcasts,
        total_discussions=total_discussions,
        total_collects=total_collects,
        expression_upvote_list=expression_upvote_list,
        expression_broadcast_list=expression_broadcast_list,
        expression_discussion_list=expression_discussion_list,
        expression_collection_list=expression_collection_list,
    )

    if not expression_secondary_id:
        return None

    return expression_primary_id



def find_url_id_database(url):
    """Find URL ID

    :param url:
    :return: url_id
    """
    log.debug('Find URL database')

    return web.find_url_id(url=url)



@transaction.atomic
def store_url_database(
        url,
        url_title,
        url_desc,
        url_imagefile,
        url_weight,
):
    """New URL

    :param url:
    :param url_title:
    :param url_desc:
    :param url_imagefile:
    :param url_weight:
    :return: url_id
    """
    log.debug('New URL insert database')

    url_primary_id = web.store_url(
                    url=url,
                    url_title=url_title,
                    url_desc=url_desc,
                    url_imagefile=url_imagefile,
                    url_weight=url_weight,
                )

    if not url_primary_id:
        return None

    url_secondary_id = interface.store_url(
                    url_primary_id=str(url_primary_id),
                    url=url,
                    url_title=url_title,
                    url_desc=url_desc,
                    url_imagefile=url_imagefile,
                    url_weight=url_weight,
                )

    if not url_secondary_id:
        return None

    return url_primary_id