# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############


import inspect
import sys, os, re

from django.conf import settings
from django.db import transaction

from libs.logger import app_logger as log

from expression import database as express
from channel import database as channel
from app_interface import database as interface
from web import database as web
from people import database as people


@transaction.atomic
def get_expressions_channel_database(
                person_id,
            ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Get Expression Channel Core Database')

    return interface.get_channel_person_list(
                person_id=person_id,
    )


@transaction.atomic
def get_expression_people_database(
                person_id,
            ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Get Expression Channel Core Database')

    return interface.get_person_person_list(
                person_id=person_id
    )


@transaction.atomic
def new_person_database(
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

    log.debug('New Person Core Database')
    person_primary_id = people.new_person(
                            user_name=user_name,
                            person_name=person_name,
                            total_followers=total_followers,
                            person_weight=person_weight,
                        )

    person_secondary_id = interface.new_person(
        user_name=user_name,
        person_name=person_name,
        person_primary_id=str(person_primary_id),
        total_followers=total_followers,
        person_weight=person_weight,
        person_channel_followee_list=person_channel_followee_list,
        person_person_followee_list=person_person_followee_list,
        person_expression_list=person_expression_list,
    )
    return person_primary_id



@transaction.atomic
def new_channel_database(
    channel_name,
    channel_unique_name,
    channel_weight,
    total_followers,
    channel_expression_list,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

    log.debug('New Channel Core Database')
    channel_primary_id = channel.new_channel(
                            channel_name=channel_name,
                            channel_unique_name=channel_unique_name,
                            channel_weight=channel_weight,
                            total_followers=total_followers,
                        )

    channel_secondary_id = interface.new_channel(
        channel_primary_id=str(channel_primary_id),
        channel_name=channel_name,
        channel_unique_name=channel_unique_name,
        channel_weight=channel_weight,
        total_followers=total_followers,
        channel_expression_list=channel_expression_list,
    )
    return channel_primary_id



@transaction.atomic
def channel_person_relation_database(
    channel_id,
    person_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

    channel_person_primary_id = channel.channel_person_relation(
                            channel_id=channel_id,
                            person_id=person_id,
                        )

    channel_person_secondary_id = interface.channel_person_relation(
                            channel_id=str(channel_id),
                            person_id=str(person_id),
                        )

    return channel_person_primary_id



@transaction.atomic
def get_expression_json(
            expression_list,
        ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Get Expression JSON Core Database')

    expression_content_list = []

    for expression_id in expression_list:
        expression_content = {}
        expression_object = interface.get_expression_objects(
            expression_id=expression_id,
        )

        expression_content['EXPRESSION_ID'] = expression_object.expression_primary_id
        expression_content['EXPRESSION_OWNER'] = expression_object.expression_owner_id
        expression_content['EXPRESSION_CONTENT'] = expression_object.expression_content
        expression_content['EXPRESSION_IMAGE'] = expression_object.expression_imagefile
        expression_content['CHANNEL'] = expression_object.expression_channel
        expression_content['TIME'] = expression_object.expression_time
        expression_content['TOTAL_UPVOTES'] = expression_object.total_upvotes
        expression_content['TOTAL_BROADCASTS'] = expression_object.total_broadcasts
        expression_content['TOTAL_DISCUSSIONS'] =expression_object.total_discussions
        expression_content['TOTAL_COLLECTS'] = expression_object.total_collects

        if not (expression_object.expression_content_url is None):
            url_contents = interface.get_url_objects(
                url=expression_object.expression_content_url,
            )
            expression_content['URL'] = url_contents.url
            expression_content['URL_TITLE'] = url_contents.url_title
            expression_content['URL_IMAGEFILE'] = url_contents.url_imagefile
            expression_content['URL_DOMAIN'] = re.findall(
                '^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)',
                url_contents.url_title,
            )[0]

        if not (expression_object.broadcast_parent_id is None):
            broadcast_object = interface.get_expression_objects(
                expression_id=expression_object.broadcast_parent_id,
            )
            expression_content['BROADCAST_PARENT_OWNER'] = broadcast_object.expression_owner_id
            expression_content['BROADCAST_CONTENT'] = broadcast_object.expression_content
            expression_content['BROADCAST_IMAGE'] = broadcast_object.expression_imagefile
            expression_content['BROADCAST_CHANNEL'] = broadcast_object.expression_channel
            expression_content['BROADCAST_TIME'] = broadcast_object.expression_time

            if not (broadcast_object.expression_content_url is None):
                url_contents = interface.get_url_objects(
                    url=broadcast_object.expression_content_url,
                )
                expression_content['BROADCAST_URL'] = url_contents.url
                expression_content['BROADCAST_URL_TITLE'] = url_contents.url_title
                expression_content['BROADCAST_URL_IMAGEFILE'] = url_contents.url_imagefile
                expression_content['BROADCAST_URL_DOMAIN'] = re.findall(
                    '^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)',
                    url_contents.url_title,
                )[0]

        expression_content_list.append(expression_content)

    return expression_content_list



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

    channel_list = interface.get_channel_list(
                        expression_id=str(expression_primary_id),
                        channels=channels,
                    )

    channel.channel_expression_relation(
        channels=channel_list,
        expression_id=expression_primary_id,
    )

    expression_upvote_list = []
    expression_broadcast_list = []
    expression_discussion_list = []
    expression_collection_list = []

    expression_secondary_id = interface.new_expression(
        expression_primary_id=str(expression_primary_id),
        expression_owner_id=expression_owner_id,
        expression_content=expression_content,
        expression_content_url=expression_content_url,
        expression_imagefile=expression_imagefile,
        expression_weight=expression_weight,
        broadcast_parent_id=broadcast_parent_id,
        expression_channel=channels,
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