# -*- coding: utf-8 -*-

import inspect
import sys

import core_database as core
from libs.logger import app_logger as log


def get_expressions_logic(
                person_id,
            ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Get Expressions Logic')

    # TODO
    # Get stuff from discover

    # expressions_ids = core.get_expressions_database(
    #     person_id=person_id,
    # )

    # Rank stuff here using all expression_ids and the weight of each

    # Assuming sorted expression_ids
    # expressions = core.get_expressions_database(
    #     expressions_ids=expressions_ids,
    # )

    #TODO ONLY FOR TESTING!
    #return core.get_index_data(person_id)
    return core.get_expressions_database(person_id)


def new_expression_logic(
        expression_owner_id,
        expression_content,
        expression_link_id,
        expression_imagefile,
        broadcast_parent_id,
        total_upvotes,
        total_downvotes,
        total_broadcasts,
        total_discussions,
        topics,
):
    # TODO
    # 1) Do some logic checks in the data
    # 2) Check if all the topics are present in DB
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New Expression Logic')

    core.new_expression_database(
        expression_owner_id=expression_owner_id,
        expression_content=expression_content,
        expression_link_id=expression_link_id,
        expression_imagefile=expression_imagefile,
        broadcast_parent_id=broadcast_parent_id,
        total_upvotes=total_upvotes,
        total_downvotes=total_downvotes,
        total_broadcasts=total_broadcasts,
        total_discussions=total_discussions,
        topics=topics,
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
        url_header,
        url_desc,
        url_imagefile,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New URL insert logic')

    return core.store_url_database(
        url=url,
        url_header=url_header,
        url_desc=url_desc,
        url_imagefile=url_imagefile
    )


def new_broadcast_logic(
        broadcast_owner_id,
        broadcast_content,
        expression_link_id,
        expression_imagefile,
        broadcast_parent_id,
        total_upvotes,
        total_downvotes,
        total_broadcasts,
        total_discussions,
        topics,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New broadcast logic')

    return core.new_broadcast_database(
        broadcast_owner_id=broadcast_owner_id,
        broadcast_content=broadcast_content,
        expression_link_id=expression_link_id,
        expression_imagefile=expression_imagefile,
        broadcast_parent_id=broadcast_parent_id,
        total_upvotes=total_upvotes,
        total_downvotes=total_downvotes,
        total_broadcasts=total_broadcasts,
        total_discussions=total_discussions,
        topics=topics,
    )


def new_discussion_expression_logic(
        discussion_parent_id,
        discussion_expression_owner_id,
        discussion_expression_content,
        discussion_expression_link_id,
        discussion_expression_imagefile,
        total_upvotes,
        total_downvotes,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New discussion expression Logic')

    return core.new_discussion_expression_database(
        discussion_parent_id=discussion_parent_id,
        discussion_expression_owner_id=discussion_expression_owner_id,
        discussion_expression_content=discussion_expression_content,
        discussion_expression_link_id=discussion_expression_link_id,
        discussion_expression_imagefile=discussion_expression_imagefile,
        total_upvotes=total_upvotes,
        total_downvotes=total_downvotes,
    )


def upvote_expression_logic(
        upvoter,
        expression_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Upvote expression Logic')

    return core.upvote_expression_database(
        upvoter=upvoter,
        expression_id=expression_id,
    )


def downvote_expression_logic(
        downvoter,
        expression_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Downvote expression Logic')

    return core.downvote_expression_database(
        downvoter=downvoter,
        expression_id=expression_id,
    )
