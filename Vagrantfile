# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
    # The most common configuration options are documented and commented below.
    # For a complete reference, please see the online documentation at
    # https://docs.vagrantup.com.
  
    # Every Vagrant development environment requires a box. You can search for
    # boxes at https://vagrantcloud.com/search.
    config.vm.box = "centos/7"

    # config.vm.network "public_network", bridge: "wlp0s20f3"
    # config.vm.network "public_network"
  
    # InfluxDB

    config.vm.define "nodeInflux" do |node2|
      node2.vm.network "forwarded_port", guest: 22, host: 2300
      node2.vm.network "forwarded_port", guest: 8086, host: 8081
      node2.vm.hostname = "influx"
      node2.vm.network "private_network", ip: "192.168.56.4", virtualbox__intnet: "private_network"
      node2.vm.provider "virtualbox" do |vb|
       vb.memory = "2048"
       vb.cpus = "2"
      end
    end
    
    # Grafana

    config.vm.define "nodeGrafana" do |node3|
      node3.vm.network "forwarded_port", guest: 22, host: 2301
      node3.vm.network "forwarded_port", guest: 3000, host: 8080
      node3.vm.hostname = "grafana"
      node3.vm.network "private_network", ip: "192.168.56.5", virtualbox__intnet: "private_network"
      node3.vm.provider "virtualbox" do |vb|
       vb.memory = "1024"
       vb.cpus = "1"
      end
    end
    
    # Telegraf

    config.vm.define "nodeTelegraf" do |node4|
      node4.vm.network "forwarded_port", guest: 22, host: 2302
      node4.vm.hostname = "telegraf"
      node4.vm.network "private_network", ip: "192.168.56.6", virtualbox__intnet: "private_network"
      node4.vm.provider "virtualbox" do |vb|
       vb.memory = "512"
       vb.cpus = "1"
      end
    end
    
  end