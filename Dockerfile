FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /core
WORKDIR /core
COPY Pipfile Pipfile.lock /core/
RUN pip3 install --no-cache-dir -U pip pipenv \
    && pipenv install --dev --system --deploy --ignore-pipfile

COPY . /core/
