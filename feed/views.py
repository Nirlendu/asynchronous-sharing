# -*- coding: utf-8 -*-

#import os

#from django.db import connection
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
#from posts.models import Posts
#from posts.forms import Posts

@ensure_csrf_cookie

def index(request):
	return render(request, "index.html", {})