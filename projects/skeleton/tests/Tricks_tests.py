# -*- coding: utf-8 -*-
# @Author: Zymous
# @Date:   2017-04-28 17:10:46
# @Last Modified by:   Zymous
# @Last Modified time: 2017-04-28 17:16:37

from nose.tools import *
import Tricks

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"