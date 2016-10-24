# -*- coding: utf-8 -*-

import inspect
import sys, os, re

from django.conf import settings

from django.db import transaction
from py2neo import Graph, ServiceRoot

from libs.logger import app_logger as log

from expression import database as express
from channel import database as channel
from app_interface import database as interface
from web import database as web

# TODO Remove this!
#from express.models import Expression, Link

@transaction.atomic
def get_expressions_database(
                person_id,
            ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Get Expression Core Database')

    # TODO
    # people = get_the_people_followed(
    #           person_id = person_id,
    # )

    # TODO
    # channels = get_the_channels_followed(
    #               person_id = person_id,
    # )

    # For the time being
    # people = [person_id]
    # streams = ['naarada']
    #
    # expressions = get_expressions.get_expressions(
    #     people=people,
    #     streams=streams,
    # )
    #
    # if expressions:
    #     for expression in expressions:
    #         pass

    #return get_index_data(person_id)
    return []

# TODO Only for testing!
# def get_index_data(person_id):
#     entry = []
#     graph = ServiceRoot(settings.GRAPHDB_URL).graph
#     express = graph.cypher.stream(
#         "MATCH (n:ExpressionGraph) -[:IN_TOPIC]->(Topic{name:'naarada'}), (a:Person{person_id: '" + person_id + "'})-[:EXPRESSED]->(n) RETURN n");
#     for record in express:
#
#         # A VERY BAD QUERY
#         try:
#             expressions = Expression.objects.filter(id=record[0]['expression_id'])
#         except:
#             log.exception('Inconsistent Data. No entry in SQL for Node')
#             raise Exception
#             return None
#
#         for expression in expressions:
#             a = {'expression_id': expression.id, 'expression_owner': expression.expression_owner_id,
#                  'expression_content': expression.expression_content,
#                  'expression_image': expression.expression_imagefile}
#             if expression.expression_link_id is not None:
#                 entries = Link.objects.filter(id=expression.expression_link_id)
#                 for x in entries:
#                     a['expression_link'] = x.link_url
#                     a['expression_link_title'] = x.link_name
#                     a['expression_link_image'] = x.link_image
#                     a['parent_domain'] = re.findall('^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)', x.link_url)[
#                         0]
#
#             q = graph.cypher.stream("MATCH (p:ExpressionGraph{expression_id: '" + str(
#                 expression.id) + "' }), (e:ExpressionGraph), (p)-[:BROADCAST_OF]->(e) return e")
#             if q:
#                 for x in q:
#                     broadcasts = Expression.objects.filter(id=x[0]['expression_id'])
#                     for broadcast in broadcasts:
#                         b = {'expression_id': broadcast.id, 'expression_owner': broadcast.expression_owner_id,
#                              'expression_content': broadcast.expression_content,
#                              'expression_image': broadcast.expression_imagefile}
#                         if broadcast.expression_link_id is not None:
#                             print 'IT DOES HAVE LINKS!'
#                             entries = Link.objects.filter(id=broadcast.expression_link_id)
#                             for x in entries:
#                                 b['expression_link'] = x.link_url
#                                 b['expression_link_title'] = x.link_name
#                                 b['expression_link_image'] = x.link_image
#                                 b['parent_domain'] = \
#                                     re.findall('^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)', x.link_url)[0]
#                     a['broadcast_of'] = b
#             entry.append(a)
#     return entry



@transaction.atomic
def new_expression_database(
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
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

    try:
        log.debug('New Expression Core Database')
        expression_primary_id = express.new_expresssion(
            expression_owner_id=expression_owner_id,
            expression_content=expression_content,
            expression_content_url=expression_content_url,
            expression_imagefile=expression_imagefile,
            broadcast_parent_id=broadcast_parent_id,
            expression_weight=expression_weight,
            total_upvotes=total_upvotes,
            total_collects=total_collects,
            total_broadcasts=total_broadcasts,
            total_discussions=total_discussions,
        )

        channel.channel_expression_relationship(
            channels=channels,
            expression_id=expression_primary_id,
        )

        expression_upvote_list = []
        expression_broadcast_list = []
        expression_discussion_list = []
        expression_collection_list = []

        expression_secondary_id = interface.new_expression(
            expression_primary_id=str(expression_primary_id),
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
        return expression_secondary_id

    except:
        log.debug('New Expression creation FAILED')
        raise Exception

    return None

#
# @transaction.atomic
# def new_expression_database(
#         expression_owner_id,
#         expression_content,
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
#     log.debug('New Expression Core Database')
#
#     expression_id = expression.new_expression_insert(
#         expression_owner_id=expression_owner_id,
#         expression_content=expression_content,
#         expression_link_id=expression_link_id,
#         expression_imagefile=expression_imagefile,
#         broadcast_parent_id=broadcast_parent_id,
#         total_upvotes=total_upvotes,
#         total_downvotes=total_downvotes,
#         total_broadcasts=total_broadcasts,
#         total_discussions=total_discussions,
#     )
#     graph = ServiceRoot(settings.GRAPHDB_URL).graph
#     intial_transaction = graph.cypher.begin()
#     expression_node_transaction = expression.new_expression_node(
#         transaction=intial_transaction,
#         expression_id=str(expression_id),
#     )
#     expression_relationship_transaction = expression.new_expression_relationship(
#         transaction=expression_node_transaction,
#         expression_node_id=str(expression_id),
#         expression_owner_id=expression_owner_id
#     )
#     final_transaction = expression.new_expression_topics(
#         transaction=expression_relationship_transaction,
#         topics=topics,
#         expression_node_id=str(expression_id),
#     )
#     try:
#         final_transaction.process()
#     except:
#         final_transaction.rollback()
#         log.info('New expression creating FAILED')
#         raise Exception
#
#     log.info('New expression creating SUCCESS')
#     final_transaction.commit()
#     return


def find_url_id_database(url):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Find URL database')

    return web.find_url_id(url=url)


@transaction.atomic
def store_url_database(
        url,
        url_title,
        url_desc,
        url_imagefile,
        url_weight,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New URL insert database')

    url_parent_id = web.store_url(
                    url=url,
                    url_title=url_title,
                    url_desc=url_desc,
                    url_imagefile=url_imagefile,
                    url_weight=url_weight,
                )

    url_secondary_id = interface.store_url(
                    url_parent_id=url_parent_id,
                    url_title=url_title,
                    url_desc=url_desc,
                    url_imagefile=url_imagefile,
                    url_weight=url_weight,
                )

    return url_secondary_id

#
# @transaction.atomic
# def new_broadcast_database(
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
#     log.debug('New Broadcast database')
#
#     expression_id = expression.new_expression_insert(
#         expression_owner_id=broadcast_owner_id,
#         expression_content=broadcast_content,
#         expression_link_id=expression_link_id,
#         expression_imagefile=expression_imagefile,
#         broadcast_parent_id=broadcast_parent_id,
#         total_upvotes=total_upvotes,
#         total_downvotes=total_downvotes,
#         total_broadcasts=total_broadcasts,
#         total_discussions=total_discussions,
#     )
#     expression.new_broadcast_update_count(
#         expression_id=broadcast_parent_id,
#     )
#     graph = ServiceRoot(settings.GRAPHDB_URL).graph
#     intial_transaction = graph.cypher.begin()
#     expression_node_transaction = expression.new_expression_node(
#         transaction=intial_transaction,
#         expression_id=str(expression_id),
#     )
#     expression_relationship_transaction = expression.new_expression_relationship(
#         transaction=expression_node_transaction,
#         expression_node_id=str(expression_id),
#         expression_owner_id=broadcast_owner_id
#     )
#     new_broadcast_transaction = expression.new_expression_topics(
#         transaction=expression_relationship_transaction,
#         expression_node_id=str(expression_id),
#         topics=topics,
#     )
#     # TODO
#     # MAKE THE FOLLOWING 3 QUERIES IN 1 TRANSACTION
#     is_parent_broadcast = broadcast.check_parent_broadcast(
#         broadcast_parent_id=broadcast_parent_id,
#     )
#
#     if not is_parent_broadcast:
#         final_transaction = broadcast.new_broadcast_relation(
#             transaction=new_broadcast_transaction,
#             expression_id=str(expression_id),
#             broadcast_parent_id=broadcast_parent_id,
#         )
#     else:
#         final_transaction = broadcast.new_broadcast_relation(
#             transaction=new_broadcast_transaction,
#             expression_id=str(expression_id),
#             broadcast_parent_id=str(is_parent_broadcast),
#         )
#     try:
#         final_transaction.process()
#     except:
#         final_transaction.rollback()
#         log.info('New Broadcast creating FAILED')
#         raise Exception
#
#     log.info('New Broadcast creating SUCESSFUL')
#     final_transaction.commit()
#     return
#
#
# @transaction.atomic
# def new_discussion_expression_database(
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
#     log.debug('New discussion expression database')
#
#     discussion_expression_id = discussion_expression.new_discussion_expression_insert(
#         discussion_parent_id=discussion_parent_id,
#         discussion_expression_owner_id=discussion_expression_owner_id,
#         discussion_expression_content=discussion_expression_content,
#         discussion_expression_link_id=discussion_expression_link_id,
#         discussion_expression_imagefile=discussion_expression_imagefile,
#         total_upvotes=total_upvotes,
#         total_downvotes=total_downvotes,
#     )
#
#     expression.new_discussion_update_count(
#         expression_id=discussion_parent_id,
#     )
#     graph = ServiceRoot(settings.GRAPHDB_URL).graph
#     intial_transaction = graph.cypher.begin()
#
#     expression_node_transaction = discussion_expression.new_discussion_expression_node(
#         transaction=intial_transaction,
#         discussion_expression_id=str(discussion_expression_id),
#     )
#
#     final_transaction = discussion_expression.new_discussion_expression_relation(
#         transaction=expression_node_transaction,
#         discussion_expression_owner_id=discussion_expression_owner_id,
#         discussion_expression_id=str(discussion_expression_id),
#         discussion_parent_id=discussion_parent_id,
#     )
#     try:
#         final_transaction.process()
#     except:
#         final_transaction.rollback()
#         log.info('New discussion expression creating FAILED')
#         raise Exception
#
#     log.info('New discussion expression creating SUCESSFUL')
#     final_transaction.commit()
#     return
#
#
# @transaction.atomic
# def upvote_expression_database(
#         upvoter,
#         expression_id,
# ):
#     log.info('IN - ' + sys._getframe().f_code.co_name)
#     log.info('FROM - ' + sys._getframe(1).f_code.co_name)
#     log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
#     log.debug('Upvote expression database')
#
#     prev_relation = expression.upvote_prev_check(
#         expression_id=expression_id,
#         upvoter=upvoter,
#     )
#
#     graph = ServiceRoot(settings.GRAPHDB_URL).graph
#     intial_transaction = graph.cypher.begin()
#
#     if prev_relation == 'UPVOTED':
#         final_transaction = expression.create_upvote_rel(
#             transaction=intial_transaction,
#             expression_id=expression_id,
#             upvoter=upvoter,
#             condition='PREV_UPVOTE',
#         )
#         expression.update_upvote_count(
#             expression_id=expression_id,
#             condition='PREV_UPVOTE',
#         )
#
#     if prev_relation == 'DOWNVOTED':
#         final_transaction = expression.create_upvote_rel(
#             transaction=intial_transaction,
#             expression_id=expression_id,
#             upvoter=upvoter,
#             condition='PREV_DOWNVOTE',
#         )
#         expression.update_upvote_count(
#             expression_id=expression_id,
#             condition='PREV_DOWNVOTE',
#         )
#
#     else:
#         if not prev_relation:
#             final_transaction = expression.create_upvote_rel(
#                 transaction=intial_transaction,
#                 expression_id=expression_id,
#                 upvoter=upvoter,
#             )
#             expression.update_upvote_count(
#                 expression_id=expression_id,
#             )
#         else:
#             final_transaction = intial_transaction
#
#     try:
#         final_transaction.process()
#     except:
#         final_transaction.rollback()
#         log.info('Upvote expression FAILED')
#         raise Exception
#
#     log.info('Upvote expression SUCESSFUL')
#     final_transaction.commit()
#     return
#
#
# @transaction.atomic
# def downvote_expression_database(
#         downvoter,
#         expression_id,
# ):
#     log.info('IN - ' + sys._getframe().f_code.co_name)
#     log.info('FROM - ' + sys._getframe(1).f_code.co_name)
#     log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
#     log.debug('Downvote expression database')
#
#     prev_relation = expression.downvote_prev_check(
#         expression_id=expression_id,
#         downvoter=downvoter,
#     )
#
#     graph = ServiceRoot(settings.GRAPHDB_URL).graph
#     intial_transaction = graph.cypher.begin()
#
#     if prev_relation == 'UPVOTED':
#         final_transaction = expression.create_downvote_rel(
#             transaction=intial_transaction,
#             expression_id=expression_id,
#             downvoter=downvoter,
#             condition='PREV_UPVOTE',
#         )
#         expression.update_downvote_count(
#             expression_id=expression_id,
#             condition='PREV_UPVOTE',
#         )
#
#     if prev_relation == 'DOWNVOTED':
#         final_transaction = expression.create_downvote_rel(
#             transaction=intial_transaction,
#             expression_id=expression_id,
#             downvoter=downvoter,
#             condition='PREV_DOWNVOTE',
#         )
#         expression.update_downvote_count(
#             expression_id=expression_id,
#             condition='PREV_DOWNVOTE',
#         )
#
#     else:
#         if not prev_relation:
#             final_transaction = expression.create_downvote_rel(
#                 transaction=intial_transaction,
#                 expression_id=expression_id,
#                 downvoter=downvoter,
#             )
#             expression.update_downvote_count(
#                 expression_id=expression_id,
#             )
#         else:
#             final_transaction = intial_transaction
#
#     try:
#         final_transaction.process()
#     except:
#         final_transaction.rollback()
#         log.info('Downvote expression FAILED')
#         raise Exception
#
#     log.info('Downvote expression SUCESSFUL')
#     final_transaction.commit()
#     return