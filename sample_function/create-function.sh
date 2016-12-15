#!/bin/bash

# TODO: update function_name
FUNCTION_NAME=sample_function

cd "$(dirname "$0")"/src
mkdir bundle
cp *.py bundle/
cd bundle

pip freeze > require.txt
[ -s require.txt ] && pip install -r require.txt -t .

zip -r upload.zip .

aws lambda create-function \
    --function-name ${FUNCTION_NAME} \
    --runtime python2.7 \
    --role #lambdaとKMSが使えるIAM ROLEのarn \
    --handler ${FUNCTION_NAME}.lambda_handler \
    --vpc-config SubnetIds=#vpc_subnet,SecurityGroupIds=#RDSに接続可能なsecurity_group \
    --zip-file fileb://upload.zip \
    --timeout 60

cd .. && rm -rf bundle
