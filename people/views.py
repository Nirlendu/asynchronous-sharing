# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############

import inspect
import sys
from app_core import core_interface as core
from libs.logger import app_logger as log

def new_person(
        user_name,
        person_name,
    ):
    """New Person Primary views

    :param user_name:
    :param person_name:
    :return:
    """
    log.debug('New Person INSERT')

    return core.new_person(
        user_name= user_name,
        person_name=person_name,
    )