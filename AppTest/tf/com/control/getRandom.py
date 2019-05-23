# -*- coding:utf-8 -*-
"""
"""
import random

def ranstr(num):

    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    salt = ''
    for i in range(num):
        salt += random.choice(H)

    return salt

'''
salt = ranstr(9)
print(salt)
'''

