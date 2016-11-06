# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############

import re, sys, inspect

from app_core import core_interface as core
from libs.logger import app_logger as log


def get_url(text):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    try:
        return urls[0]
    except:
        return None


def new_expression(
        expression_owner_id,
        expression_text,
        expression_imagefile,
        channels,
    ):
    """New Expression Primary views

    :param expression_owner_id:
    :param expression_text:
    :param expression_imagefile:
    :param channels:
    :return:
    """
    log.info('New Expression expression views')

    url = get_url(expression_text)
    if url:
        expression_content = expression_text.replace(url, '')
        url_id = core.find_url_id(url)
    else:
        expression_content = expression_text
        url_id = None
    core.new_expression(
                expression_owner_id=expression_owner_id,
                expression_content=expression_content,
                expression_content_url=url_id,
                expression_imagefile=expression_imagefile,
                channels=channels,
            )
    return
