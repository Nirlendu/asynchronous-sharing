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

from libs.logger import app_logger as log

from models import ExpressionPrimary

def new_expresssion(
        expression_owner_id,
        expression_content,
        expression_content_url,
        expression_imagefile,
        broadcast_parent_id,
        expression_weight,
        total_upvotes,
        total_collects,
        total_broadcasts,
        total_discussions,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New Expression Primary creating')

    # try:
    expression_primary_id = ExpressionPrimary.objects.create_expression(
        expression_owner_id=expression_owner_id,
        expression_content=expression_content,
        expression_content_url=expression_content_url,
        expression_imagefile=expression_imagefile,
        broadcast_parent_id=broadcast_parent_id,
        expression_weight=expression_weight,
        total_upvotes=total_upvotes,
        total_collects=total_collects,
        total_broadcasts=total_broadcasts,
        total_discussions=total_discussions,
    )
    return expression_primary_id
    # except:
    #     log.debug('New Expression Primary creating FAILED')
    #     raise Exception
    #
    # return None