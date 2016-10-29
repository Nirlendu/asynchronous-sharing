# -*- coding: utf-8 -*-

import inspect
import sys
import urllib
import uuid

import os
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from libs.image_processor import compressimages
from libs.logger import app_logger as log
import boto
from boto.s3.key import Key

def new_upload_file(file_content):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('File Uploading..')

    path = default_storage.save('upload/upload.jpg', ContentFile(file_content.read()))
    filename = os.path.join('/media/', path)
    compressimages.image_upload(filename)
    return boto_storage(filename)


def boto_storage(filename):
    if os.environ['DJANGO_SETTINGS_MODULE'] == 'core.settings.local':
        return filename
    else:
        os.environ['S3_USE_SIGV4'] = 'True'
        conn = boto.connect_s3(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY, host='s3.ap-south-1.amazonaws.com')
        my_key = Key(conn.get_all_buckets()[0], filename)
        print 'IN HERE' + str(os.environ['DJANGO_SETTINGS_MODULE']) + filename
        my_key.set_contents_from_filename(os.path.join(settings.BASE_DIR,filename[1:]))
        my_key.make_public()
        return settings.MEDIA_URL + filename[1:]


def store_url_imagefile(image_url):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Store URL Imagefile')

    try:
        image_file = 'url_images/' + str(uuid.uuid4())[:16] + '.jpg'
        urllib.urlretrieve(image_url, os.path.join('media/', image_file))
        filename =  os.path.join('/media/', image_file)
        return boto_storage(filename)
    except:
        return None