#!/usr/bin/env python3
#-*- coding: utf-8- -*-

__author__ = "西门吹雪"

'''
async web application 
'''

import logging
import asyncio
import os
import json
import time
from datetime import datetime
from aiohttp import web

logging.basicConfig(level=logging.INFO)

def index(request):
    return web.Response(body=b"<h1>hello world!</h1>", content_type='text/html')

@asyncio.coroutine
async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = await loop.create_server(app.make_handler(), '192.168.8.34', 9000)
    logging.info('server started at http://192.168.8.34:9000...')
    return srv
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

