FROM python:3.11.0-bullseye

LABEL  maintainer="ehlui"

WORKDIR /usr/src/app

COPY ./src/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/flaskr ./

CMD [ "flask","run","--host=0.0.0.0" ]
