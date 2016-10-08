# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Person_Data(models.Model):
    person_id = models.CharField(
        max_length=30,
    )
    discussion_expression_owner_id = models.CharField(
        max_length=30,
    )
    discussion_expression_content = models.CharField(
        max_length=10000,
    )
    discussion_expression_link_id = models.CharField(
        max_length=30,
        default=None,
        null=True,
    )
    discussion_expression_imagefile = models.CharField(
        max_length=30,
        default=None,
        null=True,
    )
    total_upvotes = models.IntegerField(
        default=0,
    )
    total_downvotes = models.IntegerField(
        default=0,
    )
    person_auth_updated = models.DateTimeField(
        auto_now_add=True,
    )
    person_auth_created = models.DateTimeField(
        auto_now_add=True,
    )
    objects = PersonDataManager()
