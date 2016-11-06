# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############

import inspect
import sys, os

from libs.logger import app_logger as log

from models import ExpressionChannelRelation
from models import ChannelPrimary, ChannelPersonRelation


def new_channel(
    channel_name,
    channel_unique_name,
    channel_weight,
    total_followers,
):
    """New Channel Primary database

    :param channel_name:
    :param channel_unique_name:
    :param channel_weight:
    :param total_followers:
    :return:
    """
    log.debug('New Channel creating')

    channel_primary_id = ChannelPrimary.object.create_channel(
                            channel_name=channel_name,
                            channel_unique_name=channel_unique_name,
                            channel_weight=channel_weight,
                            total_followers=total_followers,
                        )
    return channel_primary_id



def channel_person_relation(
    channel_id,
    person_id,
):
    """New Channel Person Primary database

    :param channel_id:
    :param person_id:
    :return:
    """
    try:
        log.debug('Channel Expression Relation creating')
        channel_person_relation_id = ChannelPersonRelation.object.create_channel_person_relation(
            channel_id=channel_id,
            person_id=person_id,
        )

        channel = ChannelPrimary.object.get_channel(channel_id=channel_id)
        channel.total_followers += 1
        channel.save()

        return channel_person_relation_id
    except:
        log.debug('Channel Expression Relation deleting')
        channel_person_relation_id = ChannelPersonRelation.object.delete_channel_person_relation(
            channel_id=channel_id,
            person_id=person_id,
        )

        channel = ChannelPrimary.objects.get(channel_id=channel_id)
        channel.total_followers -= 1
        channel.save()

        return channel_person_relation_id



def channel_expression_relation(
    channels,
    expression_id,
):
    """New Channel Expresson Relation Database

    :param channels:
    :param expression_id:
    :return:
    """

    for channel_id in channels:
        log.debug('Channel Expression Relation creating')
        ExpressionChannelRelation.object.create_expression_channel_relation(
            channel_id=channel_id,
            expression_id=expression_id,
        )



