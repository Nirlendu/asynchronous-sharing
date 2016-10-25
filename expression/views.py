# -*- coding: utf-8 -*-

import re, sys, inspect

from app_core import core_interface as core
from libs.logger import app_logger as log


def get_url(text):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    try:
        return urls[0]
    except:
        return None


def new_expression(
        expression_owner_id,
        expression_text,
        expression_imagefile,
        channels,
    ):

    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.info('New Expression expression views')

    url = get_url(expression_text)
    if url:
        expression_content = expresssion_text.replace(url, '')
        url_id = core.find_url_id(url)
    else:
        expression_content = expresssion_text
        url_id = None
    core.new_expression(
                expression_owner_id=expression_owner_id,
                expression_content=expression_content,
                expression_content_url=url_id,
                expression_imagefile=expression_imagefile,
                channels=channels,
            )
    return


# @ensure_csrf_cookie
# def update(request):
#     if request.method == 'POST':
#         try:
#             log.debug('Uploaded file check')
#             for filename, file in request.FILES.iteritems():
#                 data = file
#             filename = core.new_upload_file(data)
#         except:
#             filename = None
#         expresssion_text = request.POST.get('express_text')
#         url = get_url(expresssion_text)
#         if url:
#             expression_content = expresssion_text.replace(url, '')
#             link_id = core.find_url_id(url)
#         else:
#             expression_content = expresssion_text
#             link_id = None
#         channels = []
#         if request.POST.get('express_tag'):
#             #channels.append(request.POST.get('express_tag'))
#             channels.append('7dea7440-c4b3-4bf0-8568-0b552c9d7bf5')
#         core.new_expression(
#             expression_owner_id=request.session['person_id'],
#             expression_content=expression_content,
#             expression_content_url=link_id,
#             expression_imagefile=filename,
#             channels=channels,
#         )
#         return render(request, "index.html", {})
#
#
# @ensure_csrf_cookie
# def store_link(request):
#     if request.method == 'POST':
#         url_imagefile = core.store_url_imagefile(
#             image_url=request.POST.get('link_image')
#         )
#         core.store_url(
#             url=request.POST.get('link_url'),
#             url_title=request.POST.get('link_name'),
#             url_desc=request.POST.get('link_desc')[:(len(request.POST.get('link_desc')) % 199)],
#             url_imagefile=url_imagefile
#         )
#         template = "index.html"
#         context = {}
#         return render(request, template, context)
#
#
# @ensure_csrf_cookie
# def upvote(request):
#     if request.method == 'POST':
#         core.upvote_expression(
#             upvoter=request.session['person_id'],
#             expression_id=request.POST.get('expression_id'),
#         )
#         return render(request, "index.html", {})
#
#
# @ensure_csrf_cookie
# def downvote(request):
#     if request.method == 'POST':
#         core.downvote_expression(
#             downvoter=request.session['person_id'],
#             expression_id=request.POST.get('expression_id'),
#         )
#         return render(request, "index.html", {})
#
#
# @ensure_csrf_cookie
# def broadcast(request):
#     if request.method == 'POST':
#         topics = []
#         if (request.POST.get('broadcast_tag')):
#             topics.append(request.POST.get('broadcast_tag'))
#         core.new_broadcast(
#             broadcast_owner_id=request.session['person_id'],
#             broadcast_content=request.POST.get('broadcast_text'),
#             broadcast_parent_id=request.POST.get('expression_id'),
#             topics=topics,
#         )
#         return render(request, "index.html", {})
#
#
# @ensure_csrf_cookie
# def discuss(request):
#     if request.method == 'POST':
#         core.new_discussion_expression(
#             discussion_parent_id=request.POST.get('expression_id'),
#             discussion_expression_owner_id=request.session['person_id'],
#             discussion_expression_content=request.POST.get('discussion_expression_content'),
#         )
#         return render(request, "index.html", {})
