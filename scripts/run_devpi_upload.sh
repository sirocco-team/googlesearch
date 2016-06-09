#!/usr/bin/env bash

me=`basename "$0"`
echo "SCRIPT: $me"
hostname
cat /etc/hosts

devpi use --set-cfg http://dp.topia.com:3141/russ/dev

devpi login russ --password='dpdp'

echo "PACKAGES BEFORE"
devpi list --all -v --debug
echo "PACKAGES BEFORE END"

devpi upload

echo "PACKAGES AFTER"
devpi list --all -v --debug
echo "PACKAGES AFTER END"
