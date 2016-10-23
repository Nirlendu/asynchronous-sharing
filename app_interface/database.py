# -*- coding: utf-8 -*-

import inspect
import sys, os

from libs.logger import app_logger as log

from models import ExpressionSecondary

def new_expression(
        expression_primary_id,
        expression_content,
        expression_content_url,
        expression_imagefile,
        broadcast_parent_id,
        total_upvotes,
        total_broadcasts,
        total_discussions,
        total_collects,
        expression_upvote_list,
        expression_broadcast_list,
        expression_discussion_list,
        expression_collection_list,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New expression secondary creating')

    #try:
    expression_secondary = ExpressionSecondary.objects.create(
                                expression_primary_id=expression_primary_id,
                                expression_content=expression_content,
                                expression_content_url=expression_content_url,
                                expression_imagefile=expression_imagefile,
                                broadcast_parent_id=broadcast_parent_id,
                                total_upvotes=total_upvotes,
                                total_broadcasts=total_broadcasts,
                                total_discussions=total_discussions,
                                total_collects=total_collects,
                                expression_upvote_list=expression_upvote_list,
                                expression_broadcast_list=expression_broadcast_list,
                                expression_discussion_list=expression_discussion_list,
                                expression_collection_list=expression_collection_list,
                            )
    return expression_secondary.expression_secondary_id
    # except:
    #     log.info('New expression secondary creating FAILED')
    #     raise Exception

    return None