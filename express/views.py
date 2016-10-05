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
			for filename, file in request.FILES.iteritems():
				data = file
			log.debug('Uploaded file present')
			filename = core.new_upload_file(data)
		except:
			filename = None
		expresssion_text = request.POST.get('express_text')
		url = get_url(expresssion_text)
		if(url):
			expression_content = expresssion_text.replace(url,'')
			link_id = core.find_url_id(url)
		topics = []
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
	expression_id = request.POST.get('expression_id')
	person_id = request.session['person_id']
	graph = Graph()
	x = graph.cypher.stream("MATCH (p:Person{person_id:'" + person_id + "'}), (e:ExpressionGraph{expression_id: " + expression_id + " }), (p)-[r]->(e) return type(r)")
	is_exist = False
	for i in x:
		if i[0] == 'DOWNVOTED':
			graph.cypher.stream("MATCH (p:Person{person_id:'" + person_id + "'}), (e:ExpressionGraph{expression_id: " + expression_id + " }), (p)-[r:DOWNVOTED]->(e) DELETE r CREATE (p)-[:UPVOTED]->(e)")
			expressions = Expression.objects.filter(id = expression_id)
			for expression in expressions:
				expression.total_upvotes = expression.total_upvotes + 1
				expression.total_downvotes = expression.total_downvotes - 1
				expression.save()
				is_exist = True
				break
		if i[0] == 'UPVOTED':
			graph.cypher.stream("MATCH (p:Person{person_id:'" + person_id + "'}), (e:ExpressionGraph{expression_id: " + expression_id + " }), (p)-[r:UPVOTED]->(e) DELETE r")
			expressions = Expression.objects.filter(id = expression_id)
			for expression in expressions:
				expression.total_upvotes = expression.total_upvotes - 1
				expression.save()
				is_exist = True
				break
	if(not is_exist):
		graph.cypher.stream("MATCH (p:Person{person_id:'" + person_id + "'}), (e:ExpressionGraph{expression_id: " + expression_id + " }) CREATE (p)-[:UPVOTED]->(e)")
		expressions = Expression.objects.filter(id = expression_id)
		for expression in expressions:
				expression.total_upvotes = expression.total_upvotes + 1
				expression.save()
				break
	return render(request, "index.html", {})


@ensure_csrf_cookie
def broadcast(request):
	expression_id = Expression.objects.store_expression(
				expression_owner_id = request.session['person_id'], 
				expression_content = request.POST.get('broadcast_text'), 
				broadcast_parent_id = request.POST.get('expression_id')
			)
	expression = ExpressionGraph(
		expression_id = expression_id,
		).save()
	person = Person.nodes.get(person_id=request.session['person_id'])
	expression.expression_owner.connect(person)
	try:
		topic = Topic.nodes.get(name=request.POST.get('broadcast_tag'))
		expression.in_topic.connect(topic)
	except:
		pass
	graph = Graph()
	z = graph.cypher.stream("MATCH (p:ExpressionGraph{expression_id: " + request.POST.get('expression_id') + " }), (e:ExpressionGraph), (p)-[:BROADCAST_OF]->(e) return e")
	for x in z:
		graph.cypher.stream("MATCH (p:ExpressionGraph{expression_id: " + str(x[0]['expression_id']) + " }), (e:ExpressionGraph{expression_id: " + str(expression.expression_id) + " }) CREATE (e)-[:BROADCAST_OF]->(p)")
		return render(request, "index.html", {})
	graph.cypher.stream("MATCH (p:ExpressionGraph{expression_id: " + request.POST.get('expression_id') + " }), (e:ExpressionGraph{expression_id: " + str(expression.expression_id) + " }) CREATE (e)-[:BROADCAST_OF]->(p)")
	return render(request, "index.html", {})









