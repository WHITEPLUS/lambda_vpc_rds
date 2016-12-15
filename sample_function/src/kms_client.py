# -*- coding: utf-8 -*-
import base64
import boto3

kms = boto3.client('kms')


def decrypt(encrypted):
    return kms.decrypt(CiphertextBlob=base64.b64decode(encrypted))['Plaintext']
