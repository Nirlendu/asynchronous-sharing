# -*- coding: utf-8 -*-

import sys, inspect
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
	# TODO 
	# 1) Do some logic checks in the data
	# 2) Check if all the topics are present in DB
	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
	log.debug('New Expression Logic')

	core.new_expression_database(
					expression_owner_id = expression_owner_id, 
					expression_content = expression_content, 
					expression_link_id = expression_link_id, 
					expression_imagefile = expression_imagefile,
					broadcast_parent_id = broadcast_parent_id,
					total_upvotes = total_upvotes,
					total_downvotes = total_downvotes,
					total_broadcasts = total_broadcasts,
					topics = topics,
				)
	return




def find_url_id_logic(url):

	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
	log.debug('Find URL logic')
	
	return core.find_url_id_database(url = url)




def store_url_logic(
				url,
				url_header,
				url_desc,
				url_imagefile,
			):

	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
	log.debug('New URL insert logic')

	return core.store_url_database(
							url = url,
							url_header = url_header,
							url_desc = url_desc,
							url_imagefile = url_imagefile
						)


