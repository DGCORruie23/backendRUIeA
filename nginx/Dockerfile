FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d
COPY ruie.key /etc/nginx/ruie.key
COPY ruie.inami.gob.mx.cer /etc/nginx/ruie.cer