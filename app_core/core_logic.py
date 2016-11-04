# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############
"""
    This module contains functions that are for core logic.

    :Copyright: (c) 2016 by Nirlendu Saha
"""

import random

import core_database as core

from discover import logic as discover

from libs.logger import app_logger as log

def new_person_logic(
        user_name,
        person_name,
        total_followers,
        person_weight,
        person_channel_followee_list,
        person_person_followee_list,
        person_expression_list,
    ):
    """New Person registration logic

    :param user_name:
    :param person_name:
    :param total_followers:
    :param person_weight:
    :param person_channel_followee_list:
    :param person_person_followee_list:
    :param person_expression_list:
    :return:
    """
    log.debug('New Person Logic')

    return core.new_person_database(
        user_name=user_name,
        person_name=person_name,
        total_followers=total_followers,
        person_weight=person_weight,
        person_channel_followee_list=person_channel_followee_list,
        person_person_followee_list=person_person_followee_list,
        person_expression_list=person_expression_list,
    )


def new_channel_logic(
    channel_name,
    channel_unique_name,
    channel_weight,
    total_followers,
    channel_expression_list,
):
    """New Channel creation logic

    :param channel_name:
    :param channel_unique_name:
    :param channel_weight:
    :param total_followers:
    :param channel_expression_list:
    :return:
    """
    log.debug('New Channel Logic')

    return core.new_channel_database(
        channel_name=channel_name,
        channel_unique_name=channel_unique_name,
        channel_weight=channel_weight,
        total_followers=total_followers,
        channel_expression_list=channel_expression_list,
    )


def channel_person_relation_logic(
    channel_id,
    person_id,
):
    """New Channel Person Relation logic

    :param channel_id:
    :param person_id:
    :return:
    """
    log.debug('Channel Person Relation Logic')

    return core.channel_person_relation_database(
        channel_id=channel_id,
        person_id=person_id,
    )


def get_expressions_logic(
                person_id,
            ):
    """Get expressions logic

    :param person_id:
    :return:
    """
    log.debug('Get Expressions Logic')

    channel_expression_list = core.get_expressions_channel_database(
                                                person_id=person_id,
                                            )

    person_expression_list = core.get_expression_people_database(
                                                person_id=person_id,
                                            )

    discover_list = discover.get_discovery(
                            person_id = person_id,
                        )

    expression_list = create_expression_list(
        expression_list = channel_expression_list + person_expression_list + discover_list,
    )

    random.shuffle(expression_list)

    return send_json_as_response(
        expression_list=expression_list,
    )


def create_expression_list(
    expression_list,
):
    """Create new list of expressions

    :param expression_list:
    :return:
    """
    log.debug('creating expression list Logic')

    # HAVE TO RANK

    return list(set(expression_list))



def send_json_as_response(
    expression_list,
):
    """Expressions as JSON

    :param expression_list:
    :return:
    """
    log.debug('Sending JSON Response Logic')

    return core.get_expression_json(
            expression_list=expression_list,
        )


def new_expression_logic(
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
    # 1TODO
    # 1) Do some logic checks in the data
    # 2) Check if all the topics are present in DB
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
    log.debug('New Expression Logic')

    core.new_expression_database(
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
    return


def find_url_id_logic(url):
    """Find URL ID

    :param url:
    :return:
    """
    log.debug('Find URL logic')

    return core.find_url_id_database(url=url)


def store_url_logic(
        url,
        url_title,
        url_desc,
        url_imagefile,
        url_weight,
):
    """New URL insert logic

    :param url:
    :param url_title:
    :param url_desc:
    :param url_imagefile:
    :param url_weight:
    :return:
    """
    log.debug('New URL insert logic')

    return core.store_url_database(
        url=url,
        url_title=url_title,
        url_desc=url_desc,
        url_imagefile=url_imagefile,
        url_weight=url_weight,
    )
