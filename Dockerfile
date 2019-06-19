FROM nikolaik/python-nodejs:python3.6-nodejs12


# RUN apk update && \
#     apk add nodejs nodejs-npm && \
#     apk add postgresql-libs && \
#     apk add --virtual .build-deps gcc musl-dev postgresql-dev

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
# RUN python -m pip install -r requirements.txt --no-cache-dir && \
#     apk --purge del .build-deps
RUN python -m pip install -r requirements.txt

COPY package.json /app/
RUN npm install

ADD . /app/
# RUN npm run build:prod

COPY entrypoint.sh /entrypoint.sh

EXPOSE 8000