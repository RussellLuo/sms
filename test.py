#!/usr/bin/env python
# -*- coding: utf-8 -*-

from redis import Redis
from rq import Queue

from sms_singleton import SmsSingleton
from core.sms_id import gen_sms_id
from task import task


q = Queue(connection=Redis())
result = q.enqueue_call(func=task, timeout=24*60*60)


if __name__ == '__main__':
	import sys
	try:
		mobile = sys.argv[1]
	except IndexError:
		mobile = '13011112222'

	sms = SmsSingleton()
	sms.send_sms([mobile], u'你好，你的验证码为283203【测试】', gen_sms_id(mobile))
