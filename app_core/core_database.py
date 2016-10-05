# -*- coding: utf-8 -*-

import sys, inspect
from py2neo import Graph
from libs.logger import app_logger as log
from django.db import transaction
from app_core_database import new_expression, expressed_url, new_broadcast


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
	log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
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


def find_url_id_database(url):

	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
	log.debug('Find URL database')

	return expressed_url.find_url_id(url = url)


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
							url = url,
							url_header = url_header,
							url_desc = url_desc,
							url_imagefile = url_imagefile,
						)


@transaction.atomic
def new_broadcast_database(
			broadcast_owner_id , 
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

	expression_id = new_expression.new_expression_insert(
										expression_owner_id = broadcast_owner_id, 
										expression_content = broadcast_content, 
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
															expression_owner_id = broadcast_owner_id
														)
	new_broadcast_transaction = new_expression.new_expression_topics(
											transaction = expression_relationship_transaction,
											topics = topics,
											expression_node_id = str(expression_id),
										)
	# TODO
	# MAKE THE FOLLOWING 3 QUERIES IN 1 TRANSACTION
	is_parent_broadcast = new_broadcast.check_parent_broadcast(
										broadcast_parent_id = broadcast_parent_id,
									)

	if(not is_parent_broadcast):
		final_transaction = new_broadcast.new_broadcast_relation(
										transaction = new_broadcast_transaction,
										expression_id = str(expression_id),
										broadcast_parent_id = broadcast_parent_id,
									)
	else:
		final_transaction = new_broadcast.new_broadcast_relation(
											transaction = new_broadcast_transaction,
											expression_id = str(expression_id),
											broadcast_parent_id = str(is_parent_broadcast),
										)
	try:
		final_transaction.process()
	except:
		final_transaction.rollback()
		raise Exception
	final_transaction.commit()
	return






