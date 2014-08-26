#!/bin/bash

function update_apt {
    # Check if we need to perform a weekly pkgcache update
    touch -d '-1 week' /vagrant/.limit
    if [ /vagrant/.limit -nt /var/cache/apt/pkgcache.bin ]; then
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

# Tools
install vim-nox
install git
install curl
install htop

# Install updated gearman-job-server
install python-software-properties
sudo add-apt-repository ppa:gearman-developers/ppa -y
sudo apt-get update
install gearman-job-server
install gearman-tools

# Install Python
install python
install python-pip

sudo pip install ipython
sudo pip install flask

# Install python-gearman lib
sudo pip install gearman

# Install pygear lib
install python-dev
install libgearman-dev
install build-essential
sudo pip install git+https://github.com/Yelp/pygear.git@master

# Install PHP and gearman lib
install php5-cli
install php-pear
sudo pecl install gearman
# Enable PHP gearman extension
sudo sh -c 'echo "extension=gearman.so" > /etc/php5/conf.d/gearman.ini'

# Clean up
sudo apt-get -y autoremove
sudo apt-get purge memcached  # Why was memcached running on this box?