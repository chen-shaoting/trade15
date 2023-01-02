FROM python:3.9-buster

MAINTAINER Jae Liu<liuji857286@gmail.com>

WORKDIR /usr/src

# install ta-lib from source
ADD ta-lib-0.4.0-src.tar.gz ./
RUN  cd ta-lib/ && ./configure --prefix=/usr && make && make install

#install python packages from requirements file
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
        -i 'https://mirrors.aliyun.com/pypi/simple'

EXPOSE 8888/tcp

# exec jupyter
ENTRYPOINT [ "jupyter-notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root" ]

CMD [ "/notes" ]
