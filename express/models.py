#-*- coding: utf-8 -*-

from __future__ import unicode_literals
import datetime
from django.db import models
from app_base.models import Person, Topic
#from feed.models import Topic
from libs.logger import app_logger as log
from neomodel import (StructuredNode, StringProperty, IntegerProperty,
	RelationshipTo, RelationshipFrom)

# Create your models here.

# class Expression(StructuredNode):
# 	expression_id = StringProperty(unique_index=True)
# 	expression_content = StringProperty()
# 	expression_image = StringProperty(default='')
# 	expression_link = StringProperty(default='')
# 	expression_owner = RelationshipFrom(Person, 'EXPRESSED')
# 	broadcast_owner = RelationshipFrom(Person, 'BROADCASTED')
# 	upvoter = RelationshipFrom(Person, 'UPVOTED')
# 	downvoter = RelationshipFrom(Person, 'DOWNVOTED')
# 	in_topic = RelationshipTo(Topic, 'IN_TOPIC')


class ExpressionGraph(StructuredNode):
	expression_id = IntegerProperty(unique_index=True)
	expression_owner = RelationshipFrom(Person, 'EXPRESSED')
	broadcast_of = RelationshipTo('ExpressionGraph', 'BROADCAST_OF')
	upvoter = RelationshipFrom(Person, 'UPVOTED')
	downvoter = RelationshipFrom(Person, 'DOWNVOTED')
	in_topic = RelationshipTo(Topic, 'IN_TOPIC')


class ExpressionManager(models.Manager):
	def store_expression(
		self, 
		expression_owner_id, 
		expression_content, 
		expression_link_id=None, 
		expression_imagefile=None,
		broadcast_parent_id=None,
		total_upvotes=0,
		total_downvotes=0,
		total_broadcasts=0,
		):
		try:
			log.debug('Expression create operation')
			expression = self.create(
							expression_owner_id = expression_owner_id,
							expression_content = expression_content,
							expression_link_id = expression_link_id,
							expression_imagefile = expression_imagefile,
							broadcast_parent_id = broadcast_parent_id,
							total_upvotes = total_upvotes,
							total_downvotes = total_downvotes,
							total_broadcasts = total_broadcasts
							)
			return expression.id
		except Exception:
			log.exception('Could not create Expression')
			expression = None
		return




class Expression(models.Model):
	expression_owner_id = models.CharField(
		max_length = 30,
		)
	expression_content = models.CharField(
		max_length = 10000,
		)
	expression_link_id = models.CharField(
		max_length = 30,
		default = None,
		null = True,
		)
	expression_imagefile = models.CharField(
		max_length = 30,
		default = None,
		null = True,
		)
	broadcast_parent_id = models.CharField(
		max_length = 30,
		default = None,
		null = True,
		)
	total_upvotes = models.IntegerField(
		default = 0,
		)
	total_downvotes = models.IntegerField(
		default = 0,
		)
	total_broadcasts = models.IntegerField(
		default = 0,
		)
	expression_updated = models.DateTimeField ( 
		auto_now_add = True,
		)
	expression_created =  models.DateTimeField ( 
		auto_now_add = True,
		)
	objects = ExpressionManager()




class LinkManager(models.Manager):
	def store_link(
		self, 
		link_url, 
		link_name, 
		link_desc=None, 
		link_image=None
		):
		log.log('Link create operation')
		try:
			existing_link = Link.objects.filter(link_url=link_url)
			if(
				existing_link and
				(
				existing_link.link_url != link_url or
				existing_link.link_name != link_name or
				existing_link.link_desc != link_desc or
				existing_link.link_image != link_image
				)):
				logger.debug('Link present')
				link = existing_link.update(
					link_url=link_url, 
					link_name=link_name, 
					link_desc=link_desc, 
					link_image=link_image,
					link_updated=datetime.datetime.now()
					)
			else:
				logger.log('Link absent - creating one')
				link = self.create(
					link_url=link_url, 
					link_name=link_name, 
					link_desc=link_desc, 
					link_image=link_image
					)
		except Exception:
			log.exception('Could not insert Link')
			link = None
		return link




class Link(models.Model):
	link_url = models.CharField(
		max_length=150, 
		unique=True,
		)
	link_name = models.CharField(
		max_length=150, 
		null=False,
		)
	link_desc = models.CharField(
		max_length=200, 
		default=None,
		null = True,
		)
	link_image = models.CharField(
		max_length=30, 
		default=None,
		null = True,
		)
	link_updated = models.DateTimeField ( 
		auto_now_add = True,
		)
	link_created = models.DateTimeField ( 
		auto_now_add = True,
		)
	objects = LinkManager()


