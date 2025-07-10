# Base image
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN echo '#!/bin/sh\nexit 101' > /usr/sbin/policy-rc.d && chmod +x /usr/sbin/policy-rc.d

RUN apt update \
    apt install -y mysql-server vim-tiny && \
    apt clean && rm -rf /var/lib/apt/lists/*

EXPOSE 3306

CMD ["mysqld"]

