# -*- coding:utf-8 -*-
"""
db
"""
import logging

import pymysql
from AppTest.tf.com.control import config


def get_info(db_exc, db_database, db_key, db_value, db_time):
    try:
        db = pymysql.connect(host=config.DB_HOST, port=config.DB_PORT, user=config.DB_USER, password=config.DB_PWD,
                             db=config.DB_DATABASE, charset='utf8')
    except Exception as dberr:
        logging.error("connect da error:%s" % dberr)
        return
    cu = db.cursor()
    cu.execute("SELECT %s FROM %s a WHERE a.%s='%s' ORDER BY %s DESC LIMIT 1" % (
        db_exc, db_database, db_key, db_value, db_time))

    result = cu.fetchall()
    try:
        result = list(result[0])
        excresult = " ".join(result)
    except Exception as e:
        logging.error("select errror:%s" % e)
    finally:
        db.close()
        return excresult
