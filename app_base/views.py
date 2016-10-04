# -*- coding: utf-8 -*-

#import os

#from django.db import connection
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.template.context_processors import request
#import django.core.context_processors.request
from django.views.decorators.csrf import ensure_csrf_cookie
from neomodel import db
from express.models import Expression, Link, ExpressionGraph
from py2neo import Graph
import re
from libs.logger import app_logger as log
# from feed.models import 
#from posts.models import Posts
#from posts.forms import Posts
# list of mobile User Agents
mobile_uas = [
	'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
	'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
	'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
	'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
	'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
	'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
	'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
	'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
	'wapr','webc','winw','winw','xda','xda-'
	]
 
mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone' ]
 
def mobileBrowser(request):
	''' Super simple device detection, returns True for mobile devices '''
 
	mobile_browser = False
	# ua = request.META['HTTP_USER_AGENT'].lower()[0:4]
 
	# if (ua in mobile_uas):
	#     mobile_browser = True
	# else:
	#     for hint in mobile_ua_hints:
	#         if request.META['HTTP_USER_AGENT'].find(hint) > 0:
	#             mobile_browser = True
	if str(request.META['HTTP_USER_AGENT']).find('Android') != -1:
		mobile_browser = True
	return mobile_browser

@ensure_csrf_cookie
def index(request, template="index.html", page_template="feed.html"):
	#log = logger.app_logger()
	log.info('Fetching index page')
	request.session['person_name'] = 'Nirlendu Saha'
	request.session['person_id'] = 'asd123'
	request.session['person_profile_photo'] = '/media/somename_bHwPbrb.jpg'
	# graph = Graph()
	# express = graph.cypher.stream("MATCH (n:Expression) -[:IN_TOPIC]->(Topic{name:'naarada'}), (a:Person{person_id: '"+ request.session['person_id'] + "'})-[:EXPRESSED]->(n) RETURN n");
	# entry=[]
	# #print express
	# for record in express:
	# 	owner = graph.cypher.stream("MATCH (a:Person) -[:EXPRESSED]->(b:Expression{expression_id:'"+record[0]['expression_id']+"'}) return a");
	# 	for x in owner:
	# 		record[0]['expression_owner'] = x[0]['person_name']
	# 		record[0]['expression_owner_id'] = x[0]['id']
	# 		break
	# 	if record[0]['expression_link']!= '':
	# 		entries = Link.objects.filter(link_url = record[0]['expression_link'])
	# 		#print entry
	# 		for entri in entries:
	# 			record[0]['parent_domain'] = re.findall('^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)', record[0]['expression_link'])[0]
	# 			record[0]['expression_link_title'] = entri.link_name
	# 			record[0]['expression_link_image'] = entri.link_image
	# 	entry.append(record[0])




		#print 'ENTRY ' + record[0]['expression_owner']
	# template = "index_dev.html"
	# feed_template = "feed.html"
	# if request.is_ajax():
	# 	template = feed_template
	# print template
	# return render_to_response(
	#     template, context, context_instance=RequestContext(request))
	entry = []
	graph = Graph()
	express = graph.cypher.stream("MATCH (n:ExpressionGraph) -[:IN_TOPIC]->(Topic{name:'naarada'}), (a:Person{person_id: '"+ request.session['person_id'] + "'})-[:EXPRESSED]->(n) RETURN n");
	#express = graph.cypher.stream("MATCH (n:ExpressionGraph), (a:Person{person_id: '"+ request.session['person_id'] + "'})-[:EXPRESSED]->(n) RETURN n");
	for record in express:
		expressions = Expression.objects.filter(id = record[0]['expression_id'])
		for expression in expressions:
			a = {}
			a['expression_id'] = expression.id
			a['expression_owner'] = expression.expression_owner_id
			a['expression_content'] = expression.expression_content
			a['expression_image'] = expression.expression_imagefile
			#expression_link
			#expression_link_title
			#parent_domain		
			if (expression.expression_link_id != None):
				entries = Link.objects.filter(id = expression.expression_link_id)
				for x in entries:
					a['expression_link_title'] = x.link_name
					a['expression_link_image'] = x.link_image
					a['parent_domain'] = re.findall('^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)', x.link_url)[0]
			
			q = graph.cypher.stream("MATCH (p:ExpressionGraph{expression_id: " + str(expression.id) + " }), (e:ExpressionGraph), (p)-[:BROADCAST_OF]->(e) return e")
			if (q):
				#print 'SHARED!'
				for x in q:
					broadcasts = Expression.objects.filter(id = x[0]['expression_id'])
					for broadcast in broadcasts:
						b = {}
						b['expression_id'] = broadcast.id
						b['expression_owner'] = broadcast.expression_owner_id
						b['expression_content'] = broadcast.expression_content
						b['expression_image'] = broadcast.expression_imagefile
						#expression_link
						#expression_link_title
						#parent_domain
						#print 'Link ID' + str(broadcast.expression_link_id)	
						#print 'broadcast conent' + str(broadcast.expression_content)
						if (broadcast.expression_link_id!= None):
							print 'IT DOES HAVE LINKS!'
							entries = Link.objects.filter(id = broadcast.expression_link_id)
							for x in entries:
								#print 'IT DOES HAVE LINKS!'
								b['expression_link_title'] = x.link_name
								b['expression_link_image'] = x.link_image
								b['parent_domain'] = re.findall('^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)', x.link_url)[0]
					a['broadcast_of'] = b
			
			entry.append(a)
	if mobileBrowser(request):
		return render(request, "mobile/index_dev_m.html", {})
	#print entry[0]['expression_content'];
	#return render(request, "index_dev.html", {'Expressions' : entry, 'feed_template' : feed_template})
	context = {
		'Expressions': entry,
		'page_template': page_template,
	}
	if request.is_ajax():
		template = page_template
	#return render_to_response(template, context, context_instance=RequestContext(request))
	return render(request, template, context)

@ensure_csrf_cookie
def topic(request):
	if mobileBrowser(request):
		return render(request, "mobile/index_dev_m.html", {})
	return render(request, "topic_dev.html", {})

