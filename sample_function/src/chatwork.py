# -*- coding: utf-8 -*-
import urllib
import logging
from urllib2 import Request, urlopen, URLError, HTTPError
from chatwork_config import BASE_URL, DEFAULT_TOKEN
from kms_client import decrypt

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def post(room_id, message):
    logger.info("Message: " + str(message))

    url = BASE_URL.format(room_id)
    token = decrypt(DEFAULT_TOKEN)
    headers = {
        'X-ChatWorkToken': token
    }
    payload = {
        'body': message
    }

    req = Request(url, urllib.urlencode(payload), headers)
    try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", payload['body'])
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)
