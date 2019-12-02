FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /core
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libc-dev \
		linux-headers
WORKDIR /core
COPY Pipfile Pipfile.lock /core/
RUN pip3 install --no-cache-dir -U pip pipenv \
    && pipenv install --dev --system --deploy --ignore-pipfile

COPY . /core/
