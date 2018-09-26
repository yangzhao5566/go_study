# Description test img

FROM busybox:latest
#MAINTAINER "yz<yangzhao6_6@163.com>"
LABEL maintainer="yz<yangzhao6_6@163.com>"
COPY index.html /data/web/html/
ADD http://nginx.org/download/nginx-1.15.3.tar.gz /usr/local/src/
WORKDIR /usr/local/
ADD nginx-1.15.3.tar.gz ./src
