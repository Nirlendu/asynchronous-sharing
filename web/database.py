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

from web.models import Url
from libs.logger import app_logger as log


def find_url_id(
        url,
):
    """Find URL ID Primary database

    :param url:
    :return:
    """

    try:
        log.debug('Finding URL')
        url = Url.objects.get(url=url)
        return url.pk

    except Exception:
        log.debug('no URL found')

    return None


def store_url(
        url,
        url_title,
        url_desc,
        url_imagefile,
        url_weight,
):
    """New URL Primary insert database

    :param url:
    :param url_title:
    :param url_desc:
    :param url_imagefile:
    :param url_weight:
    :return:
    """
    log.debug('New URL INSERT CORE')

    return Url.objects.store_url(
        url=url,
        url_title=url_title,
        url_desc=url_desc,
        url_imagefile=url_imagefile,
        url_weight=url_weight,
    )