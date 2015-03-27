FROM python:2-onbuild

WORKDIR /usr/src/app

EXPOSE 8888

CMD [ "python", "./events.py" ]
