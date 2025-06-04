FROM bm_server_web:base AS runtime

WORKDIR /var/www/html


# Copy toàn bộ source
COPY . .

# Phân quyền cho Laravel
# RUN chown -R www-data:www-data storage bootstrap/cache

# (tuỳ) cache config/route/view
RUN php artisan config:cache \
 && php artisan route:cache  \
 && php artisan view:cache || true

EXPOSE 9000
CMD ["php-fpm", "-F"]
