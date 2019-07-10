FROM node:10.16-alpine

LABEL authors="Roman Dodin <dodin.roman@gmail.com>"

WORKDIR /app

RUN apk update && \
    apk add --update alpine-sdk python && \
    npm install -g @angular/cli@8.1.0 && \
    apk del alpine-sdk python && \
    rm -rf /tmp/* /var/cache/apk/* *.tar.gz ~/.npm && \
    npm cache clean --force