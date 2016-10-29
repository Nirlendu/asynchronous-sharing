# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############

from __future__ import unicode_literals

import uuid
from datetime import datetime


from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model as ModelCassandra


class ChannelSecondary(ModelCassandra):
    channel_secondary_id = columns.Text(primary_key=True, default=str(uuid.uuid4()).replace('-','')[:8], required=True)
    channel_primary_id  = columns.Text(index=True, required=True)
    channel_name = columns.Text(required=True)
    channel_unique_name = columns.Text(index=True, required=True)
    channel_weight = columns.Decimal(default=0)
    total_followers = columns.Integer(default=0)
    channel_expression_list = columns.List(value_type=columns.Text(),default=[])

class PersonSecondary(ModelCassandra):
    person_secondary_id = columns.Text(primary_key=True, default=str(uuid.uuid4()).replace('-','')[:12], required=True)
    user_name = columns.Text(index=True, required=True)
    person_primary_id  = columns.Text(index=True, required=True)
    person_name = columns.Text(required=True)
    total_followers = columns.Integer(default=0)
    person_weight = columns.Decimal(default=0)
    person_channel_followee_list = columns.List(value_type=columns.Text(),default=[])
    person_person_followee_list = columns.List(value_type=columns.Text(),default=[])
    person_expression_list = columns.List(value_type=columns.Text(),default=[])

class ExpressionSecondary(ModelCassandra):
    expression_secondary_id = columns.Text(primary_key=True, default=str(uuid.uuid4()).replace('-','')[:16], required=True)
    expression_primary_id = columns.Text(index=True, required=True)
    expression_owner_id = columns.Text(required=True)
    expression_weight = columns.Decimal(default=0)
    expression_content = columns.Text(required=True)
    expression_content_url = columns.Text(default=None)
    expression_imagefile = columns.Text(default=None)
    broadcast_parent_id = columns.Text(default=None)
    expression_time = columns.DateTime(default=datetime.now())
    expression_channel = columns.List(value_type=columns.Text(),default=[])
    total_upvotes = columns.Integer(default=0)
    total_broadcasts = columns.Integer(default=0)
    total_discussions = columns.Integer(default=0)
    total_collects = columns.Integer(default=0)
    expression_upvote_list = columns.List(value_type=columns.Text(),default=[])
    expression_broadcast_list = columns.List(value_type=columns.Text(),default=[])
    expression_discussion_list = columns.List(value_type=columns.Text(),default=[])
    expression_collection_list = columns.List(value_type=columns.Text(),default=[])

class UrlSecondary(ModelCassandra):
    url_secondary_id = columns.Text(primary_key=True, default=str(uuid.uuid4()).replace('-','')[:16],required=True)
    url_primary_id = columns.Text(index=True, required=True)
    url = columns.Text(index=True, required=True)
    url_title = columns.Text(required=True)
    url_desc = columns.Text(default=None)
    url_imagefile = columns.Text(default=None)
    url_weight = columns.Decimal(default=0)