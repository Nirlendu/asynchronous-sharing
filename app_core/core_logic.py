# -*- coding: utf-8 -*-

import inspect
import sys

import core_database as core
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
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
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
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
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
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Channel Person Relation Logic')

    return core.channel_person_relation_database(
        channel_id=channel_id,
        person_id=person_id,
    )


def get_expressions_logic(
                person_id,
            ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Get Expressions Logic')

    # 1TODO
    # Get stuff from discover

    # expressions_ids = core.get_expressions_database(
    #     person_id=person_id,
    # )

    # Rank stuff here using all expression_ids and the weight of each

    # Assuming sorted expression_ids
    # expressions = core.get_expressions_database(
    #     expressions_ids=expressions_ids,
    # )

    # ONLY FOR TESTING!
    #return core.get_index_data(person_id)
    return core.get_expressions_database(person_id)


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
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
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
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Find URL logic')

    return core.find_url_id_database(url=url)


def store_url_logic(
        url,
        url_title,
        url_desc,
        url_imagefile,
        url_weight,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New URL insert logic')

    return core.store_url_database(
        url=url,
        url_title=url_title,
        url_desc=url_desc,
        url_imagefile=url_imagefile,
        url_weight=url_weight,
    )


# def new_broadcast_logic(
#         broadcast_owner_id,
#         broadcast_content,
#         expression_link_id,
#         expression_imagefile,
#         broadcast_parent_id,
#         total_upvotes,
#         total_downvotes,
#         total_broadcasts,
#         total_discussions,
#         topics,
# ):
#     log.info('IN - ' + sys._getframe().f_code.co_name)
#     log.info('FROM - ' + sys._getframe(1).f_code.co_name)
#     log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
#     log.debug('New broadcast logic')
#
#     return core.new_broadcast_database(
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
# def new_discussion_expression_logic(
#         discussion_parent_id,
#         discussion_expression_owner_id,
#         discussion_expression_content,
#         discussion_expression_link_id,
#         discussion_expression_imagefile,
#         total_upvotes,
#         total_downvotes,
# ):
#     log.info('IN - ' + sys._getframe().f_code.co_name)
#     log.info('FROM - ' + sys._getframe(1).f_code.co_name)
#     log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
#     log.debug('New discussion expression Logic')
#
#     return core.new_discussion_expression_database(
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
# def upvote_expression_logic(
#         upvoter,
#         expression_id,
# ):
#     log.info('IN - ' + sys._getframe().f_code.co_name)
#     log.info('FROM - ' + sys._getframe(1).f_code.co_name)
#     log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
#     log.debug('Upvote expression Logic')
#
#     return core.upvote_expression_database(
#         upvoter=upvoter,
#         expression_id=expression_id,
#     )
#
#
# def downvote_expression_logic(
#         downvoter,
#         expression_id,
# ):
#     log.info('IN - ' + sys._getframe().f_code.co_name)
#     log.info('FROM - ' + sys._getframe(1).f_code.co_name)
#     log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
#     log.debug('Downvote expression Logic')
#
#     return core.downvote_expression_database(
#         downvoter=downvoter,
#         expression_id=expression_id,
#     )
