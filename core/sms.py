#!/usr/bin/env python
# -*- coding: utf-8 -*-

from suds.client import Client

from config import URL, SERIAL_NO, KEY, PASSWORD
from errors import get_errors


SRV = Client(URL).service


class SmsException(Exception):
    """ 短信异常类
    """
    pass


def retry(max_times=5):
    """ 重试装饰器

    如果遇到“`method`返回错误，但允许重试的情况”，则进行重试（最多重试`max_times`次）
    """
    def wrapper(method):
        def inner(*args, **kwargs):
            result = method(*args, **kwargs)

            if result != 0:
                err = get_errors(method.__name__, result)
                if err['retry'] and method.ncalls < max_times:
                    method.ncalls += 1
                    inner(*args, **kwargs)
                else:
                    raise SmsException(err['msg'])

        method.ncalls = 0
        return inner

    return wrapper


@retry()
def regist_ex():
    """ 注册序列号
    """
    return SRV.registEx(
        SERIAL_NO,
        KEY,
        PASSWORD
    )


@retry()
def send_sms(mobiles, content, sms_id):
    """ 发送短信
    """
    return SRV.sendSMS(
        SERIAL_NO,
        KEY,
        '',
        mobiles,
        content,
        '',
        'GBK',
        3,
        sms_id
    )


def get_report(callback):
    result = SRV.getReport(SERIAL_NO, KEY)
    if result:
        # (Pdb) p result
        # [(statusReport){
        #    errorCode = "0"
        #    memo = None
        #    mobile = "8613094446757"
        #    receiveDate = "20140313214109"
        #    reportStatus = 0
        #    seqID = 1223334444
        #    serviceCodeAdd = None
        #    submitDate = "20140313214103"
        #  },
        #  (statusReport){
        #    errorCode = "DELIVRD"
        #    memo = None
        #    mobile = "15208316984"
        #    receiveDate = "20140313214108"
        #    reportStatus = 0
        #    seqID = 1223334444
        #    serviceCodeAdd = None
        #    submitDate = "20140313214102"
        #  }]
        # (Pdb) p type(result)
        # <type 'list'>
        # (Pdb) p len(result)
        # 2
        # (Pdb) p type(result[0])
        # <type 'instance'>
        # (Pdb) p result[0].mobile
        # 8613094446757
        callback(result)
    return result


@retry(0)
def logout():
    """ 注销序列号
    """
    return SRV.logout(SERIAL_NO, KEY)


if __name__ == '__main__':
    # 注册
    regist_ex()

    # 发送
    send_sms(
        ['13011112222'],
        u'你好，你的验证码为283203【案例】',
        1223334444
    )

    # 获取状态报告
    def callback(result):
        print result

    import time
    try:
        while True:
            if get_report(callback):
                break
            time.sleep(5)
    finally:
        # 注销
        logout()
