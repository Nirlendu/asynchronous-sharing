# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import inspect
import sys

from libs.logger import app_logger as log

from django.db import models

##
#
# Person Primary Manager
#
##
class PersonPrimaryManager(models.Manager):
    def create_person(
            self,
            user_name,
            person_name,
            total_followers=0,
            person_weight=0,
        ):
        log.info('IN - ' + sys._getframe().f_code.co_name)
        log.info('FROM - ' + sys._getframe(1).f_code.co_name)
        log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

        try:
            log.debug('Person Create operation')
            person = self.create(
                user_name=user_name,
                person_name=person_name,
                total_followers=total_followers,
                person_weight=person_weight,
            )
            return person.id
        except Exception:
            log.exception('Could not Create Person')
        return

    def update_person(
            self,
            person_name,
            total_followers,
            person_weight,
        ):
        log.info('IN - ' + sys._getframe().f_code.co_name)
        log.info('FROM - ' + sys._getframe(1).f_code.co_name)
        log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

        try:
            log.debug('Person Update operation')
            person = self.update(
                user_name=user_name,
                person_name=person_name,
                total_followers=total_followers,
                person_weight=person_weight,
            )
            return person.id
        except Exception:
            log.exception('Could not Update Person')
        return

##
#
# Person Primary
#
##
class PersonPrimary(models.Model):
    user_name = models.CharField(
        max_length=15,
    )
    person_name  = models.CharField(
        max_length=30,
    )
    total_followers = models.IntegerField(
        default=0,
    )
    person_weight = models.DecimalField (
        default=0,
        max_digits=15,
        decimal_places=10
    )
    person_created = models.DateTimeField(
        auto_now_add=True,
    )
    person_updated = models.DateTimeField(
        auto_now_add=True,
    )
    object = PersonPrimaryManager()

##
#
# Person Person Relation Manager
#
##
class PersonPersonRelationManager(models.Manager):
    def create_person_person_relation(
            self,
            person_follower_id,
            person_followee_id
        ):
        log.info('IN - ' + sys._getframe().f_code.co_name)
        log.info('FROM - ' + sys._getframe(1).f_code.co_name)
        log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))

        try:
            log.debug('Person Person Relation create operation')
            person_relation = self.create(
                person_follower_id=person_follower_id,
                person_followee_id=person_followee_id,
            )
            return person_relation.id
        except Exception:
            log.exception('Could not create Person Person Relation')
        return

##
#
# Person Person Relation
#
##
class PersonPersonRelation(models.Model):
    person_follower_id = models.CharField(
        max_length=12,
    )
    person_followee_id = models.CharField(
        max_length=12,
    )

    class Meta:
        unique_together = ('person_follower_id', 'person_followee_id',)

    object = PersonPersonRelationManager()