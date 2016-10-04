# -*- coding: utf-8 -*-

import sys
import core_database as core
from libs.logger import app_logger as log

def new_expression_logic(
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
	log.debug('New Expression Logic')
	expression_id = core.new_expression_insert(
						expression_owner_id = expression_owner_id, 
						expression_content = expression_content, 
						expression_link_id = expression_link_id, 
						expression_imagefile = expression_imagefile,
						broadcast_parent_id = broadcast_parent_id,
						total_upvotes = total_upvotes,
						total_downvotes = total_downvotes,
						total_broadcasts = total_broadcasts,
					)
	expression_node = core.new_expression_node(
							expression_id = expression_id,
						)
	core.new_expression_relationship(
			expression_node_id = str(expression_node.expression_id),
			expression_owner_id = expression_owner_id
		)
	core.new_expression_topics(
		topics = topics,
		expression_node_id = str(expression_node.expression_id),
		)
	return
	