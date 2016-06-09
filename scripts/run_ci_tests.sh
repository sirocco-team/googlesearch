#!/usr/bin/env bash

devpi use --set-cfg http://dp.topia.com:3141/russ/dev

devpi login russ --password='dpdp'

echo "INDEX"
devpi list --all -v --debug
echo "INDEX END"

echo "FREEZE"
pip freeze
echo "FREEZE END"

bash /app/scripts/wait_tornet.sh

py.test

