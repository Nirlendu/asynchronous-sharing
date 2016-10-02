# -*- coding: utf-8 -*-

import os, urllib, time

#from django.db import connection
from django.conf import settings
from django.shortcuts import render
#from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.views.decorators.csrf import ensure_csrf_cookie
from express.models import Link, Expression, Person
from feed.models import Topic
from image_processor import compressimages
import re

@ensure_csrf_cookie

def update(request):
	if request.method == 'POST':
		try:
			for filename, file in request.FILES.iteritems():
				data = file
			path = default_storage.save('tmp/somename.jpg', ContentFile(data.read()))
			tmp_file = os.path.join(settings.MEDIA_URL, path)
			compressimages.processfile(tmp_file)
		except:
			tmp_file = ''
		text = request.POST.get('express_text')
		link = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
		text.replace(link[0],'')
		print text
		print link[0]
		expression = Expression(
			expression_id = str(round(time.time() * 1000)),
			expression_content = text, 
			expression_image = tmp_file, 
			expression_link = link[0]
			).save()
		person = Person.nodes.get(person_id=request.session['person_id'])
		expression.expression_owner.connect(person)
		try:
			topic = Topic.nodes.get(name=request.POST.get('express_tag'))
			topic.related_posts.connect(expression)
		except:
			pass
		return render(request, "index.html", {})

def store_link(request):
	if request.method == 'POST':
		try:
			image_file = str(round(time.time() * 1000)) + '.jpg'
			urllib.urlretrieve(request.POST.get('link_image'), os.path.join(settings.MEDIA_ROOT, image_file))
			image_file_name = os.path.join(settings.MEDIA_URL, image_file)
		except:
			image_file_name = ''
		link = Link.objects.store_link(
				request.POST.get('link_url'),
				request.POST.get('link_name'),
				request.POST.get('link_desc'),
				image_file_name
			)
		return render(request, "index.html", {})