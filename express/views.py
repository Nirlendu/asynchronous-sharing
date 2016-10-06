# -*- coding: utf-8 -*-

import os, urllib, time

#from django.db import connection
from django.conf import settings
#from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.template.context_processors import request
from py2neo import Graph
#from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.views.decorators.csrf import ensure_csrf_cookie
from express.models import Link, Expression, ExpressionGraph
from app_base.models import Topic, Person
from libs.image_processor import compressimages
from app_core import core_interface as core
import re
from libs.logger import app_logger as log



def get_url(text):
	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
	try:
		return urls[0]
	except:
		return None



@ensure_csrf_cookie
def update(request):
	if request.method == 'POST':
		try:
			log.debug('Uploaded file check')
			for filename, file in request.FILES.iteritems():
				data = file
			filename = core.new_upload_file(data)
		except:
			filename = None
		expresssion_text = request.POST.get('express_text')
		url = get_url(expresssion_text)
		if(url):
			expression_content = expresssion_text.replace(url,'')
			link_id = core.find_url_id(url)
		else:
			expression_content = expresssion_text
			link_id = None
		topics = []
		if(request.POST.get('express_tag')):
			topics.append(request.POST.get('express_tag'))
		core.new_expression(
					expression_owner_id = request.session['person_id'], 
					expression_content = expression_content, 
					expression_link_id = link_id, 
					expression_imagefile = filename,
					topics = topics,
				)
		return render(request, "index.html", {})




@ensure_csrf_cookie
def store_link(request):
	if request.method == 'POST':
		url_imagefile = core.store_url_imagefile(
								image_url = request.POST.get('link_image')
							)
		core.store_url(
				url = request.POST.get('link_url'),
				url_header = request.POST.get('link_name'),
				url_desc = request.POST.get('link_desc')[:(len(request.POST.get('link_desc'))%199)],
				url_imagefile = url_imagefile
			)
		template = "index.html"
		context = {}
		return render(request, template, context)




@ensure_csrf_cookie
def upvote(request):
	if request.method == 'POST':
		core.upvote_expression(
				upvoter = request.session['person_id'],
				expression_id = request.POST.get('expression_id'),
			)
		return render(request, "index.html", {})




@ensure_csrf_cookie
def broadcast(request):
	if request.method == 'POST':
		topics = []
		if(request.POST.get('broadcast_tag')):
			topics.append(request.POST.get('broadcast_tag'))
		core.new_broadcast(
						broadcast_owner_id = request.session['person_id'], 
						broadcast_content = request.POST.get('broadcast_text'), 
						broadcast_parent_id = request.POST.get('expression_id'),
						topics = topics,
					)
		return render(request, "index.html", {})




@ensure_csrf_cookie
def discuss(request):
	if request.method == 'POST':
		core.new_discussion_expression(
				discussion_parent_id = request.POST.get('expression_id'),
				discussion_expression_owner_id = request.session['person_id'],
				discussion_expression_content = request.POST.get('discussion_expression_content'),
			)
		return render(request, "index.html", {})








