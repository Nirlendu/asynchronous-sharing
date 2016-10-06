# -*- coding: utf-8 -*-

import sys, inspect
from py2neo import Graph
from libs.logger import app_logger as log
from django.db import transaction
from express.models import Expression


def check_parent_broadcast(
		broadcast_parent_id
		):

	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
	log.debug('Checking parent broadcast')

	graph = Graph()
	is_parent_broadcast = graph.cypher.stream("MATCH (p:ExpressionGraph{expression_id: " + broadcast_parent_id + " }), (e:ExpressionGraph), (p)-[:BROADCAST_OF]->(e) return e")
	for each in is_parent_broadcast:
		return each[0]['expression_id']
	return None



# def new_broadcast_relation(
# 				transaction,
# 				expression_id,
# 				broadcast_parent_id
# 			):

# 	log.info('IN - ' + sys._getframe().f_code.co_name)
# 	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
# 	log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
# 	log.debug('Creating New Broadcast Realationship')

# 	#query = "MATCH (b:ExpressionGraph{expression_id: " + broadcast_parent_id + " }), (e:ExpressionGraph), (b)-[:BROADCAST_OF]->(e)" + "CASE (e)" + "WHEN NULL THEN (MATCH (p:ExpressionGraph{expression_id: " + expression_id + " }) CREATE (p)-[:BROADCAST_OF]->(b))" + "ELSE (MATCH (p:ExpressionGraph{expression_id: " + expression_id + " }) CREATE (p)-[:BROADCAST_OF]->(e))"
# 	query = "MATCH (b:ExpressionGraph{expression_id: "+ broadcast_parent_id +" }), (e:ExpressionGraph),(b)-[:BROADCAST_OF]->(e) return CASE (b) WHEN NULL THEN MATCH (p:ExpressionGraph{expression_id: "+ expression_id +" }) CREATE (p)-[:BROADCAST_OF]->(b) ELSE MATCH (p:ExpressionGraph{expression_id: " + expression_id +" }) CREATE (p)-[:BROADCAST_OF]->(e) END"
# 	transaction.append(query)
# 	return transaction


def new_broadcast_relation(
					transaction,
					expression_id ,
					broadcast_parent_id ,
				):

	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
	log.debug('Creating New Broadcast Realationship')

	transaction.append("MATCH (p:ExpressionGraph{expression_id: " + broadcast_parent_id + " }), (e:ExpressionGraph{expression_id: " + expression_id + " }) CREATE (e)-[:BROADCAST_OF]->(p)")
	return transaction





