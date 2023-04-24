FROM amazonlinux:latest
LABEL maintainer Paulo Henrique (phraulino@outlook.com)

# Install apt dependencies
RUN yum update -y && \
    yum groupinstall -y "Development Tools" && \
    yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel xz-devel && \
    yum clean all


RUN curl -O https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz && \
    tar xzf Python-3.10.0.tgz && \
    cd Python-3.10.0 && \
    ./configure --enable-optimizations && \
    make altinstall

RUN ln -s /usr/local/bin/python3.10 /usr/local/bin/python

COPY . /app

WORKDIR /app

RUN python -m pip install --upgrade pip
RUN python -m pip install --user -r requirements.txt
RUN chmod +x init_db.sh

CMD ./init_db.sh && python -m gunicorn -c config.py src.main:app --preload
