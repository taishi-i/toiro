FROM ubuntu:18.04

ENV LANG "ja_JP.UTF-8"
ENV PYTHONIOENCODING "utf-8"

RUN apt update -y && \
    apt install -y libprotobuf-dev libgoogle-perftools-dev \
    language-pack-ja build-essential \
    wget git g++ make cmake vim \
    python3 python3-dev python3-pip

# kytea
RUN wget http://www.phontron.com/kytea/download/kytea-0.4.7.tar.gz && \
    tar zxvf kytea-0.4.7.tar.gz && cd kytea-0.4.7 && \
    wget https://patch-diff.githubusercontent.com/raw/neubig/kytea/pull/24.patch && \
    git apply ./24.patch && ./configure && \
    make && make install && ldconfig -v

# jumanpp
RUN wget https://github.com/ku-nlp/jumanpp/releases/download/v2.0.0-rc3/jumanpp-2.0.0-rc3.tar.xz && \
    tar xvf jumanpp-2.0.0-rc3.tar.xz && \
    cd jumanpp-2.0.0-rc3 && mkdir build && cd build && cmake .. && make install


WORKDIR /workspace
COPY . toiro

RUN pip3 install -U pip
RUN cd toiro && pip3 install .[all_tokenizers]

CMD ["/bin/bash"]
