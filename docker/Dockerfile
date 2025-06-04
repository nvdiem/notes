# --- Dockerfile (Laravel 11 ready) ---
FROM php:8.3-fpm-alpine

# 1. Công cụ & libs hệ thống cần cho build extension
RUN apk add --no-cache \
        bash git curl unzip libzip-dev oniguruma-dev \
        icu-dev zlib-dev libpng-dev libjpeg-turbo-dev libwebp-dev freetype-dev \
        libxml2-dev openssl-dev

# 2. Cài/biên dịch extension bắt buộc & khuyến nghị cho Laravel
RUN docker-php-ext-configure gd \
        --with-freetype --with-jpeg --with-webp \
    && docker-php-ext-install -j$(nproc) \
        intl mbstring bcmath pcntl zip xml gd pdo_mysql opcache

# 3. (Tuỳ chọn) Cài redis nếu cần
# RUN pecl install redis && docker-php-ext-enable redis

# 4. Chỉnh FPM lắng nghe TCP 9000
RUN sed -i 's|^listen = .*|listen = 0.0.0.0:9000|' /usr/local/etc/php-fpm.d/www.conf \
    && echo "clear_env = no" >> /usr/local/etc/php-fpm.d/www.conf

# 5. Thêm composer (multi-stage nhỏ gọn)
COPY --from=composer:2.7 /usr/bin/composer /usr/local/bin/composer

# 6. Sao chép code ứng dụng
WORKDIR /var/www/html


EXPOSE 9000
CMD ["php-fpm", "-F"]
