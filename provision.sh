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

change_hostname 'vagrant-ubuntu'
update_apt
install vim-nox
install curl
install git
install htop
install tree
install python-pip
install ipython