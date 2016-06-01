# base image
FROM centos:centos7.1.1503
MAINTAINER kentaro a
ENV PATH $PATH:/usr/local/bin

# Install required modules
RUN yum -y install git
RUN yum -y install wget
RUN yum -y install tar
RUN yum -y install gcc zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc-c++
RUN yum -y install make

# Get the source of Python3 and build it.
RUN cd /usr/local/src/ && \
    wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz && \
    tar zxvf Python-3.5.1.tgz && \
    cd /usr/local/src/Python-3.5.1 && \
    ./configure && \
     make && make install

# upgrade pip for latest-version
RUN pip3 install --upgrade pip

# Install Python's utility modules
RUN pip3 install pandas
RUN pip3 install xlwt
RUN pip3 install openpyxl
RUN pip3 install httplib2
RUN cd /usr/local/src/ && \
    git clone https://github.com/mysql/mysql-connector-python.git && \
    cd mysql-connector-python && \
    python3 ./setup.py build && \
    python3 ./setup.py install

# Setting up sample-modules
RUN git clone https://github.com/kentaro-a/python-proto.git /home/python/
