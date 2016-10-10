# -*- coding: utf-8 -*-

import inspect
import sys, os

from django.db import transaction
from py2neo import Graph, ServiceRoot

from app_core_database import expression, expressed_url, broadcast, discussion_expression
from libs.logger import app_logger as log


@transaction.atomic
def new_expression_database(
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
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New Expression Core Database')

    expression_id = expression.new_expression_insert(
        expression_owner_id=expression_owner_id,
        expression_content=expression_content,
        expression_link_id=expression_link_id,
        expression_imagefile=expression_imagefile,
        broadcast_parent_id=broadcast_parent_id,
        total_upvotes=total_upvotes,
        total_downvotes=total_downvotes,
        total_broadcasts=total_broadcasts,
        total_discussions=total_discussions,
    )
    graphdb_url = os.environ.get('GRAPHDB_URL')
    graph = ServiceRoot(graphdb_url).graph
    intial_transaction = graph.cypher.begin()
    expression_node_transaction = expression.new_expression_node(
        transaction=intial_transaction,
        expression_id=str(expression_id),
    )
    expression_relationship_transaction = expression.new_expression_relationship(
        transaction=expression_node_transaction,
        expression_node_id=str(expression_id),
        expression_owner_id=expression_owner_id
    )
    final_transaction = expression.new_expression_topics(
        transaction=expression_relationship_transaction,
        topics=topics,
        expression_node_id=str(expression_id),
    )
    try:
        final_transaction.process()
    except:
        final_transaction.rollback()
        log.info('New expression creating FAILED')
        raise Exception

    log.info('New expression creating SUCCESS')
    final_transaction.commit()
    return


def find_url_id_database(url):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Find URL database')

    return expressed_url.find_url_id(url=url)


@transaction.atomic
def store_url_database(
        url,
        url_header,
        url_desc,
        url_imagefile,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New URL insert database')

    return expressed_url.store_url(
        url=url,
        url_header=url_header,
        url_desc=url_desc,
        url_imagefile=url_imagefile,
    )


@transaction.atomic
def new_broadcast_database(
        broadcast_owner_id,
        broadcast_content,
        expression_link_id,
        expression_imagefile,
        broadcast_parent_id,
        total_upvotes,
        total_downvotes,
        total_broadcasts,
        topics,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New Broadcast database')

    expression_id = expression.new_expression_insert(
        expression_owner_id=broadcast_owner_id,
        expression_content=broadcast_content,
        expression_link_id=expression_link_id,
        expression_imagefile=expression_imagefile,
        broadcast_parent_id=broadcast_parent_id,
        total_upvotes=total_upvotes,
        total_downvotes=total_downvotes,
        total_broadcasts=total_broadcasts,
    )
    expression.new_broadcast_update_count(
        expression_id=discussion_parent_id,
    )
    graphdb_url = os.environ.get('GRAPHDB_URL')
    graph = ServiceRoot(graphdb_url).graph
    intial_transaction = graph.cypher.begin()
    expression_node_transaction = expression.new_expression_node(
        transaction=intial_transaction,
        expression_id=str(expression_id),
    )
    expression_relationship_transaction = expression.new_expression_relationship(
        transaction=expression_node_transaction,
        expression_node_id=str(expression_id),
        expression_owner_id=broadcast_owner_id
    )
    new_broadcast_transaction = expression.new_expression_topics(
        transaction=expression_relationship_transaction,
        topics=topics,
        expression_node_id=str(expression_id),
    )
    # TODO
    # MAKE THE FOLLOWING 3 QUERIES IN 1 TRANSACTION
    is_parent_broadcast = broadcast.check_parent_broadcast(
        broadcast_parent_id=broadcast_parent_id,
    )

    if (not is_parent_broadcast):
        final_transaction = broadcast.new_broadcast_relation(
            transaction=new_broadcast_transaction,
            expression_id=str(expression_id),
            broadcast_parent_id=broadcast_parent_id,
        )
    else:
        final_transaction = broadcast.new_broadcast_relation(
            transaction=new_broadcast_transaction,
            expression_id=str(expression_id),
            broadcast_parent_id=str(is_parent_broadcast),
        )
    try:
        final_transaction.process()
    except:
        final_transaction.rollback()
        log.info('New Broadcast creating FAILED')
        raise Exception

    log.info('New Broadcast creating SUCESSFUL')
    final_transaction.commit()
    return


@transaction.atomic
def new_discussion_expression_database(
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
    log.debug('New discussion expression database')

    discussion_expression_id = discussion_expression.new_discussion_expression_insert(
        discussion_parent_id=discussion_parent_id,
        discussion_expression_owner_id=discussion_expression_owner_id,
        discussion_expression_content=discussion_expression_content,
        discussion_expression_link_id=discussion_expression_link_id,
        discussion_expression_imagefile=discussion_expression_imagefile,
        total_upvotes=total_upvotes,
        total_downvotes=total_downvotes,
    )

    expression.new_discussion_update_count(
        expression_id=discussion_parent_id,
    )
    graphdb_url = os.environ.get('GRAPHDB_URL')
    graph = ServiceRoot(graphdb_url).graph
    intial_transaction = graph.cypher.begin()

    expression_node_transaction = discussion_expression.new_discussion_expression_node(
        transaction=intial_transaction,
        discussion_expression_id=str(discussion_expression_id),
    )

    final_transaction = discussion_expression.new_discussion_expression_relation(
        transaction=expression_node_transaction,
        discussion_expression_owner_id=discussion_expression_owner_id,
        discussion_expression_id=str(discussion_expression_id),
        discussion_parent_id=discussion_parent_id,
    )
    try:
        final_transaction.process()
    except:
        final_transaction.rollback()
        log.info('New discussion expression creating FAILED')
        raise Exception

    log.info('New discussion expression creating SUCESSFUL')
    final_transaction.commit()
    return


@transaction.atomic
def upvote_expression_database(
        upvoter,
        expression_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Upvote expression database')

    prev_relation = expression.upvote_prev_check(
        expression_id=expression_id,
        upvoter=upvoter,
    )

    graphdb_url = os.environ.get('GRAPHDB_URL')
    graph = ServiceRoot(graphdb_url).graph
    intial_transaction = graph.cypher.begin()

    if (prev_relation == 'UPVOTED'):
        final_transaction = expression.create_upvote_rel(
            transaction=intial_transaction,
            expression_id=expression_id,
            upvoter=upvoter,
            condition='PREV_UPVOTE',
        )
        expression.update_upvote_count(
            expression_id=expression_id,
            condition='PREV_UPVOTE',
        )

    if (prev_relation == 'DOWNVOTED'):
        final_transaction = expression.create_upvote_rel(
            transaction=intial_transaction,
            expression_id=expression_id,
            upvoter=upvoter,
            condition='PREV_DOWNVOTE',
        )
        expression.update_upvote_count(
            expression_id=expression_id,
            condition='PREV_DOWNVOTE',
        )

    else:
        if (not prev_relation):
            final_transaction = expression.create_upvote_rel(
                transaction=intial_transaction,
                expression_id=expression_id,
                upvoter=upvoter,
            )
            expression.update_upvote_count(
                expression_id=expression_id,
            )
        else:
            final_transaction = intial_transaction

    try:
        final_transaction.process()
    except:
        final_transaction.rollback()
        log.info('Upvote expression FAILED')
        raise Exception

    log.info('Upvote expression SUCESSFUL')
    final_transaction.commit()
    return


@transaction.atomic
def downvote_expression_database(
        downvoter,
        expression_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Downvote expression database')

    prev_relation = expression.downvote_prev_check(
        expression_id=expression_id,
        downvoter=downvoter,
    )

    graphdb_url = os.environ.get('GRAPHDB_URL')
    graph = ServiceRoot(graphdb_url).graph
    intial_transaction = graph.cypher.begin()

    if (prev_relation == 'UPVOTED'):
        final_transaction = expression.create_downvote_rel(
            transaction=intial_transaction,
            expression_id=expression_id,
            downvoter=downvoter,
            condition='PREV_UPVOTE',
        )
        expression.update_downvote_count(
            expression_id=expression_id,
            condition='PREV_UPVOTE',
        )

    if (prev_relation == 'DOWNVOTED'):
        final_transaction = expression.create_downvote_rel(
            transaction=intial_transaction,
            expression_id=expression_id,
            downvoter=downvoter,
            condition='PREV_DOWNVOTE',
        )
        expression.update_downvote_count(
            expression_id=expression_id,
            condition='PREV_DOWNVOTE',
        )

    else:
        if (not prev_relation):
            final_transaction = expression.create_downvote_rel(
                transaction=intial_transaction,
                expression_id=expression_id,
                downvoter=downvoter,
            )
            expression.update_downvote_count(
                expression_id=expression_id,
            )
        else:
            final_transaction = intial_transaction

    try:
        final_transaction.process()
    except:
        final_transaction.rollback()
        log.info('Downvote expression FAILED')
        raise Exception

    log.info('Downvote expression SUCESSFUL')
    final_transaction.commit()
    return
