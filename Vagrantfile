# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "locust1" do |locust1|
    locust1.vm.box = "ubuntu/trusty64"
    # locust1.vm.network "private_network", ip: "10.211.55.30"

    locust1.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end

    locust1.vm.provision "ansible" do |ansible|
      ansible.playbook = "deploy/playbook.yml"
      ansible.verbose = "v"
    end
  end
  config.vm.define "locust2" do |locust2|
    locust2.vm.box = "ubuntu/trusty64"
    # locust2.vm.network "private_network", ip: "10.211.55.31"

    locust2.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end

    locust2.vm.provision "ansible" do |ansible|
      ansible.playbook = "deploy/playbook.yml"
      ansible.verbose = "v"
    end
  end
end
