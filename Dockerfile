FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /core
WORKDIR /core
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install

COPY . /core/
