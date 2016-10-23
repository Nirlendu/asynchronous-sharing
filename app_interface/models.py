# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model as ModelCassandra


class ChannelSecondary(ModelCassandra):
    channel_secondary_id = columns.Text(primary_key=True, default=str(uuid.uuid4()).replace('-','')[:8])
    channel_primary_id  = columns.Text()
    channel_weight = columns.Decimal()
    channel_expression_list = columns.List(value_type=columns.Text())

class PersonSecondary(ModelCassandra):
    person_secondary_id = columns.Text(primary_key=True, default=str(uuid.uuid4()).replace('-','')[:12])
    person_primary_id  = columns.Text()
    person_weight = columns.Decimal()
    person_channel_followee_list = columns.List(value_type=columns.Text())
    person_person_followee_list = columns.List(value_type=columns.Text())
    person_expression_list = columns.List(value_type=columns.Text())

class ExpressionSecondary(ModelCassandra):
    expression_secondary_id = columns.Text(primary_key=True, default=str(uuid.uuid4()).replace('-','')[:16])
    expression_primary_id = columns.Text()
    expression_weight = columns.Decimal(default=0)
    expression_content = columns.Text()
    expression_content_url = columns.Text(default=None)
    expression_imagefile = columns.Text(default=None)
    broadcast_parent_id = columns.Text(default=None)
    total_upvotes = columns.Integer()
    total_broadcasts = columns.Integer()
    total_discussions = columns.Integer()
    total_collects = columns.Integer()
    expression_upvote_list = columns.List(value_type=columns.Text())
    expression_broadcast_list = columns.List(value_type=columns.Text())
    expression_discussion_list = columns.List(value_type=columns.Text())
    expression_collection_list = columns.List(value_type=columns.Text())