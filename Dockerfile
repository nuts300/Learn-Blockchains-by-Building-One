FROM python:3.6
ENV PYTHONUNBUFFERED 1ADD . /SampleBlockchainAPI/
MAINTAINER David Soichi Nakahashi <sdn0303.guitar@gmail.com>
RUN mkdir /SampleBlockchainAPI
WORKDIR /SampleBlockchainAPI
ADD requirements.txt /SampleBlockchainAPI
RUN pip install -r requirements.txt