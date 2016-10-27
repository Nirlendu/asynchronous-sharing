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


class UrlManager(models.Manager):
    def store_url(
            self,
            url,
            url_title,
            url_desc=None,
            url_imagefile=None,
            url_weight=0,
    ):

        log.info('IN - ' + sys._getframe().f_code.co_name)
        log.info('FROM - ' + sys._getframe(1).f_code.co_name)
        log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

        try:
            log.debug('URL create operation')
            url = Url.objects.create(
                    url=url,
                    url_title=url_title,
                    url_desc=url_desc,
                    url_imagefile=url_imagefile,
                    url_weight=url_weight,
                )
            return url.pk
        except Exception:
            log.exception('Could not insert URL')
        return


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