# -*- coding:utf-8 -*-
"""
db
"""
import logging

import pymysql
from AppTest.tf.com.control import config


def get_info(db_database, db_key, db_value):
    try:
        db = pymysql.connect(host=config.DB_HOST, port=config.DB_PORT, user=config.DB_USER, password=config.DB_PWD,
                             db=config.DB_DATABASE, charset='utf8')
    except Exception as dberr:
        logging.error("connect da error:%s" % dberr)
        return
    cu = db.cursor()

    cu.execute("SELECT * FROM %s a WHERE a.%s=%s ORDER BY GMT_CREATE DESC LIMIT 1", db_database, db_key, db_value)
    result = cu.fetchall()

    db.close()
    return result


get_info("mns.t_notify_msg", "APP_ID", "SMSG")
print(get_info())
