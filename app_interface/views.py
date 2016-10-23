# -*- coding: utf-8 -*-

from django.shortcuts import render

from app_core import core_interface as core

from app_interface.models import ChannelSecondary

from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from channel.models import ChannelPrimary

@ensure_csrf_cookie
def channel(request):
    channel_id = '2'
    #idx = ChannelSecondary.objects.create(channel_primary_id=channel_id, channel_expression_list=[])
    #print idx
    for i in ChannelSecondary.objects.all():
        print "HEYY THE CHANNEL IS: "
    return render(request, "index.html", {})
