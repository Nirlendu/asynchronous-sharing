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

from app_core import core_interface as core
from libs.logger import app_logger as log

def store_url(
        url,
        url_title,
        url_desc,
        url_imagefile,
):
    """New URL Primary views

    :param url:
    :param url_title:
    :param url_desc:
    :param url_imagefile:
    :return:
    """
    # TODO
    # Some checks on the url
    # Some data about the url
    log.debug('New URL INSERT')

    return core.store_url_interface(
        url=url,
        url_title=url_title,
        url_desc=url_desc,
        url_imagefile=url_imagefile,
    )
