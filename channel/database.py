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
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

    try:
        log.debug('New Channel creating')
        channel_primary_id = ChannelPrimary.object.create_channel(
                                channel_name=channel_name,
                                channel_unique_name=channel_unique_name,
                                channel_weight=channel_weight,
                                total_followers=total_followers,
                            )
        return channel_primary_id

    except:
        log.debug('New Channel creating FAILED')
        raise Exception

    return None



def channel_person_relation(
    channel_id,
    person_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

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
        try:
            log.debug('Channel Expression Relation deleting')
            channel_person_relation_id = ChannelPersonRelation.object.delete_channel_person_relation(
                channel_id=channel_id,
                person_id=person_id,
            )

            channel = ChannelPrimary.objects.get(channel_id=channel_id)
            channel.total_followers -= 1
            channel.save()

            return channel_person_relation_id
        except Exception:
            log.debug('Channel Expression Relation creating FAILED')

    return None



def channel_expression_relation(
    channels,
    expression_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

    for channel_id in channels:
        # try:
        log.debug('Channel Expression Relation creating')
        ExpressionChannelRelation.object.create_expression_channel_relation(
            channel_id=channel_id,
            expression_id=expression_id,
        )
        # except:
        #     log.debug('Channel Expression Relation FAILED')
        #     raise Exception
    return None


