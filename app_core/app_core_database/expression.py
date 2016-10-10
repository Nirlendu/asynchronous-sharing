# -*- coding: utf-8 -*-

import inspect
import sys

from py2neo import Graph

from express.models import Expression
from libs.logger import app_logger as log


def new_expression_insert(
        expression_owner_id,
        expression_content,
        expression_link_id,
        expression_imagefile,
        broadcast_parent_id,
        total_upvotes,
        total_downvotes,
        total_broadcasts,
        total_discussions,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New Expression Insert Operation')

    expression_id = Expression.objects.store_expression(
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
    return expression_id


def new_expression_node(
        transaction,
        expression_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New Expression Node Creation')

    query = "CREATE (a:ExpressionGraph{expression_id:{expression_id}})"
    transaction.append(query, parameters={'expression_id': expression_id})
    return transaction


def new_expression_relationship(
        transaction,
        expression_node_id,
        expression_owner_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New Expression Node Owner Relation')

    query = "MATCH (e:ExpressionGraph{expression_id:{expression_node_id}}),(p:Person{person_id:{expression_owner_id}})"\
            " CREATE (p)-[:EXPRESSED]->(e)"

    transaction.append(query, parameters={'expression_node_id': expression_node_id,
                                          'expression_owner_id': expression_owner_id})
    return transaction


def new_discussion_update_count(
        expression_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New discussion expression update count')

    expressions = Expression.objects.filter(id=expression_id)
    for expression in expressions:
        expression.total_discussions += 1
        expression.save()
        return
    return


def new_broadcast_update_count(
        expression_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New discussion expression update count')

    expressions = Expression.objects.filter(id=expression_id)
    for expression in expressions:
        expression.total_broadcasts += 1
        expression.save()
        return
    return


# TODO
# change the name to Stream!
def new_expression_topics(
        transaction,
        topics,
        expression_node_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New Expression Node Stream Relation')

    for stream in topics:
        query = "MATCH (e:ExpressionGraph{expression_id:{expression_node_id}}), (t:Topic{name:{stream}}) " \
                "CREATE (e)-[:IN_TOPIC]->(t)"
        transaction.append(query, parameters={'expression_node_id': expression_node_id, 'stream': stream})

    return transaction


def upvote_prev_check(
        expression_id,
        upvoter,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Prev Upvote Check')

    graph = Graph()
    x = graph.cypher.stream(
        "MATCH (p:Person{person_id:{upvoter}}), (e:ExpressionGraph{expression_id:{expression_id}}), "
        "(p)-[r]->(e)"
        "return type(r)"
        , parameters={'upvoter': upvoter, 'expression_id': expression_id}
    )
    for i in x:
        if i[0] == 'UPVOTED' or i[0] == 'DOWNVOTED':
            return i[0]

    return None


def create_upvote_rel(
        transaction,
        expression_id,
        upvoter,
        condition=None,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Upvote create Relation')

    if not condition:
        query = "MATCH (p:Person{person_id:{upvoter}}), (e:ExpressionGraph{expression_id:{expression_id}}) " \
                "CREATE (p)-[:UPVOTED]->(e)"

    if condition == 'PREV_UPVOTE':
        query = "MATCH (p:Person{person_id:{upvoter}}), (e:ExpressionGraph{expression_id:{expression_id}}), " \
                "(p)-[r:UPVOTED]->(e) " \
                "DELETE r"

    if condition == 'PREV_DOWNVOTE':
        query = "MATCH (p:Person{person_id:{upvoter}}), (e:ExpressionGraph{expression_id:{expression_id}}), " \
                "(p)-[r:DOWNVOTED]->(e) " \
                "DELETE r " \
                "CREATE (p)-[:UPVOTED]->(e)"

    transaction.append(query, parameters={'upvoter': upvoter, 'expression_id': expression_id})
    return transaction


def update_upvote_count(
        expression_id,
        condition=None,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Upvote changing count')

    if not condition:
        expressions = Expression.objects.filter(id=expression_id)
        for expression in expressions:
            expression.total_upvotes += 1
            expression.save()
            return
        return

    if condition == 'PREV_UPVOTE':
        expressions = Expression.objects.filter(id=expression_id)
        for expression in expressions:
            expression.total_upvotes -= 1
            expression.save()
            return
        return

    if condition == 'PREV_DOWNVOTE':
        expressions = Expression.objects.filter(id=expression_id)
        for expression in expressions:
            expression.total_upvotes += 1
            expression.total_downvotes -= 1
            expression.save()
            return
        return


def downvote_prev_check(
        expression_id,
        downvoter,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Prev Downvote Check')

    graph = Graph()
    x = graph.cypher.stream(
        "MATCH (p:Person{person_id:{downvoter}}), (e:ExpressionGraph{expression_id:{expression_id}}), "
        "(p)-[r]->(e) "
        "return type(r)"
        , parameters={'downvoter': downvoter, 'expression_id': expression_id}
    )
    for i in x:
        if i[0] == 'UPVOTED' or i[0] == 'DOWNVOTED':
            return i[0]
    return None


def create_downvote_rel(
        transaction,
        expression_id,
        downvoter,
        condition=None,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Downvote create Relation')

    if not condition:
        query = "MATCH (p:Person{person_id:{downvoter}}), (e:ExpressionGraph{expression_id:{expression_id}}) " \
                "CREATE (p)-[:DOWNVOTED]->(e)"

    if condition == 'PREV_DOWNVOTE':
        query = "MATCH (p:Person{person_id:{downvoter}}), (e:ExpressionGraph{expression_id:{expression_id}}), " \
                "(p)-[r:DOWNVOTED]->(e) " \
                "DELETE r"

    if condition == 'PREV_UPVOTE':
        query = "MATCH (p:Person{person_id:{downvoter}), (e:ExpressionGraph{expression_id:{expression_id}), " \
                "(p)-[r:UPVOTED]->(e) " \
                "DELETE r " \
                "CREATE (p)-[:DOWNVOTED]->(e)"

    transaction.append(query, parameters={'downvoter': downvoter, 'expression_id': expression_id})
    return transaction


def update_downvote_count(
        expression_id,
        condition=None,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Downvote changing count')

    if not condition:
        expressions = Expression.objects.filter(id=expression_id)
        for expression in expressions:
            expression.total_downvotes += 1
            expression.save()
            return
        return

    if condition == 'PREV_DOWNVOTE':
        expressions = Expression.objects.filter(id=expression_id)
        for expression in expressions:
            expression.total_downvotes -= 1
            expression.save()
            return
        return

    if condition == 'PREV_UPVOTE':
        expressions = Expression.objects.filter(id=expression_id)
        for expression in expressions:
            expression.total_downvotes += 1
            expression.total_upvotes -= 1
            expression.save()
            return
        return
