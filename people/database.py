# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############

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
    """New Person Primary database

    :param user_name:
    :param person_name:
    :param total_followers:
    :param person_weight:
    :return:
    """
    log.info('New person primary DB')

    return PersonPrimary.object.create_person(
        user_name=user_name,
        person_name=person_name,
        total_followers=total_followers,
        person_weight=person_weight,
    )