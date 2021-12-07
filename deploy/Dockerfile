FROM python:3-alpine
LABEL maintaner='1287641566@qq.com'
LABEL description='my dajngo app'

WORKDIR /usr/src/app
COPY ./ocean_land ./ocean_land
COPY ./gunicorn_configs ./configs/
WORKDIR
ENV Term dump
RUN apk add --update supervisor nginx && \
rm -rf /var/cache/apk/* && \
mkdir /tmp/ && \
mkdir -p /var/www/html && \
#将/var/www/html目录的拥有者设置为nginx，群体的使用者设置为nginx
chown -R nginx:nginx /var/www/html

COPY ../front_code /var/www/html
COPY configs/default.conf /ect/nginx/conf.d
COPY configs/nginx.conf /etc/nginx/nginx.conf
COPY configs/supervisord.conf /etc/supervisord.conf

VOLUME /var/log/nginx
EXPOSE 80 8000 443
CMD['supervisord']



