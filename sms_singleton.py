#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core import sms


class SmsSingleton(object):
    """ 短信单例类

    对sms模块的薄封装，主要为了解决Python模块没有合适的init/del机制的问题
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SmsSingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        sms.regist_ex()

    def __del__(self):
        sms.logout()

    def send_sms(self, mobiles, content, sms_id):
        return sms.send_sms(mobiles, content, sms_id)

    def get_report(self, callback):
        return sms.get_report(callback)
