#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sms_singleton import SmsSingleton
from core.sms_id import gen_sms_id

SMS = SmsSingleton()


if __name__ == '__main__':
	mobile = 13011112222
	SMS.send_sms([mobile], u'你好，你的验证码为283203【测试】', gen_sms_id(mobile))

	def callback(result):
		print result

	import time
	while True:
		if SMS.get_report(callback):
			break
		time.sleep(5)
