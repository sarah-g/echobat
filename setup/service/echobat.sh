#!/bin/bash
# echobat start/stop scripts

start() {
  	echo "start echobat python script"
	cd /home/root/code
	python echobat.py
}

stop() {
	killall python
}

case $1 in
  start|stop) "$1" ;;
esac
