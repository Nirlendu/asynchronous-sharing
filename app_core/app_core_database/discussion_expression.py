# -*- coding: utf-8 -*-

import inspect
import sys

from express.models import Discussion_Expression
from libs.logger import app_logger as log


def new_discussion_expression_insert(
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
    log.debug('New discussion expression Insert')

    discussion_expression_id = Discussion_Expression.objects.store_discussion_expression(
        discussion_parent_id=discussion_parent_id,
        discussion_expression_owner_id=discussion_expression_owner_id,
        discussion_expression_content=discussion_expression_content,
        discussion_expression_link_id=discussion_expression_link_id,
        discussion_expression_imagefile=discussion_expression_imagefile,
        total_upvotes=total_upvotes,
        total_downvotes=total_downvotes,
    )
    return discussion_expression_id


def new_discussion_expression_node(
        transaction,
        discussion_expression_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New discussion expression Node Create')

    transaction.append(
        "CREATE (a:DiscussionExpressionGraph{discussion_expression_id : " + discussion_expression_id + "})")
    return transaction


def new_discussion_expression_relation(
        transaction,
        discussion_expression_owner_id,
        discussion_expression_id,
        discussion_parent_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New discussion expression Node Relation Create')

    transaction.append(
        "MATCH (e:ExpressionGraph{expression_id: " + discussion_parent_id + " }), (p:Person{person_id: '" + discussion_expression_owner_id + "' }) , (d:DiscussionExpressionGraph{discussion_expression_id: " + discussion_expression_id + " })  CREATE (p)-[:DISCUSSED]->(d)-[:ON_EXPRESSION]->(e)")
    return transaction