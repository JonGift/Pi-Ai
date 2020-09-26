FROM python:3.7

COPY . /Pi-Ai
WORKDIR /Pi-Ai/app

RUN pip3 install --upgrade pip && \
    pip3 install \
    -r requirements.txt
