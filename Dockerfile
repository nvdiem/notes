https://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx_1.31.9-1~trixie_amd64.deb
https://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx_1.31.9-1~noble_amd64.deb

FROM php:8.5-fpm

COPY nginx_*.deb /tmp/

RUN apt-get update \
 && apt-get install -y --no-install-recommends /tmp/nginx_*.deb \
 && rm -rf /var/lib/apt/lists/* /tmp/*.deb

CMD ["sh", "-c", "php-fpm -D && nginx -g 'daemon off;'"]
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

COPY nginx_1.31.9-1~noble_amd64.deb /tmp/

RUN apt-get update \
 && apt-get install -y --no-install-recommends /tmp/nginx_1.31.9-1~noble_amd64.deb \
 && rm -rf /var/lib/apt/lists/* /tmp/*.deb

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
