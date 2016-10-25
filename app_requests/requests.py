# -*- coding: utf-8 -*-

import sys
import inspect

import re, os
import ujson
import redis

from celery import shared_task

from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from app_core import core_interface as core
#from app_interface.models import ChannelSecondary
#from channel.models import ChannelPrimary

from expression import views as expression
from web import views as web
from people import views as people

from libs.logger import app_logger as log
from libs.file_upload import uploader
from libs.device_data import device_data as device

# @ensure_csrf_cookie
# def channel(request):
#     channel_id = '2'
#     #idx = ChannelSecondary.objects.create(channel_primary_id=channel_id, channel_expression_list=[])
#     #print idx
#     for i in ChannelSecondary.objects.all():
#         print "HEYY THE CHANNEL IS: "
#     return render(request, "index.html", {})


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
def update(request):
    if request.method == 'POST':
        try:
            log.debug('Uploaded file check')
            for filename, file_data in request.FILES.iteritems():
                data = file_data
            filename = uploader.new_upload_file(data)
        except:
            filename = None
        expression_text = request.POST.get('express_text')
        channels = []
        if request.POST.get('express_tag'):
            channels.append(request.POST.get('express_tag'))
            #channels.append('7dea7440-c4b3-4bf0-8568-0b552c9d7bf5')
        expression.new_expression(
            expression_owner_id=request.session['person_id'],
            expression_text=expression_text,
            expression_imagefile=filename,
            channels=channels,
        )
        return render(request, "index.html", {})


@ensure_csrf_cookie
def store_link(request):
    if request.method == 'POST':
        url_imagefile = uploader.store_url_imagefile(
            image_url=request.POST.get('link_image')
        )
        web.store_url(
            url=request.POST.get('link_url'),
            url_title=request.POST.get('link_name'),
            url_desc=request.POST.get('link_desc')[:(len(request.POST.get('link_desc')) % 199)],
            url_imagefile=url_imagefile
        )
        template = "index.html"
        context = {}
        return render(request, template, context)


@ensure_csrf_cookie
def init(request):
    person_secondary_id = people.new_person(
        user_name = request.session['person_id'],
        person_name = 'Nirlendu Saha',
    )


#
#
#
#
# Unused till now
#
#
#
#
#
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
@ensure_csrf_cookie
def upvote(request):
    if request.method == 'POST':
        core.upvote_expression(
            upvoter=request.session['person_id'],
            expression_id=request.POST.get('expression_id'),
        )
        return render(request, "index.html", {})


@ensure_csrf_cookie
def downvote(request):
    if request.method == 'POST':
        core.downvote_expression(
            downvoter=request.session['person_id'],
            expression_id=request.POST.get('expression_id'),
        )
        return render(request, "index.html", {})


@ensure_csrf_cookie
def broadcast(request):
    if request.method == 'POST':
        topics = []
        if (request.POST.get('broadcast_tag')):
            topics.append(request.POST.get('broadcast_tag'))
        core.new_broadcast(
            broadcast_owner_id=request.session['person_id'],
            broadcast_content=request.POST.get('broadcast_text'),
            broadcast_parent_id=request.POST.get('expression_id'),
            topics=topics,
        )
        return render(request, "index.html", {})


@ensure_csrf_cookie
def discuss(request):
    if request.method == 'POST':
        core.new_discussion_expression(
            discussion_parent_id=request.POST.get('expression_id'),
            discussion_expression_owner_id=request.session['person_id'],
            discussion_expression_content=request.POST.get('discussion_expression_content'),
        )
        return render(request, "index.html", {})
