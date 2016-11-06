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
    """New Expression Primary Database

    :param expression_owner_id:
    :param expression_content:
    :param expression_content_url:
    :param expression_imagefile:
    :param broadcast_parent_id:
    :param expression_weight:
    :param total_upvotes:
    :param total_collects:
    :param total_broadcasts:
    :param total_discussions:
    :return:
    """
    log.debug('New Expression Primary creating')

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