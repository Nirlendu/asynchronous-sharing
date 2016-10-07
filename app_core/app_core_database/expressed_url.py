# -*- coding: utf-8 -*-

import inspect
import sys

from express.models import Link
from libs.logger import app_logger as log


def find_url_id(url):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Find URL CORE')

    urls = Link.objects.filter(link_url=url)
    for url in urls:
        return url.pk;
    else:
        return None


def store_url(
        url,
        url_header,
        url_desc,
        url_imagefile,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New URL INSERT CORE')

    return Link.objects.store_link(
        link_url=url,
        link_name=url_header,
        link_desc=url_desc,
        link_image=url_imagefile,
    )
