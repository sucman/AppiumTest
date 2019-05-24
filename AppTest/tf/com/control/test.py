# -*- coding:utf-8 -*-
import logging

import pymysql
from AppTest.tf.com.control import config


def get_info(db_exc, db_database, db_key, db_value):
    try:
        db = pymysql.connect(host=config.DB_HOST, port=config.DB_PORT, user=config.DB_USER, password=config.DB_PWD,
                             db=config.DB_DATABASE, charset='utf8')
    except Exception as dberr:
        logging.error("connect da error:%s" % dberr)
        return
    cu = db.cursor()
    cu.execute("SELECT %s FROM %s a WHERE a.%s='%s' ORDER BY GMT_CREATE DESC LIMIT 1" % (
        db_exc, db_database, db_key, db_value))

    result = cu.fetchall()
    print(result)

    try:
        result = list(result[0])
        a = " ".join(result)
        print(a)
        b = a[-6:]
        print(b)
    except Exception as e:
        logging.error("select errror:%s" % e)
    finally:
        db.close()
        return b

get_info("CONTENT", "mns.t_notify_msg", "APP_ID", "SMSG")
