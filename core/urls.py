# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

# from app_base.views import
from app_requests.requests import channel, index, dev, get_index_data, test, \
    update, store_link, upvote, downvote, broadcast, discuss, init
from app_test.views import react_webpack_test, react_pre_render_test

# from neo4django import admin as neo_admin

urlpatterns = [
    url(r'^express/update/$', update),
    #url(r'^topic/$', topic),
    url(r'^$', index),
    url(r'init/$', init),
    url(r'store/link/$', store_link),
    url(r'expression/upvote/$', upvote),
    url(r'expression/downvote/$', downvote),
    url(r'expression/broadcast/$', broadcast),
    url(r'test/$', test),
    url(r'channel/$', channel),
    url(r'test/react-webpack-test/$', react_webpack_test),
    url(r'test/react-pre-render-test/$', react_pre_render_test),
    url(r'expression/discuss/$', discuss),
    url(r'dev/$', dev),
    url(r'api/get_index_data', get_index_data),
    # url(r'^neo_admin/', include(neo_admin.site.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
