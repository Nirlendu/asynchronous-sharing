# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############

from __future__ import unicode_literals
import sys
import inspect

from django.db import models
from libs.logger import app_logger as log


class UrlManager(models.Manager):
    def store_url(
            self,
            url,
            url_title,
            url_desc=None,
            url_imagefile=None,
            url_weight=0,
    ):
        log.debug('URL create operation')
        url = Url.objects.create(
                url=url,
                url_title=url_title,
                url_desc=url_desc,
                url_imagefile=url_imagefile,
                url_weight=url_weight,
            )
        return url.pk


class Url(models.Model):
    url = models.CharField(
        max_length=150,
        unique=True,
    )
    url_title = models.CharField(
        max_length=150,
        null=False,
    )
    url_desc = models.CharField(
        max_length=200,
        default=None,
        null=True,
    )
    url_imagefile = models.CharField(
        max_length=100,
        default=None,
        null=True,
    )
    url_weight = models.DecimalField (
        default=0,
        max_digits=15,
        decimal_places=10
    )
    url_updated = models.DateTimeField(
        auto_now_add=True,
    )
    url_created = models.DateTimeField(
        auto_now_add=True,
    )
    objects = UrlManager()