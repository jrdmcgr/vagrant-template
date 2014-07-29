#!/bin/bash

function update_apt {
    # Check if we need to perform a weekly pkgcache update
    touch -d '-1 week' /tmp/.limit
    if [ /tmp/.limit -nt /var/cache/apt/pkgcache.bin ]; then
        sudo apt-get -y update
    fi
}

function install {
    sudo apt-get install -y --force-yes $1
}

function change_hostname {
	local new_hostname="$1"
	local old_hostname="$(hostname)"
	sudo sed -i "s/$old_hostname/$new_hostname/" /etc/hostname /etc/hosts
	sudo hostname "$new_hostname" &> /dev/null
	# `&> /dev/null` to suppress this message: "sudo: unable to resolve host"
}

sudo apt-get install -y python-software-properties
sudo add-apt-repository ppa:gearman-developers/ppa -y
sudo apt-get update
sudo apt-get install -y gearman-job-server
sudo apt-get install -y python
sudo apt-get install -y python-pip
sudo apt-get install vim-nox

sudo pip install gearman
