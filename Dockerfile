FROM php:8.5-fpm

COPY nginx_*.deb /tmp/

RUN apt-get update \
 && apt-get install -y --no-install-recommends /tmp/nginx_*.deb \
 && rm -rf /var/lib/apt/lists/* /tmp/*.deb

CMD ["sh", "-c", "php-fpm -D && nginx -g 'daemon off;'"]
