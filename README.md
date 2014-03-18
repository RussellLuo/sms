sms
===

emay-SMS demo for consuming WSDL (SOAP) Web Services in Python.

Dependencies
------------

1. [suds][]

    sudo pip install suds

2. [rq][]

    sudo pip install rq

Run
---

1. start redis

    $ ./redis-server

2. start a rq worker

    $ rqworker

3. run test.py

    $ python test.py


[suds]: https://fedorahosted.org/suds/
[rq]: http://python-rq.org/
