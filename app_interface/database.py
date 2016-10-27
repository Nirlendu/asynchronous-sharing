# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############

import inspect
import sys, os, uuid

from libs.logger import app_logger as log

from models import ExpressionSecondary, UrlSecondary, PersonSecondary, ChannelSecondary

def new_expression(
        expression_primary_id,
        expression_owner_id,
        expression_content,
        expression_content_url,
        expression_imagefile,
        expression_weight,
        broadcast_parent_id,
        expression_channel,
        total_upvotes,
        total_broadcasts,
        total_discussions,
        total_collects,
        expression_upvote_list,
        expression_broadcast_list,
        expression_discussion_list,
        expression_collection_list,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

    log.debug('New expression secondary creating')
    expression_secondary = ExpressionSecondary.objects.create(
                                expression_secondary_id = str(uuid.uuid4()).replace('-','')[:16],
                                expression_primary_id=expression_primary_id,
                                expression_owner_id=expression_owner_id,
                                expression_content=expression_content,
                                expression_content_url=expression_content_url,
                                expression_imagefile=expression_imagefile,
                                expression_weight=expression_weight,
                                broadcast_parent_id=broadcast_parent_id,
                                expression_channel=expression_channel,
                                total_upvotes=total_upvotes,
                                total_broadcasts=total_broadcasts,
                                total_discussions=total_discussions,
                                total_collects=total_collects,
                                expression_upvote_list=expression_upvote_list,
                                expression_broadcast_list=expression_broadcast_list,
                                expression_discussion_list=expression_discussion_list,
                                expression_collection_list=expression_collection_list,
                            )
    return expression_secondary.expression_secondary_id


def new_channel(
    channel_primary_id,
    channel_name,
    channel_unique_name,
    channel_weight,
    total_followers,
    channel_expression_list,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

    log.debug('New channel secondary creating')
    channel_secondary = ChannelSecondary.objects.create(
                                        channel_secondary_id = str(uuid.uuid4()).replace('-','')[:8],
                                        channel_primary_id=channel_primary_id,
                                        channel_name=channel_name,
                                        channel_unique_name=channel_unique_name,
                                        channel_weight=channel_weight,
                                        total_followers=total_followers,
                                        channel_expression_list=channel_expression_list,
                                    )
    return channel_secondary.channel_secondary_id


def channel_person_relation(
            channel_id,
            person_id,
        ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

    log.debug('New channel person secondary creating')
    person_secondary = PersonSecondary.objects.get(person_primary_id=person_id)
    if channel_id in person_secondary.person_channel_followee_list:
        person_secondary.person_channel_followee_list.remove(channel_unique_name)
        person_secondary.total_followers -= 1
        person_secondary.save()
        channel_secondary = ChannelSecondary.objects.get(channel_primary_id=channel_id)
        channel_secondary.total_followers -= 1
        channel_secondary.save()
    else:
        person_secondary.person_channel_followee_list.append(channel_id)
        person_secondary.total_followers += 1
        person_secondary.save()
        channel_secondary = ChannelSecondary.objects.get(channel_primary_id=channel_id)
        channel_secondary.total_followers += 1
        channel_secondary.save()
    return True


def store_url(
        url,
        url_primary_id,
        url_title,
        url_desc,
        url_imagefile,
        url_weight,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

    log.debug('New url secondary creating')
    url_secondary = UrlSecondary.objects.create(
                                    url_secondary_id = str(uuid.uuid4()).replace('-','')[:16],
                                    url_primary_id=url_primary_id,
                                    url=url,
                                    url_title=url_title,
                                    url_desc=url_desc,
                                    url_imagefile=url_imagefile,
                                    url_weight=url_weight,
                                    )
    return url_secondary.url_secondary_id


def new_person(
        person_primary_id,
        user_name,
        person_name,
        total_followers,
        person_weight,
        person_channel_followee_list,
        person_person_followee_list,
        person_expression_list,
    ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

    log.debug('New person secondary creating')
    person_secondary = PersonSecondary.objects.create(
                                    person_secondary_id = str(uuid.uuid4()).replace('-','')[:12],
                                    user_name=user_name,
                                    person_name=person_name,
                                    person_primary_id=person_primary_id,
                                    total_followers=total_followers,
                                    person_weight=person_weight,
                                    person_channel_followee_list=person_channel_followee_list,
                                    person_person_followee_list=person_person_followee_list,
                                    person_expression_list=person_expression_list,
                                    )
    return person_secondary.person_secondary_id


def get_channel_list(
        channels,
        expression_id,
    ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

    log.debug('Getting channel id list')
    channel_id_list = []
    for channel in channels:
        channel_secondary = ChannelSecondary.objects.get(channel_unique_name=channel)
        channel_id_list.append(channel_secondary.channel_primary_id)
        channel_expression_relation(
            channel_secondary=channel_secondary,
            expression_id=expression_id,
        )
    return channel_id_list


def channel_expression_relation(
        channel_secondary,
        expression_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('channel expression interface relation')

    channel_secondary.channel_expression_list.append(expression_id)
    channel_secondary.save()


def get_channel_person_list(
        person_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('expression list in channels followed')

    person_secondary = PersonSecondary.objects.get(person_primary_id=person_id)
    channel_list = person_secondary.person_channel_followee_list

    channel_expression_list = []

    for channel in channel_list:
        channel_expression_list += ChannelSecondary.objects.get(channel_primary_id=channel).channel_expression_list

    return channel_expression_list


def get_person_person_list(
        person_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('expression list in people followed')

    person_list = PersonSecondary.objects.get(person_primary_id=person_id).person_person_followee_list

    person_expression_list = []

    for person in person_list:
        person_expression_list += PersonSecondary.objects.get(person_primary_id=person).person_expression_list

    return person_expression_list


def get_expression_objects(
        expression_id,
    ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('get expression objects')

    return ExpressionSecondary.objects.get(expression_primary_id=expression_id)


def get_url_objects(
        url_primary_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('get url objects')

    return UrlSecondary.objects.get(url_primary_id=url_primary_id)