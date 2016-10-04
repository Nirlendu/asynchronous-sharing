# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import url
from app_base.views import index, topic
from express.views import update, store_link, upvote, broadcast
from django.conf.urls.static import static
#from neo4django import admin as neo_admin

urlpatterns = [
	url(r'^express/update/$', update),
	url(r'^topic/$', topic),
	url(r'^$', index),
	url(r'store/link/$', store_link),	
	url(r'expression/upvote/$', upvote),
	url(r'expression/broadcast/$', broadcast),
	#url(r'^neo_admin/', include(neo_admin.site.urls))
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)