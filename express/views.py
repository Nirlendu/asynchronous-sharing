# -*- coding: utf-8 -*-

import os

#from django.db import connection
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.views.decorators.csrf import ensure_csrf_cookie
#from posts.models import Posts
#from posts.forms import Posts

@ensure_csrf_cookie


def update(request):
	if request.method == 'POST':
		try:
			for filename, file in request.FILES.iteritems():
				data = file
		except:
			return render(request, "home.html", {})
		path = default_storage.save('tmp/somename.jpg', ContentFile(data.read()))
		tmp_file = os.path.join(settings.MEDIA_ROOT, path)
		return render(request, "index.html", {})