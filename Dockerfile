FROM ubuntu:22.04

USER root

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update -y && \
    apt-get install wget -y

RUN  apt-get install python3.10 -y && \
    apt-get install python3-pip -y && \
    pip install behave==1.2.6  && \
    pip install selenium==4.12.0

RUN wget "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb" && \
    apt-get install ./google-chrome-stable_current_amd64.deb -y && \
    rm google-chrome*

WORKDIR /test

ADD . .

