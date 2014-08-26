# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise64"
  config.vm.network "forwarded_port", guest: 5000, host: 8001
  # config.vm.network "public_network"
  config.ssh.forward_agent = true
  config.vm.provision "shell", path: 'provision.sh'
end
