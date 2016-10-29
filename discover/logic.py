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

from libs.logger import app_logger as log

import database as discover

def get_discovery(
        person_id,
    ):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Get Discovery Logic')

    # Do some calculation about which list is to be taken
    if person_id:
        discover_bucket=None

    return discover.get_discover_items(
        discover_bucket=discover_bucket,
    )