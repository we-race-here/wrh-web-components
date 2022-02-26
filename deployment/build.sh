#!/bin/sh

docker build -t wrh-wc-image:prd -f Dockerfile .
if [ `echo $?` == 0 ]; then
	docker rm -f wrh-wc
	docker run -dt --restart=always -p 8004:8004 --name wrh-wc wrh-wc-image:prd
fi