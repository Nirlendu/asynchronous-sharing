# -*- coding: utf-8 -*-

import inspect
import sys, os

from libs.logger import app_logger as log

from models import ExpressionSecondary, UrlSecondary, PersonSecondary

def new_expression(
        expression_primary_id,
        expression_content,
        expression_content_url,
        expression_imagefile,
        expression_weight,
        broadcast_parent_id,
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

    try:
        log.debug('New expression secondary creating')
        expression_secondary = ExpressionSecondary.objects.create(
                                    expression_primary_id=expression_primary_id,
                                    expression_content=expression_content,
                                    expression_content_url=expression_content_url,
                                    expression_imagefile=expression_imagefile,
                                    expression_weight=expression_weight,
                                    broadcast_parent_id=broadcast_parent_id,
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
    except:
        log.info('New expression secondary creating FAILED')
        raise Exception

    return None


def store_url(
        url_parent_id,
        url_title,
        url_desc,
        url_imagefile,
        url_weight,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

    try:
        log.debug('New url secondary creating')
        url_secondary = UrlSecondary.objects.create(
                                        url_parent_id=url_parent_id,
                                        url_title=url_title,
                                        url_desc=url_desc,
                                        url_imagefile=url_imagefile,
                                        url_weight=url_weight,
                                        )
        return url_secondary.url_secondary_id
    except:
        log.info('New url secondary creating FAILED')
        raise Exception

    return None

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

    try:
        log.debug('New person secondary creating')
        url_secondary = PersonSecondary.objects.create(
                                        user_name=user_name,
                                        person_name=person_name,
                                        person_primary_id=person_primary_id,
                                        total_followers=total_followers,
                                        person_weight=person_weight,
                                        person_channel_followee_list=person_channel_followee_list,
                                        person_person_followee_list=person_person_followee_list,
                                        person_expression_list=person_expression_list,
                                        )
        return url_secondary.url_secondary_id
    except:
        log.info('New person secondary creating FAILED')
        raise Exception

    return None