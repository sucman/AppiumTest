# -*- coding:utf-8 -*-

from AppTest.tf.com.control import test_getRandom

"""
用户
"""
LOG_MAIL = "xybtest7@tf.com"

a = test_getRandom.ranstr(9)
REG_MAIL = a + "@tf.com"

REG_NAME = a

OLD_PWD = "qweqwe123"
NEW_PWD = "qweqwe1234"

'''
DB
'''
DB_HOST = "192.168.9.168"
DB_USER = "reader"
DB_PWD = "reader"
DB_DATABASE = ""
DB_TABLE = ""
DB_PORT = 3306
