# -*- coding: utf-8 -*-

import sys, inspect
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
		total_discussions,
		):

	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
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
		total_discussions = total_discussions,
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

	transaction.append("CREATE (a:ExpressionGraph{expression_id : " + expression_id + "})")
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

	transaction.append("MATCH (e:ExpressionGraph{expression_id: " + expression_node_id + " }), (p:Person{person_id: '" + expression_owner_id + "' }) CREATE (p)-[:EXPRESSED]->(e)")
	return transaction




def new_discussion_update_count(
					expression_id,
				):
	
	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
	log.debug('New discussion expression update count')

	expressions = Expression.objects.filter(id = expression_id)
	for expression in expressions:
		expression.total_discussions = expression.total_discussions + 1
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

	expressions = Expression.objects.filter(id = expression_id)
	for expression in expressions:
		expression.total_broadcasts = expression.total_broadcasts + 1
		expression.save()
		return
	return


def new_expression_topics(
					transaction,
					topics,
					expression_node_id,
				):

	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
	log.debug('New Expression Node Topic Relation')

	for each_topic in topics:
		transaction.append("MATCH (e:ExpressionGraph{expression_id: " + expression_node_id + " }), (t:Topic{name: '" + each_topic + "' }) CREATE (e)-[:IN_TOPIC]->(t)")
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
	x = graph.cypher.stream("MATCH (p:Person{person_id:'" + upvoter + "'}), (e:ExpressionGraph{expression_id: " + expression_id + " }), (p)-[r]->(e) return type(r)")
	for i in x:
		if( i[0] == 'UPVOTED' or i[0] == 'DOWNVOTED'):
			return i[0]
	return None


def create_upvote_rel(
			transaction,
			expression_id,
			upvoter,
			condition = None,
		):

	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
	log.debug('Upvote create Relation')

	if(not condition):
		transaction.append("MATCH (p:Person{person_id:'" + upvoter + "'}), (e:ExpressionGraph{expression_id: " + expression_id + " }) CREATE (p)-[:UPVOTED]->(e)")
		return transaction

	if(condition == 'PREV_UPVOTE'):
		transaction.append("MATCH (p:Person{person_id:'" + upvoter + "'}), (e:ExpressionGraph{expression_id: " + expression_id + " }), (p)-[r:UPVOTED]->(e) DELETE r")
		return transaction

	if(condition == 'PREV_DOWNVOTE'):
		transaction.append("MATCH (p:Person{person_id:'" + upvoter + "'}), (e:ExpressionGraph{expression_id: " + expression_id + " }), (p)-[r:DOWNVOTED]->(e) DELETE r CREATE (p)-[:UPVOTED]->(e)")
		return transaction


def update_upvote_count(
			expression_id ,
			condition = None,
		):
	
	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
	log.debug('Upvote changing count')

	if(not condition):
		expressions = Expression.objects.filter(id = expression_id)
		for expression in expressions:
				expression.total_upvotes = expression.total_upvotes + 1
				expression.save()
				return
		return

	if(condition == 'PREV_UPVOTE'):
		expressions = Expression.objects.filter(id = expression_id)
		for expression in expressions:
			expression.total_upvotes = expression.total_upvotes - 1
			expression.save()
			return
		return

	if(condition == 'PREV_DOWNVOTE'):
		expressions = Expression.objects.filter(id = expression_id)
		for expression in expressions:
			expression.total_upvotes = expression.total_upvotes + 1
			expression.total_downvotes = expression.total_downvotes - 1
			expression.save()
			return
		return








