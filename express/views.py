# -*- coding: utf-8 -*-

import os, urllib, time

#from django.db import connection
from django.conf import settings
from django.shortcuts import render
#from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.views.decorators.csrf import ensure_csrf_cookie
from express.models import Link, Posts
from feed.models import Topic

@ensure_csrf_cookie

def update(request):
	if request.method == 'POST':
		try:
			for filename, file in request.FILES.iteritems():
				data = file
			path = default_storage.save('tmp/somename.jpg', ContentFile(data.read()))
			tmp_file = os.path.join(settings.MEDIA_ROOT, path)
		except:
			tmp_file = ''
		#print request.POST
		#print 'Post Text is! :'
		#print request.POST.get('express_text')
		post = Posts(
			post_content = request.POST.get('express_text'), 
			post_image = tmp_file, 
			post_link = ''
			).save()
		topic = Topic.nodes.get(name='naarada')
		#post.in_topic.connect(topic)
		topic.related_posts.connect(post)
		return render(request, "index.html", {})

def store_link(request):
	if request.method == 'POST':
		try:
			image_file_name = str(round(time.time() * 1000)) + '.jpg'
			urllib.urlretrieve(request.POST.get('link_image'), os.path.join(settings.MEDIA_ROOT, image_file_name))
		except:
			image_file_name = ''
		link = Link.objects.store_link(
				request.POST.get('link_name'),
				request.POST.get('link_desc'),
				image_file_name
			)
		return update(request)
