#!/bin/bash
# edibat start/stop scripts

start() {
  	echo "start edibat python script"
	cd /home/root
	python edibat.py
}

stop() {
	killall python
}

case $1 in
  start|stop) "$1" ;;
esac
