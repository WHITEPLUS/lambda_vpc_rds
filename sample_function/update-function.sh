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

aws lambda update-function-code \
    --function-name ${FUNCTION_NAME} \
    --zip-file fileb://upload.zip

cd .. && rm -rf bundle
