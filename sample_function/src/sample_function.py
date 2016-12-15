# -*- coding: utf-8 -*-
import sys
import logging
from mysql_client import connect, fetch

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = connect()
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()


def lambda_handler(event, context):
    num, cur = fetch(conn, 'SELECT NOW()')
    for row in cur:
        logger.info('接続確認 %s' % row[0])

    return "Got %d items from RDS MySQL table" % num
