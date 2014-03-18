#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import itertools

counter = {}


def gen_sms_id(mobile):
    """ 生成短信ID

    mobile + year + month + day + count = ID
     (11)     (2)    (2)    (2)    (2)   (19)

    示例:
        mobile      | date       | ID1                 | ID2
        ----------- | ---------- | ------------------- | -------------------
        13011112222 | 2014-03-16 | 1301111222214031600 | 1301111222214031601
        13012345678 | 2014-03-18 | 1301234567814031800 | 1301234567814031801

    同一个手机号码，同一天，100个以内的ID都不重复。
    """
    mobile = str(mobile)
    assert mobile.isdigit() and len(mobile) == 11, \
           '`mobile`不是（或不能被转换为）长度为11的字符串'

    if mobile not in counter:
        counter[mobile] = itertools.cycle(xrange(0, 100))

    now = datetime.datetime.now()
    date = now.strftime('%Y%m%d')[2:]

    string = '{}{}{:02d}'.format(mobile, date, counter[mobile].next())
    return long(string)
