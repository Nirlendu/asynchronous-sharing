# -*- coding: utf-8 -*-

import sys
from py2neo import Graph
from libs.logger import app_logger as log
from django.db import transaction
from express.models import Expression


def new_expression_insert(
		expression_owner_id, 
		expression_content, 
		expression_link_id, 
		expression_imagefile,
		broadcast_parent_id,
		total_upvotes,
		total_downvotes,
		total_broadcasts,
		):
	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.debug('New Expression Insert Operation')
	expression_id = Expression.objects.store_expression(
		expression_owner_id = expression_owner_id, 
		expression_content = expression_content, 
		expression_link_id = expression_link_id, 
		expression_imagefile = expression_imagefile,
		broadcast_parent_id = broadcast_parent_id,
		total_upvotes = total_upvotes,
		total_downvotes = total_downvotes,
		total_broadcasts = total_broadcasts,
	)
	return expression_id


def new_expression_node(
		transaction,
		expression_id,
	):
	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.debug('New Expression Node Creation')
	transaction.append("CREATE (a:ExpressionGraph{expression_id : " + expression_id + "})")
	return transaction


def new_expression_relationship(
			transaction,
			expression_node_id,
			expression_owner_id,
		):
	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.debug('New Expression Node Owner Relation')
	transaction.append("MATCH (e:ExpressionGraph{expression_id: " + expression_node_id + " }), (p:Person{person_id: '" + expression_owner_id + "' }) CREATE (p)-[:EXPRESSED]->(e)")
	return transaction

def new_expression_topics(
					transaction,
					topics,
					expression_node_id,
				):
	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.debug('New Expression Node Topic Relation')
	for each_topic in topics:
		transaction.append("MATCH (e:ExpressionGraph{expression_id: " + expression_node_id + " }), (t:Topic{name: '" + each_topic + "' }) CREATE (e)-[:IN_TOPIC]->(t)")
	return transaction


