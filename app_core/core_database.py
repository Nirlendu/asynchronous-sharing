# -*- coding: utf-8 -*-

import sys
from py2neo import Graph
from libs.logger import app_logger as log
from django.db import transaction
from app_core_database import new_expression


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
			topics,
		):
	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.debug('New Expression Core Database')
	expression_id = new_expression.new_expression_insert(
										expression_owner_id = expression_owner_id, 
										expression_content = expression_content, 
										expression_link_id = expression_link_id, 
										expression_imagefile = expression_imagefile,
										broadcast_parent_id = broadcast_parent_id,
										total_upvotes = total_upvotes,
										total_downvotes = total_downvotes,
										total_broadcasts = total_broadcasts,
									)
	graph = Graph()
	intial_transaction = graph.cypher.begin()
	expression_node_transaction = new_expression.new_expression_node(
													transaction = intial_transaction,
													expression_id = str(expression_id),
												)
	expression_relationship_transaction = new_expression.new_expression_relationship(
															transaction = expression_node_transaction,
															expression_node_id = str(expression_id),
															expression_owner_id = expression_owner_id
														)
	final_transaction = new_expression.new_expression_topics(
											transaction = expression_relationship_transaction,
											topics = topics,
											expression_node_id = str(expression_id),
										)
	try:
		final_transaction.process()
	except:
		final_transaction.rollback()
		raise Exception
	final_transaction.commit()
	return

