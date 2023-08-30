#! /bin/bash

VERSION=0.16.3rc1

make dist
mkdir -p ../deb/
rm -rf ../deb/*
cp -v stimfit-${VERSION}.tar.gz ../deb/
cp -v stimfit-${VERSION}.tar.gz ../deb/stimfit_${VERSION}.orig.tar.gz
cd ../deb/
tar -xzf stimfit_${VERSION}.orig.tar.gz
cd stimfit-${VERSION}
cp -rv ../../../dist/debian ./
debuild -S -sa
sudo pbuilder build --basetgz /var/cache/pbuilder/base.tgz ../*.dsc
