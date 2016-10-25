# -*- coding: utf-8 -*-

import inspect
import sys, os

from models import PersonPrimary

from libs.logger import app_logger as log

def new_person(
        user_name,
        person_name,
        total_followers,
        person_weight,
    ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.info('New person primary DB')

    return PersonPrimary.object.create_person(
        user_name=user_name,
        person_name=person_name,
        total_followers=total_followers,
        person_weight=person_weight,
    )