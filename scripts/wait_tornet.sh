#!/bin/bash
set -e

function check_port() {
	local host=${1} && shift
	local port=${1} && shift
	local retries=10
	local wait=10

	until( $(nc -zv ${host} ${port}) ); do
	    local remaining=$((retries * wait))
		((retries--))
		if [ $retries -lt 0 ]; then
			echo "Service ${host} didn't become ready in time."
			exit 1
		fi
		echo "waiting for ${host}:${port} - remaining ${remaining} "
		sleep "${wait}"
	done
}

check_port "tornet" "9050"
