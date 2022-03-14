FROM python:3.7

WORKDIR /workspace

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt