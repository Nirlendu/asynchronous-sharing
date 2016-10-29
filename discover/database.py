# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############

import inspect
import sys, re

from django.db import connection

from libs.logger import app_logger as log

from app_interface.models import ExpressionSecondary, UrlSecondary, PersonSecondary, ChannelSecondary
from app_interface import database as interface

def get_discover_items(
    discover_bucket,
):
    log.info('IN - ' + sys._getframe().f_code.co_name)
    log.info('FROM - ' + sys._getframe(1).f_code.co_name)
    log.info('HAS - ' + str(inspect.getargvalues(sys._getframe())))
    log.debug('Get Discovery Logic')

    discover_items = []
    if not discover_bucket:

        discover_items_id = ''
        url_ids = []
        urls=UrlSecondary.objects.all()

        for each_url in urls:
            url_ids.append(each_url.url_primary_id)

        for url_id in url_ids:
            discover_items_id += 'DW' + url_id + '-'

        bufferx = discover_items_id.count('DW')%3

        for i in xrange(0,3-bufferx):
            discover_items_id += 'DW' + url_ids[0] + '-'

        discover_items.append(discover_items_id)

        # SECOND ELEMENT
        discover_items_id = ''
        expression_ids = []
        expression_id_list = ExpressionSecondary.objects.all()

        for each_e in expression_id_list:
            if each_e.expression_content_url == 'None':
                continue
            expression_ids.append(each_e.expression_primary_id)


        for expression_id in expression_ids:
            discover_items_id += 'DE' + expression_id + '-'

        if len(expression_ids)% 2:
            discover_items_id += 'DE' + expression_ids[1] + '-'

        discover_items.append(discover_items_id)

        # THIRD ELEMENT
        discover_items_id = ''
        person_secondary=[]
        channel_secondary = []
        persons = PersonSecondary.objects.all()
        for person in persons:
            person_secondary.append(person.person_primary_id)

        channels = ChannelSecondary.objects.all()
        for channel in channels:
            channel_secondary.append(channel.channel_primary_id)

        for i in xrange(0,1):
            discover_items_id += 'DAE' + expression_ids[0] + '-'
            discover_items_id += 'DAP' + person_secondary[0] + '-'
            discover_items_id += 'DAC' + channel_secondary[0] + '-'

        discover_items.append(discover_items_id)

    return discover_items


def get_discovery_json(ids):
    discover_items={}

    if ids.find('DW') != -1:
        id_list = ids.split('-')
        id_list.remove('')
        discover_items['DW'] = []

        for each_id in id_list:
            json_discovery = {}

            url_contents = UrlSecondary.objects.get(url_primary_id=each_id[2:])

            json_discovery['URL'] = url_contents.url
            json_discovery['URL_TITLE'] = url_contents.url_title
            json_discovery['URL_IMAGEFILE'] = url_contents.url_imagefile
            json_discovery['URL_DOMAIN'] = re.findall(
                '^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)',
                url_contents.url,
            )[0]

            discover_items['DW'].append(json_discovery)

        return discover_items

    if ids.find('DE') != -1:
        id_list = ids.split('-')
        id_list.remove('')
        discover_items['DE'] = []

        for each_id in id_list:
            json_discovery = {}
            expression_object = ExpressionSecondary.objects.get(expression_primary_id=each_id[2:])

            json_discovery['EXPRESSION_ID'] = expression_object.expression_primary_id
            json_discovery['EXPRESSION_OWNER'] = interface.get_expression_owner_name(
                person_id=expression_object.expression_owner_id,
            )
            json_discovery['EXPRESSION_CONTENT'] = expression_object.expression_content
            json_discovery['EXPRESSION_IMAGE'] = expression_object.expression_imagefile
            json_discovery['CHANNEL'] = interface.get_expression_channel_name(
                channel_list=expression_object.expression_channel,
            )
            json_discovery['TIME'] = expression_object.expression_time
            json_discovery['TOTAL_UPVOTES'] = expression_object.total_upvotes
            json_discovery['TOTAL_BROADCASTS'] = expression_object.total_broadcasts
            json_discovery['TOTAL_DISCUSSIONS'] = expression_object.total_discussions
            json_discovery['TOTAL_COLLECTS'] = expression_object.total_collects

            if expression_object.expression_content_url != 'None':
                url_contents = interface.get_url_objects(
                    url_primary_id=str(expression_object.expression_content_url),
                )
                json_discovery['URL'] = url_contents.url
                json_discovery['URL_TITLE'] = url_contents.url_title
                json_discovery['URL_IMAGEFILE'] = url_contents.url_imagefile
                json_discovery['URL_DOMAIN'] = re.findall(
                    '^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)',
                    url_contents.url,
                )[0]

            discover_items['DE'].append(json_discovery)

        return discover_items

    if ids.find('DA') != -1:
        id_list = ids.split('-')
        id_list.remove('')
        discover_items['DA'] = []

        for each_id in id_list:
            json_discovery = {}

            if each_id.find('DAE') != -1:

                expression_object = ExpressionSecondary.objects.get(expression_primary_id=each_id[3:])

                json_discovery['EXPRESSION_ID'] = expression_object.expression_primary_id
                json_discovery['EXPRESSION_OWNER'] = interface.get_expression_owner_name(
                    person_id=expression_object.expression_owner_id,
                )
                json_discovery['EXPRESSION_CONTENT'] = expression_object.expression_content
                json_discovery['EXPRESSION_IMAGE'] = expression_object.expression_imagefile
                json_discovery['CHANNEL'] = interface.get_expression_channel_name(
                    channel_list=expression_object.expression_channel,
                )
                json_discovery['TIME'] = expression_object.expression_time
                json_discovery['TOTAL_UPVOTES'] = expression_object.total_upvotes
                json_discovery['TOTAL_BROADCASTS'] = expression_object.total_broadcasts
                json_discovery['TOTAL_DISCUSSIONS'] = expression_object.total_discussions
                json_discovery['TOTAL_COLLECTS'] = expression_object.total_collects

                if expression_object.expression_content_url != 'None':
                    url_contents = interface.get_url_objects(
                        url_primary_id=str(expression_object.expression_content_url),
                    )
                    json_discovery['URL'] = url_contents.url
                    json_discovery['URL_TITLE'] = url_contents.url_title
                    json_discovery['URL_IMAGEFILE'] = url_contents.url_imagefile
                    json_discovery['URL_DOMAIN'] = re.findall(
                        '^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)',
                        url_contents.url,
                    )[0]

            if each_id.find('DAP') != -1:
                person_object = PersonSecondary.objects.get(person_primary_id=each_id[3:])
                json_discovery['PERSON_NAME'] = person_object.person_name

            if each_id.find('DAC') != -1:
                channel_object = ChannelSecondary.objects.get(channel_primary_id=each_id[3:])
                json_discovery['CHANNEL_NAME'] = channel_object.channel_name

            discover_items['DA'].append(json_discovery)

        return discover_items

    return discover_items