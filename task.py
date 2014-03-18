#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from sms_singleton import SmsSingleton

sms = SmsSingleton()
logger = logging.getLogger(__name__)


def task():
	def callback(result):
		""" 将result记入日志
		"""
		logger.info(str(result))

	import time
	while True:
		sms.get_report(callback)
		time.sleep(10)
