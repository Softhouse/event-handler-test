FROM python:2-onbuild

WORKDIR /usr/src/app

EXPOSE 80:80

CMD [ "python", "./events.py" ]
