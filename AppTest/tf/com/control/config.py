# -*- coding:utf-8 -*-

from AppTest.tf.com.control import test_getRandom

"""
登录用户
"""
LOG_MAIL = "xiangyb1@tigerft.com"
LOG_PWD = "qweqwe123"

'''
注册用
'''
a = test_getRandom.ranstr(9)
REG_MAIL = a + "@tf.com"
REG_PWD = "qweqwe123"
REG_NAME = a

'''
DB
'''
DB_HOST = "192.168.9.168"
DB_USER = "reader"
DB_PWD = "reader"
DB_DATABASE = ""
DB_TABLE = ""
DB_PORT = 3306

