# -*- coding: utf-8 -*-

#import os

#from django.db import connection
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from neomodel import db
from express.models import Expression
from py2neo import Graph
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
def index(request):
	request.session['person_name'] = 'Nirlendu Saha'
	request.session['person_id'] = 'asd123'
	request.session['person_profile_photo'] = '/media/somename_bHwPbrb.jpg'
	graph = Graph()
	express = graph.cypher.stream("MATCH (n:Expression) -[:IN_TOPIC]->(Topic{name:'naarada'}), (a:Person{person_id: '"+ request.session['person_id'] + "'})-[:EXPRESSED]->(n) RETURN n");
	entry=[]
	#print express
	for record in express:
		entry.append(record[0])
	if mobileBrowser(request):
		return render(request, "mobile/index_dev_m.html", {})
	#print entry[0]['expression_content'];
	return render(request, "index_dev.html", {'Expressions' : entry})

@ensure_csrf_cookie
def topic(request):
	if mobileBrowser(request):
		return render(request, "mobile/index_dev_m.html", {})
	return render(request, "topic_dev.html", {})