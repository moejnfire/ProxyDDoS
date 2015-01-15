#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading
import random
class Proxy(object):
    def __init__(self, ip, port, valid_time = time.time()):
        self.ip = ip
        self.port = port
        self.valid_time = valid_time

    def __eq__(self, other):
        if self.ip == other.ip and self.port == other.port:
            return True
        return False

class ProxyPool():

    instance = None

    def __init__(self):
        self.lst_proxy = []
        self.max_valid_time = 30 * 60
        self.lock = threading.Lock()

    @staticmethod
    def get_instance():
        if ProxyPool.instance is None:
            ProxyPool.instance = ProxyPool()
        return ProxyPool.instance

    def add(self, proxy):
        self.lock.acquire()
        if time.time() - proxy.valid_time > self.max_valid_time or proxy in self.lst_proxy:
            self.lock.release()
            return False
        self.lst_proxy.append(proxy)
        self.lock.release()
        return True

    def put(self, proxy):
        self.add(proxy)

    def pop(self):
        self.lock.acquire()
        if len(self.lst_proxy) == 0:
            self.lock.release()
            return None
        p = random.choice(self.lst_proxy)
        self.lst_proxy.remove(p)
        self.lock.release()
        return p

    def count(self):
        return len(self.lst_proxy)


def test():
    pool = ProxyPool.get_instance()
    print pool.add(Proxy('127.0.0.1', 80))
    print pool.add(Proxy('127.0.0.1', 80))
    pool.max_valid_time = 0
    print pool.add(Proxy('233.233.233.233', 80, time.time() - 1))
    print pool.add(Proxy('233.233.233.233', 80, time.time() + 1))