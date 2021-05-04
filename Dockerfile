FROM python:3.9.1-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /core
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libc-dev \
		linux-headers
WORKDIR /core
COPY . /core/
RUN pip install --upgrade pip && pip install -r ./requirements/local.txt

ENTRYPOINT ["/core/entrypoint.sh"]
