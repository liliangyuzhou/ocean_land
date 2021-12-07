FROM python:3-alpine
LABEL maintaner='1287641566@qq.com'
LABEL description='my dajngo app'

ARG PROJECT_NAME='ocean_land'
ENV PROJECT_NAME=${PROJECT_NAME}

WORKDIR /usr/src/app/
COPY ./${PROJECT_NAME}/ ./${PROJECT_NAME}/
COPY ./gunicorn_config.py ./configs/
COPY ./docker-entrypoint.sh /docker-entrypoint.sh

WORKDIR ./${PROJECT_NAME}/

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories && \
    apk update && \
    apk add --allow-untrusted build-base mariadb-connector-c-dev && \
    pip install -i https://pypi.douban.com/simple gunicorn && \
    pip install -i https://pypi.douban.com/simple -r requirements.txt && \
    apk update && apk upgrade && \
    rm -rf /var/cache/apk/* && \
    chmod u+x /docker-entrypoint.sh

VOLUME /usr/src/app/logs/
VOLUME /usr/src/app/${PROJECT_NAME}/
EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint.sh"]

