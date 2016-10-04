# -*- coding: utf-8 -*-

import os, sys

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from libs.image_processor import compressimages
from libs.logger import app_logger as log

import core_logic as core


def new_upload_file(file_content):
	log.info('IN - ' + sys._getframe().f_code.co_name)
	log.info('FROM - ' + sys._getframe(1).f_code.co_name)
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

