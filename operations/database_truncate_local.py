# -*- coding: utf-8 -*-

#############
#
# Copyright - Nirlendu Saha
#
# author - nirlendu@gmail.com
#
#############

from django.db import connections

cursor_postgres = connections['default'].cursor()
cursor_cassandra = connections['cassandra'].cursor()

cursor_cassandra.execute("truncate channel_secondary")
cursor_cassandra.execute("truncate person_secondary")
cursor_cassandra.execute("truncate expression_secondary")
cursor_cassandra.execute("truncate url_secondary")

cursor_postgres.execute("truncate channel_channelchannelrelation")
cursor_postgres.execute("truncate channel_channelpersonrelation")
cursor_postgres.execute("truncate channel_channelprimary")
cursor_postgres.execute("truncate channel_expressionchannelrelation")
cursor_postgres.execute("truncate channel_urlchannelrelation")
cursor_postgres.execute("truncate expression_expressionprimary")
cursor_postgres.execute("truncate people_personpersonrelation")
cursor_postgres.execute("truncate people_personprimary")
cursor_postgres.execute("truncate web_url")
