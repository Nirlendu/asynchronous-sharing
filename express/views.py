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
import re


@ensure_csrf_cookie
def update(request):
	if request.method == 'POST':
		try:
			for filename, file in request.FILES.iteritems():
				data = file
			path = default_storage.save('tmp/somename.jpg', ContentFile(data.read()))
			tmp_file = os.path.join(settings.MEDIA_URL, path)
			compressimages.image_upload(tmp_file)
		except:
			tmp_file = None
		text = request.POST.get('express_text')
		link = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
		try:
			trimmed_text = text.replace(link[0],'')
			text_url = link[0]
		except:
			trimmed_text = text
			text_url = ''
		# #print 'TRIMEED TEXT IS :' + trimmed_text
		# #print link[0]
		# expression = Expression(
		# 	expression_id = str(round(time.time() * 1000)),
		# 	expression_content = trimmed_text, 
		# 	expression_image = tmp_file, 
		# 	expression_link = text_url
		# 	).save()
		# person = Person.nodes.get(person_id=request.session['person_id'])
		# expression.expression_owner.connect(person)
		# try:
		# 	topic = Topic.nodes.get(name=request.POST.get('express_tag'))
		# 	#print 'EXPRESS TAG!' + request.POST.get('express_tag')
		# 	#topic.related_posts.connect(expression)
		# 	expression.in_topic.connect(topic)
		# except:
		# 	pass
		if(text_url!=''):
			link = Link.objects.filter(link_url = text_url)
			for entries in link:
				link_id = entries.pk;
				break;
		else:
			link_id = None
		expression_id = Expression.objects.store_expression(
				expression_owner_id = request.session['person_id'], 
				expression_content = trimmed_text, 
				expression_link_id = link_id, 
				expression_imagefile = tmp_file,
			)
		expression = ExpressionGraph(
			expression_id = expression_id,
			).save()
		person = Person.nodes.get(person_id=request.session['person_id'])
		expression.expression_owner.connect(person)
		try:
			topic = Topic.nodes.get(name=request.POST.get('express_tag'))
			expression.in_topic.connect(topic)
		except:
			pass
		return render(request, "index.html", {})



@ensure_csrf_cookie
def store_link(request):
	if request.method == 'POST':
		try:
			image_file = str(round(time.time() * 1000)) + '.jpg'
			urllib.urlretrieve(request.POST.get('link_image'), os.path.join(settings.MEDIA_ROOT, image_file))
			image_file_name = os.path.join(settings.MEDIA_URL, image_file)
			#compressimages.image_upload(tmp_file)
		except:
			image_file_name = ''
		#print 'LINK URL IS : ' + request.POST.get('link_url')
		link = Link.objects.store_link(
				request.POST.get('link_url'),
				request.POST.get('link_name'),
				request.POST.get('link_desc'),
				image_file_name
			)
		#print "LINK IS STRED MAYBE:"  + link.link_url
		template = "index.html"
		context = {}
		return render(request, template, context)



@ensure_csrf_cookie
def upvote(request):
	expression_id = request.POST.get('expression_id')
	person_id = request.session['person_id']
	#Expression.upvoter
	graph = Graph()
	#graph.cypher.stream("CREATE (a:Person), (b:Expression), (a)-[:UPVOTED]->(b) WHERE a.person_id = '" + person_id + "', b.expression_id ='" + expression_id + "'");
	graph.cypher.stream("MATCH (p:Person{person_id:'" + person_id + "'}), (e:Expression{expression_id:'" + expression_id + "'}) CREATE (p)-[:UPVOTED]->(e)")
	return render(request, "index.html", {})