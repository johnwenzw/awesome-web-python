# !/usr/bin/env python 
# -*- coding:utf-8 -*-
import orm, asyncio
from models import User, Blog, Comment

async def demo(loop):
    await orm.create_pool(loop=loop, user='test', password='qwer1234', db='awesome')
    u = User(name="test", email="test@123.com",passwd="test", image="about:blank")
    await u.save()
    #await orm.destory_pool()

loop =asyncio.get_event_loop()
loop.run_until_complete(demo(loop))
loop.close()
