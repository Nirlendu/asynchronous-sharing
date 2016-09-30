# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import url
from feed.views import index, topic, upvote
from express.views import update, store_link
from django.conf.urls.static import static
#from neo4django import admin as neo_admin

urlpatterns = [
	url(r'^express/update/$', update),
	url(r'^dev/$', index),
	url(r'^$', topic),
	url(r'store/link/$', store_link),	
	url(r'expression/upvote/$', upvote),
	#url(r'^neo_admin/', include(neo_admin.site.urls))
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)