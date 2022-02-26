#!/bin/sh

docker build -t whr-wc-image:prd -f Dockerfile .
if [ `echo $?` == 0 ]; then
	docker rm -f whr-wc
	docker run -dt --restart=always -p 8004:8004 --name whr-wc whr-wc-image:prd
fi