# -*- coding: utf-8 -*-

import inspect
import sys, os

from libs.logger import app_logger as log

from models import ExpressionChannelRelation

def channel_expression_relationship(
    channels,
    expression_id,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Channel Expression Relation creating')

    for channel_id in channels:
        try:
            ExpressionChannelRelation.objects.create_expression_channel_relation(
                channel_id=channel_id,
                expression_id=expression_id,
            )
        except:
            log.debug('Channel Expression Relation FAILED')
            raise Exception
    return