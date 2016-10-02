#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models as models_sql
#from feed.models import Topic

from neomodel import (StructuredNode, StringProperty, IntegerProperty,
	RelationshipTo, RelationshipFrom)

# Create your models here.


class Person(StructuredNode):
	person_id = StringProperty(unique_index=True, required=True)
	person_name = StringProperty(required=True)
	person_age = IntegerProperty()
	person_gender = StringProperty() 
	person_follow = RelationshipFrom('Person', 'FOLLOWS')

class Expression(StructuredNode):
	expression_id = StringProperty(unique_index=True)
	expression_content = StringProperty()
	expression_image = StringProperty(default='')
	expression_link = StringProperty(default='')
	expression_owner = RelationshipFrom(Person, 'EXPRESSED')
	broadcast_owner = RelationshipFrom(Person, 'BROADCASTED')
	upvoter = RelationshipFrom(Person, 'UPVOTED')
	downvoter = RelationshipFrom(Person, 'DOWNVOTED')
	in_topic = RelationshipTo('Topic', 'IN_TOPIC')


class LinkManager(models_sql.Manager):
	def store_link(self, link_url, link_name, link_desc, link_image):
		link = self.create(link_url = link_url, link_name=link_name, link_desc=link_desc, link_image=link_image)
		return link

class Link(models_sql.Model):
	link_url = models_sql.CharField(max_length=100, default='')
	link_name = models_sql.CharField(max_length=100)
	link_desc = models_sql.CharField(max_length=100)
	link_image = models_sql.CharField(max_length=10)
	objects = LinkManager()