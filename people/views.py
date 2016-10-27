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

    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New Person INSERT')

    return core.new_person(
        user_name= user_name,
        person_name=person_name,
    )