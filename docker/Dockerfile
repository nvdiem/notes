FROM php:8.3-fpm

ENV PHP_FPM_PORT=9002

# 1. Cài đặt gói hệ thống cần thiết (bao gồm cả gnupg để fix lỗi gpg)
RUN apt-get update && apt-get install -y \
    bash \
    git \
    curl \
    unzip \
    zip \
    gnupg \
    libzip-dev \
    libonig-dev \
    libicu-dev \
    libxml2-dev \
    libpng-dev \
    libjpeg-dev \
    libwebp-dev \
    libfreetype6-dev \
    libpq-dev \
    sqlite3 \
    libsqlite3-dev \
    zlib1g-dev \
    libssl-dev \
    pkg-config \
    libcurl4-openssl-dev \
    autoconf \
    make \
    g++ \
    cpio \
    rpm2cpio \
    iproute2 \
    nginx \
    xvfb \
    libxrender1 \
    libx11-xcb1 \
    libxcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libnss3 \
    libxrandr2 \
    libasound2 \
    fonts-liberation \
    libappindicator3-1 \
    lsb-release \
    xdg-utils \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 2. Cài đặt các PHP extensions

# -- Nhóm xử lý ảnh
RUN docker-php-ext-configure gd --with-freetype --with-jpeg --with-webp \
    && docker-php-ext-install -j$(nproc) gd

# -- Nhóm chuỗi, encoding, định dạng
RUN docker-php-ext-install -j$(nproc) mbstring intl bcmath

# -- Nhóm hệ thống
RUN docker-php-ext-install -j$(nproc) pcntl zip xml opcache

# -- Nhóm kết nối CSDL, socket, soap
RUN docker-php-ext-install -j$(nproc) \
    pdo_mysql \
    mysqli \
    calendar \
    exif \
    ftp \
    sockets \
    soap

# 3. Cài Redis PHP extension
RUN pecl install redis && docker-php-ext-enable redis

# 4. Cài Composer (từ multi-stage image)
COPY --from=composer:2.7 /usr/bin/composer /usr/local/bin/composer

# 5. Cấu hình PHP-FPM
RUN sed -i "s|^listen = .*|listen = 0.0.0.0:${PHP_FPM_PORT}|" /usr/local/etc/php-fpm.d/www.conf \
    && echo "clear_env = no" >> /usr/local/etc/php-fpm.d/www.conf

# 6. Cài đặt Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# 7. Cài đặt ChromeDriver tương thích với Chrome
RUN LATEST=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE) \
    && wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && chmod +x /usr/local/bin/chromedriver \
    && rm /tmp/chromedriver.zip

# 8. Thư mục làm việc mặc định
WORKDIR /var/www/html

# 9. Mở cổng PHP-FPM
EXPOSE ${PHP_FPM_PORT}

# 10. Lệnh khởi động
CMD ["php-fpm", "-F"]
