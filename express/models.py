#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models as models_sql
#from feed.models import Topic

from neomodel import (StructuredNode, StringProperty, IntegerProperty,
	RelationshipTo, RelationshipFrom)

# Create your models here.


class Person(StructuredNode):
	#code = StringProperty(unique_index=True, required=True)
	name = StringProperty()
	age = IntegerProperty()
	gender = StringProperty() 
	follow = RelationshipFrom('Person', 'FOLLOWS')

class Posts(StructuredNode):
	# name = StringProperty(unique_index=True)
	# age = IntegerProperty(index=True, default=0)
	post_content = StringProperty()
	post_image = StringProperty()
	post_link = StringProperty()
	post_owner = RelationshipFrom(Person, 'POSTED')
	shared_owner = RelationshipFrom(Person, 'SHARED')
	upvoter = RelationshipFrom(Person, 'UPVOTED')
	downvoter = RelationshipFrom(Person, 'DOWNVOTED')
	in_topic = RelationshipTo('Topic', 'IN_TOPIC')


class LinkManager(models_sql.Manager):
    def store_link(self, link_name, link_desc, link_image):
        link = self.create(link_name=link_name, link_desc=link_desc, link_image=link_image)
        return link

class Link(models_sql.Model):
    link_name = models_sql.CharField(max_length=100)
    link_desc = models_sql.CharField(max_length=100)
    link_image = models_sql.CharField(max_length=10)
    objects = LinkManager()