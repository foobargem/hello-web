FROM python:3.9.7-alpine3.13

RUN mkdir -p /app
COPY helloweb /app

RUN apk update && \
    apk add bind-tools && \
    pip install django

EXPOSE 80
STOPSIGNAL SIGQUIT

WORKDIR /app

CMD ["/usr/local/bin/python", "manage.py", "runserver", "0.0.0.0:80"]
