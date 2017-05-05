#!/bin/bash

VER=2.0.11.2
TAR_FILE=uwsgi-${VER}.tar.gz
SRC_DIR=uwsgi-${VER}

if [ ! -e ${TAR_FILE} ]; then
	curl http://projects.unbit.it/downloads/${TAR_FILE} > ${TAR_FILE}
fi

if [ ! -d ${SRC_DIR} ]; then
	tar xzvf ${TAR_FILE}
fi

cd $SRC_DIR
cp ../bootstrap.py ./
python uwsgiconfig.py -b ../pex
cd -

cp $SRC_DIR/pex_uwsgi ./
