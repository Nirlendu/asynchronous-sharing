# -*- coding: utf-8 -*-

import os, sys, urllib, uuid, inspect

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from libs.image_processor import compressimages
from libs.logger import app_logger as log

import core_logic as core



def new_upload_file(file_content):

	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
	log.debug('File Uploading..')

	path = default_storage.save('upload/upload.jpg', ContentFile(file_content.read()))
	filename = os.path.join(settings.MEDIA_URL, path)
	compressimages.image_upload(filename)
	return filename



def new_expression(
		expression_owner_id, 
		expression_content, 
		expression_link_id=None, 
		expression_imagefile=None,
		broadcast_parent_id=None,
		total_upvotes=0,
		total_downvotes=0,
		total_broadcasts=0,
		topics = [],
		):

	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
	log.debug('New Expression Interface')

	# TODO
	# 1) Parse the contents and do some stuff
	# 2) Determine appropriate topics not provided
	return core.new_expression_logic(
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



def store_url_imagefile(image_url):

	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
	log.debug('Store URL Imagefile')

	try:
		image_file = 'url_images/' + str(uuid.uuid4())[:16] + '.jpg'
		urllib.urlretrieve(image_url , os.path.join(settings.MEDIA_ROOT, image_file))
		return os.path.join(settings.MEDIA_URL, image_file)
	except:
		return None



def store_url(
			url,
			url_header,
			url_desc,
			url_imagefile,
		):
	# TODO
	# Some checks on the url
	# Some data about the url

	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
	log.debug('New URL INSERT')

	return core.store_url_logic(
						url = url,
						url_header = url_header,
						url_desc = url_desc,
						url_imagefile = url_imagefile
					)


def find_url_id(url):

	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
	log.debug('Find URL')

	return core.find_url_id_logic(url = url)



def new_broadcast(
			broadcast_owner_id, 
			broadcast_content,
			broadcast_parent_id, 
			expression_link_id=None, 
			expression_imagefile=None,
			total_upvotes=0,
			total_downvotes=0,
			total_broadcasts=0,
			topics = [],
		):
	
	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
	log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
	log.debug('New Broadcast Interface')

	return core.new_broadcast_logic(
				broadcast_owner_id = broadcast_owner_id, 
				broadcast_content = broadcast_content,
				expression_link_id = expression_link_id, 
				expression_imagefile = expression_imagefile,
				broadcast_parent_id = broadcast_parent_id,
				total_upvotes = total_upvotes,
				total_downvotes = total_downvotes,
				total_broadcasts = total_broadcasts,
				topics = topics,
			)


