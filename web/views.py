# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############

from app_core import core_interface as core
from libs.logger import app_logger as log

def store_url(
        url,
        url_title,
        url_desc,
        url_imagefile,
):
    # TODO
    # Some checks on the url
    # Some data about the url

    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('New URL INSERT')

    return core.store_url_interface(
        url=url,
        url_title=url_title,
        url_desc=url_desc,
        url_imagefile=url_imagefile,
    )
