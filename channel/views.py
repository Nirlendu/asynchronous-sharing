# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############

import sys, inspect

from app_core import core_interface as core
from libs.logger import app_logger as log

def new_channel(
            channel_name,
            channel_unique_name,
        ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New Channel')

    return core.new_channel(
        channel_name=channel_name,
        channel_unique_name=channel_unique_name,
    )

def channel_person_relation(
            channel_id,
            person_id,
        ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New Channel Person Relation')

    return core.channel_person_relation(
        channel_id=channel_id,
        person_id=person_id,
    )