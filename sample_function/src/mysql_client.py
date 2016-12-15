# -*- coding: utf-8 -*-
import pymysql
import rds_config
from kms_client import decrypt

# rds settings
rds_host = decrypt(rds_config.db_host)
name = decrypt(rds_config.db_username)
password = decrypt(rds_config.db_password)
db_name = rds_config.db_name


def connect():
    return pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5, charset='utf8')


def fetch(conn, sql, param=None):
    with conn.cursor() as cur:
        num = cur.execute(sql, param)
        return num, cur
