# -*- coding: utf-8 -*-

import sys
from py2neo import Graph
from libs.logger import app_logger as log
from app_base.models import Topic, Person
from express.models import Link, Expression, ExpressionGraph


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
		expression_id
	):
	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	try:
		log.debug('New Expression Node Creation')
		return ExpressionGraph(
			expression_id = expression_id,
		).save()
	except Exception:
		log.debug('Could not create new expression node')
	return


def new_expression_relationship(
			expression_node_id,
			expression_owner_id,
		):
	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	try:
		log.debug('New Expression Node Owner Relation Creation')
		graph = Graph()
		graph.cypher.execute("MATCH (e:ExpressionGraph{expression_id: " + expression_node_id + " }), (p:Person{person_id: '" + expression_owner_id + "' }) CREATE (p)-[:EXPRESSED]->(e)")
	except Exception:
		log.debug('Could not create New Expression Node Owner Relation')
	return


def new_expression_topics(
					topics,
					expression_node_id,
				):
	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	graph = Graph()
	log.debug('Create New Expression Topic Relation')
	for each_topic in topics:
		try:
			graph.cypher.execute("MATCH (e:ExpressionGraph{expression_id: " + expression_node_id + " }), (t:Topic{name: '" + each_topic + "' }) CREATE (e)-[:IN_TOPIC]->(t)")
		except Exception:
			log.debug('Could not create New Expression Topic Relation')
	return

