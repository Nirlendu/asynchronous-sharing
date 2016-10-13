from django.shortcuts import render


from celery import shared_task
import app_core.core_interface as core
import redis
import ujson
from app_core import core_interface as core

@shared_task
def update_graph_cache():
    print "STARTING REDIS!"
    redis_cache = redis.StrictRedis(host='localhost', port=6379, db=0)
    data = core.get_expressions('asd123')
    redis_cache.hset('asd123', 'asd123', ujson.dumps(data))