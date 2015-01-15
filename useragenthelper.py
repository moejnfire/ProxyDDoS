#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def get(client = ''):
    return 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)' \
           ' Chrome/%s.0.%s.%s Safari/537.36' % (random.randint(28, 39), random.randint(100, 2800), random.randint(0, 100))

def test():
    print get()
