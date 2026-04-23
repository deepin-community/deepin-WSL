#!/bin/bash

set -e -u -x

ARCH=$1
VERSION=$2

ROOTFS=deepin-wsl-rootfs-${ARCH}.tar.gz
ROOTFS_URL=https://github.com/deepin-community/deepin-rootfs/releases/download/${VERSION}/${ROOTFS}

curl -OLS $ROOTFS_URL

mkdir -p $ARCH
sudo tar -zxvf $ROOTFS -C $ARCH

sudo cp config/wsl-distribution.conf $ARCH/etc/
sudo cp config/oobe.sh $ARCH/etc/
sudo chmod +x $ARCH/etc/oobe.sh
sudo mkdir -p $ARCH/usr/lib/wsl/
sudo cp config/terminal-profile.json $ARCH/usr/lib/wsl/
sudo cp resources/deepin.ico $ARCH/usr/lib/wsl/deepin.ico

pushd $ARCH
sudo tar --numeric-owner --absolute-names -c  * | gzip --best > ../deepin-$ARCH.wsl
popd
