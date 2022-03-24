FROM python:3.8-buster

LABEL maintainer="DA specialist <da-specialist-gr@access-company.com>"

USER root
WORKDIR /var/tmp

RUN set -x && \
    : Update package and upgrade installed packages && \
    apt update && apt upgrade -y && \
    apt install sudo

RUN set -x && \
    : Install Mecab && \
    wget -O mecab-0.996.tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE" && \
    tar zxf mecab-0.996.tar.gz && cd mecab-0.996 && \
    ./configure --with-charset=utf8 --prefix=/usr/local --build=arm-unknown-linux-gnu --host=arm-unknown-linux-gnu --target=arm-unknown-linux-gnu && make && make install && ldconfig

RUN set -x && \
    : Install IPA dictionary && \
    wget -O mecab-ipadic-2.7.0-20070801.tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM" && \
    tar zxf mecab-ipadic-2.7.0-20070801.tar.gz && cd mecab-ipadic-2.7.0-20070801 && \
    ./configure --with-charset=utf8 --prefix=/usr/local --build=arm-unknown-linux-gnu --host=arm-unknown-linux-gnu --target=arm-unknown-linux-gnu && make && make install && cd .. &&\
    #
    : Install JUMAN dictionary && \
    curl -Lb /tmp/cookie "https://drive.google.com/uc?expornnt=download&confirm=t&id=0B4y35FiV1wh7X2pESGlLREpxdXM" -o mecab-jumandic-7.0-20130310.tar.gz && \
    tar zxf mecab-jumandic-7.0-20130310.tar.gz && cd mecab-jumandic-7.0-20130310 && \
    ./configure --with-charset=utf8 --prefix=/usr/local --build=arm-unknown-linux-gnu --host=arm-unknown-linux-gnu --target=arm-unknown-linux-gnu && make && make install && cd .. && \
    
    : Install NAIST dictionary && \
    wget http://iij.dl.sourceforge.jp/naist-jdic/53500/mecab-naist-jdic-0.6.3b-20111013.tar.gz && \
    tar zxf mecab-naist-jdic-0.6.3b-20111013.tar.gz && cd mecab-naist-jdic-0.6.3b-20111013 && \
    ./configure --with-charset=utf8 --prefix=/usr/local --build=arm-unknown-linux-gnu --host=arm-unknown-linux-gnu --target=arm-unknown-linux-gnu && make && make install && cd .. && \
    #
    : Install mecab-ipadic-NEologd && \
    git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git && \
    cd mecab-ipadic-neologd && \
    ./bin/install-mecab-ipadic-neologd -n -a -y && cd .. && \
    #
    : Install mecab-ipadic-NEologd && \
    git clone --depth 1 https://github.com/neologd/mecab-unidic-neologd.git && \
    cd mecab-unidic-neologd && \
    ./libexec/install-mecab-unidic.sh && ./bin/install-mecab-unidic-neologd -y -n

RUN set -x && \
    : Install CRF++ && \
    wget -O CRF++-0.58.tar.gz "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7QVR6VXJ5dWExSTQ" && \
    tar zxf CRF++-0.58.tar.gz && cd CRF++-0.58 && \
    ./configure --prefix=/usr/local --build=arm-unknown-linux-gnu --host=arm-unknown-linux-gnu --target=arm-unknown-linux-gnu && make && make install && \
    echo "/usr/local/lib" >> /etc/ld.so.conf.d/lib.conf && ldconfig

RUN set -x && \
    : Install CaboCha  && \
    curl -Lb /tmp/cookie "https://drive.google.com/uc?expornnt=download&confirm=t&id=0B4y35FiV1wh7SDd1Q1dUQkZQaUU" -o cabocha-0.69.tar.bz2 && \
    tar xjf cabocha-0.69.tar.bz2 && cd cabocha-0.69 && \
    ./configure --prefix=/usr/local --with-mecab-config=$(which mecab-config) --with-charset=utf8 --build=arm-unknown-linux-gnu --host=arm-unknown-linux-gnu --target=arm-unknown-linux-gnu \
    && make && make install && ldconfig

RUN set -x && \
    : Install boost for boost && \
    apt -y install libboost-dev && ldconfig && \
    #
    : Install JUMAN && \
    wget http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/juman/juman-7.01.tar.bz2 && \
    tar jxf juman-7.01.tar.bz2 && cd juman-7.01 && \
    ./configure --prefix=/usr/local --build=arm-unknown-linux-gnu --host=arm-unknown-linux-gnu --target=arm-unknown-linux-gnu \
    && make && make install && ldconfig

COPY requirements.txt /var/tmp

RUN set -x && \
    : Install Python libraries && \
    python -m pip install --upgrade pip && \
    python -m pip install -r /var/tmp/requirements.txt

RUN set -x && \
    : Install nodejs and npm && \
    apt install -y nodejs npm && \
    npm install n -g && \
    n stable && \
    apt purge -y nodejs npm && \
    #
    : Install JupyterLab extensions && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager && \
    jupyter nbextension enable --py --sys-prefix widgetsnbextension

RUN rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/tmp/*.*

## enable to use Japanease in Matplotlib
RUN apt update && apt install -y fonts-ipaexfont
RUN apt clean && rm -rf /var/lib/apt/lists/*

RUN sed -i "s/^#font\.family.*/font.family:  IPAexGothic/g" /usr/local/lib/python3.8/site-packages/matplotlib/mpl-data/matplotlibrc

RUN adduser access
ENV HOME /home/access
USER access
WORKDIR /home/access/work