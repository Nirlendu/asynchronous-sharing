# -*- coding: utf-8 -*-

# from __future__ import unicode_literals

# from neomodel import (StructuredNode, StringProperty, IntegerProperty,
#                       RelationshipTo, RelationshipFrom)


# class Person(StructuredNode):
#     person_id = StringProperty(unique_index=True, required=True)
#     person_name = StringProperty(required=True)
#     person_age = IntegerProperty()
#     person_gender = StringProperty()
#     person_follow = RelationshipFrom('Person', 'FOLLOWS')


# class Topic(StructuredNode):
#     # name = StringProperty(unique_index=True)
#     # age = IntegerProperty(index=True, default=0)
#     name = StringProperty()
#     followed_topic = RelationshipFrom(Person, 'FOLLOWS')
#     child_topic = RelationshipTo('Topic', 'CHILD_TOPIC')
#     related_topic = RelationshipTo('Topic', 'RELATED')
#     related_posts = RelationshipFrom('Expression', 'IN_TOPIC')


# class RootTopic(StructuredNode):
#     # code = StringProperty(unique_index=True, required=True)
#     Root = StringProperty()
#     follow = RelationshipTo(Topic, 'CHILD_TOPIC')

#
# import uuid
# from cassandra.cqlengine import columns
# from cassandra.cqlengine.models import Model
#
# class ExampleModel(Model):
#     example_id    = columns.UUID(primary_key=True, default=uuid.uuid4)
#     example_type  = columns.Integer(index=True)
#     created_at    = columns.DateTime()
#     description   = columns.Text(required=False)