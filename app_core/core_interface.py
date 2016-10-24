# -*- coding: utf-8 -*-

import inspect
import sys
import urllib
import uuid

import os
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

import core_logic as core
from libs.image_processor import compressimages
from libs.logger import app_logger as log


def get_expressions(
            person_id,
        ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Fetching expressions interface..')

    return core.get_expressions_logic(
        person_id=person_id,
    )


# def new_upload_file(file_content):
#     log.info('IN - ' + sys._getframe().f_code.co_name)
#     log.info('FROM - ' + sys._getframe(1).f_code.co_name)
#     log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
#     log.debug('File Uploading..')
#
#     path = default_storage.save('upload/upload.jpg', ContentFile(file_content.read()))
#     filename = os.path.join('/media/', path)
#     compressimages.image_upload(filename)
#     return boto_storage(filename)
#
#
# def boto_storage(filename):
#     if os.environ['DJANGO_SETTINGS_MODULE'] == 'core.settings.local':
#         print 'IN LOCAL'
#         return filename
#     else:
#         os.environ['S3_USE_SIGV4'] = 'True'
#         import boto
#         from boto.s3.key import Key
#         conn = boto.connect_s3(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY, host='s3.ap-south-1.amazonaws.com')
#         my_key = Key(conn.get_all_buckets()[0], filename)
#         print 'IN HERE' + str(os.environ['DJANGO_SETTINGS_MODULE']) + filename
#         my_key.set_contents_from_filename(os.path.join(settings.BASE_DIR,filename[1:]))
#         my_key.make_public()
#         return settings.MEDIA_URL + filename[1:]
#
#
# def store_url_imagefile(image_url):
#     log.info('IN - ' + sys._getframe().f_code.co_name)
#     log.info('FROM - ' + sys._getframe(1).f_code.co_name)
#     log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
#     log.debug('Store URL Imagefile')
#
#     try:
#         image_file = 'url_images/' + str(uuid.uuid4())[:16] + '.jpg'
#         urllib.urlretrieve(image_url, os.path.join('media/', image_file))
#         filename =  os.path.join('/media/', image_file)
#         return boto_storage(filename)
#         # return settings.MEDIA_URL + filename[1:]
#     except:
#         return None


def new_expression(
        expression_owner_id,
        expression_content,
        expression_content_url=None,
        expression_imagefile=None,
        expression_weight=0,
        broadcast_parent_id=None,
        total_upvotes=0,
        total_collects=0,
        total_broadcasts=0,
        total_discussions=0,
        channels=[],
    ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New Expression Interface')

    # TODO
    # 1) Parse the contents and do some stuff
    # 2) Determine appropriate topics not provided
    return core.new_expression_logic(
        expression_owner_id=expression_owner_id,
        expression_content=expression_content,
        expression_content_url=expression_content_url,
        expression_imagefile=expression_imagefile,
        expression_weight=expression_weight,
        broadcast_parent_id=broadcast_parent_id,
        total_upvotes=total_upvotes,
        total_collects=total_collects,
        total_broadcasts=total_broadcasts,
        total_discussions=total_discussions,
        channels=channels,
    )


def store_url_interface(
        url,
        url_title,
        url_desc=None,
        url_imagefile=None,
        url_weight=0,
):
    # TODO
    # Some checks on the url
    # Some data about the url

    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New URL INSERT')

    return core.store_url_logic(
        url=url,
        url_title=url_title,
        url_desc=url_desc,
        url_imagefile=url_imagefile,
        url_weight=url_weight,
    )


def find_url_id(url):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Find URL')

    return core.find_url_id_logic(url=url)


# def new_broadcast(
#         broadcast_owner_id,
#         broadcast_content,
#         broadcast_parent_id,
#         expression_link_id=None,
#         expression_imagefile=None,
#         total_upvotes=0,
#         total_downvotes=0,
#         total_broadcasts=0,
#         total_discussions=0,
#         topics=[],
# ):
#     log.info('IN - ' + sys._getframe().f_code.co_name)
#     log.info('FROM - ' + sys._getframe(1).f_code.co_name)
#     log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
#     log.debug('New Broadcast Interface')
#
#     return core.new_broadcast_logic(
#         broadcast_owner_id=broadcast_owner_id,
#         broadcast_content=broadcast_content,
#         expression_link_id=expression_link_id,
#         expression_imagefile=expression_imagefile,
#         broadcast_parent_id=broadcast_parent_id,
#         total_upvotes=total_upvotes,
#         total_downvotes=total_downvotes,
#         total_broadcasts=total_broadcasts,
#         total_discussions=total_discussions,
#         topics=topics,
#     )
#
#
# def new_discussion_expression(
#         discussion_parent_id,
#         discussion_expression_owner_id,
#         discussion_expression_content,
#         discussion_expression_link_id=None,
#         discussion_expression_imagefile=None,
#         total_upvotes=0,
#         total_downvotes=0,
# ):
#     log.info('IN - ' + sys._getframe().f_code.co_name)
#     log.info('FROM - ' + sys._getframe(1).f_code.co_name)
#     log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
#     log.debug('New discussion expression Interface')
#
#     return core.new_discussion_expression_logic(
#         discussion_parent_id=discussion_parent_id,
#         discussion_expression_owner_id=discussion_expression_owner_id,
#         discussion_expression_content=discussion_expression_content,
#         discussion_expression_link_id=discussion_expression_link_id,
#         discussion_expression_imagefile=discussion_expression_imagefile,
#         total_upvotes=total_upvotes,
#         total_downvotes=total_downvotes,
#     )
#
#
# def upvote_expression(
#         upvoter,
#         expression_id,
# ):
#     log.info('IN - ' + sys._getframe().f_code.co_name)
#     log.info('FROM - ' + sys._getframe(1).f_code.co_name)
#     log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
#     log.debug('Upvote expression Interface')
#
#     return core.upvote_expression_logic(
#         upvoter=upvoter,
#         expression_id=expression_id,
#     )
#
#
# def downvote_expression(
#         downvoter,
#         expression_id,
# ):
#     log.info('IN - ' + sys._getframe().f_code.co_name)
#     log.info('FROM - ' + sys._getframe(1).f_code.co_name)
#     log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
#     log.debug('Downvote expression Interface')
#
#     return core.downvote_expression_logic(
#         downvoter=downvoter,
#         expression_id=expression_id,
#     )
