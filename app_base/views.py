# -*- coding: utf-8 -*-

import sys
import inspect

import re, os

from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from celery import shared_task

from app_core import core_interface as core

from express.models import Expression, Link
from py2neo import ServiceRoot

from libs.logger import app_logger as log

from libs.device_data import device_data as device
import ujson
import redis


# import logging
# logger = logging.getLogger(__name__)



def mobile_browser(request):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.info('Check if mobile device')

    is_mobile_browser = False
    if str(request.META['HTTP_USER_AGENT']).find('Android') != -1:
        is_mobile_browser = True
    return is_mobile_browser


def init_session(request):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Init the session data')

    request.session['person_name'] = 'Nirlendu Saha'
    request.session['person_id'] = 'asd123'
    request.session['person_profile_photo'] = '/media/somename_bHwPbrb.jpg'

    return


@ensure_csrf_cookie
def index(request):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.info('Index page rendering')

    init_session(request)

    #print 'ENV IS : ' + os.environ['DJANGO_SETTINGS_MODULE']

    try:
        redis_cache = redis.StrictRedis(host='localhost', port=6379, db=0)
        expressions = ujson.loads(redis_cache.hget('asd123','asd123'))
        print "REDIS PRESENT"
    except:
        expressions = core.get_expressions(
            person_id=request.session['person_id'],
        )

    #if mobile_browser(request):
    if device.get_device_data(request).detectTierIphone():
        mobile_template = "m-index.html"
        mobile_page_template = "m-feed-elements.html"
        mobile_context = {
            'Expressions': expressions,
            'page_template': mobile_page_template,
        }
        if request.is_ajax():
            mobile_template = mobile_page_template
        return render(request, mobile_template, mobile_context)

    else:
        template = "index.html"
        page_template = "feed-elements.html"

        context = {
            'Expressions': expressions,
            'page_template': page_template,
        }

        if request.is_ajax():
            template = page_template
        return render(request, template, context)


@ensure_csrf_cookie
def test(request):
    if device.get_device_data(request).detectTierIphone():
        return render(request, 'm-test.html', {})
    return render(request, 'test.html', {})


@ensure_csrf_cookie
def get_index_data(request):
    return None


@ensure_csrf_cookie
def channel(request):
    if mobile_browser(request):
        return render(request, "mobile/index_dev_m.html", {})
    return render(request, "topic_dev.html", {})


@ensure_csrf_cookie
def dev(request):
    return render(request, "index_dev.html", {})
