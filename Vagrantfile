# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.define "puppet" do |puppet|

    # The most common configuration options are documented and commented below.
    # For a complete reference, please see the online documentation at
    # https://docs.vagrantup.com.

    # Every Vagrant development environment requires a box. You can search for
    # boxes at https://atlas.hashicorp.com/search.
    puppet.vm.box = "bento/ubuntu-16.04"

    # Disable automatic box update checking. If you disable this, then
    # boxes will only be checked for updates when the user runs
    # `vagrant box outdated`. This is not recommended.
    # config.vm.box_check_update = false

    # Create a forwarded port mapping which allows access to a specific port
    # within the machine from a port on the host machine. In the example below,
    # accessing "localhost:8080" will access port 80 on the guest machine.
    # NOTE: This will enable public access to the opened port
    # config.vm.network "forwarded_port", guest: 80, host: 8080

    # Create a forwarded port mapping which allows access to a specific port
    # within the machine from a port on the host machine and only allow access
    # via 127.0.0.1 to disable public access
    # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

    # Create a private network, which allows host-only access to the machine
    # using a specific IP.
    puppet.vm.network "private_network", ip: "192.168.33.10"
    puppet.vm.hostname = "puppet.londonappleadmins.org.uk"
    # Create a public network, which generally matched to bridged network.
    # Bridged networks make the machine appear as another physical device on
    # your network.
    # config.vm.network "public_network"

    # Share an additional folder to the guest VM. The first argument is
    # the path on the host to the actual folder. The second argument is
    # the path on the guest to mount the folder. And the optional third
    # argument is a set of non-required options.
    # config.vm.synced_folder "../data", "/vagrant_data"

    # Provider-specific configuration so you can fine-tune various
    # backing providers for Vagrant. These expose provider-specific options.
    config.vm.provider "vmware_fusion" do |v|
      v.vmx["memsize"] = "4096"
      v.vmx["numvcpus"] = "2"
    end
    #
    # View the documentation for the provider you are using for more
    # information on available options.

    # Enable provisioning with a shell script. Additional provisioners such as
    # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
    # documentation for more information about their specific syntax and use.
    puppet.vm.provision "file", source: "puppet.conf", destination: "/tmp/puppet.conf"
    # puppet.vm.provision "file", source: "~/src/airbnb/puppet_control", destination: "/tmp/puppet_control"
    puppet.vm.provision "shell", inline: <<-SHELL

    #
    # This bootstraps Puppet Server on Ubuntu 16.04 LTS.
    #
    set -e

    REPO_DEB_URL="https://apt.puppetlabs.com/puppetlabs-release-pc1-xenial.deb"

    #--------------------------------------------------------------------
    # NO TUNABLES BELOW THIS POINT
    #--------------------------------------------------------------------
    if [ "$EUID" -ne "0" ]; then
    echo "This script must be run as root." >&2
    exit 1
    fi

    # Install the PuppetLabs repo
    echo "Configuring PuppetLabs repo..."
    mkdir -p /etc/puppetlabs/puppet
    cp /tmp/puppet.conf /etc/puppetlabs/puppet/puppet.conf
    cp /vagrant/hiera.yaml /etc/puppetlabs/puppet/hiera.yaml
    mkdir -p /etc/puppetlabs/r10k
    cp /vagrant/r10k.yaml /etc/puppetlabs/r10k/r10k.yaml
    mkdir -p /root/.ssh
    cp /vagrant/ssh/id_rsa /root/.ssh/id_rsa
    chown root /root/.ssh/id_rsa
    chmod 600 /root/.ssh/id_rsa
    ssh-keyscan -t rsa github.com >> /root/.ssh/known_hosts
    repo_deb_path=$(mktemp)
    wget --output-document=${repo_deb_path} ${REPO_DEB_URL}
    dpkg -i ${repo_deb_path}
    apt-get update > /dev/null

    # Install Puppet
    echo "Installing Puppet Server..."
    apt-get install -o Dpkg::Options::="--force-confold" -y puppetserver rubygems

    echo "Installing r10k"
    gem install r10k
    echo "Installing lookup_http"
    /opt/puppetlabs/bin/puppetserver gem install lookup_http
    /opt/puppetlabs/puppet/bin/gem install lookup_http
    echo "Running 10k"
    r10k deploy environment -pv
    puppet module install crayfishx/hiera_http
    puppetserver gem install CFPropertyList
    cp /vagrant/plist.rb /opt/puppetlabs/puppet/lib/ruby/vendor_ruby/puppet/util/plist.rb
    systemctl start puppetserver
    systemctl enable puppetserver
    SHELL
  end
  config.vm.define "app" do |app|
    app.vm.box = "bento/ubuntu-16.04"
    app.vm.network "private_network", ip: "192.168.33.11"
    app.vm.hostname = "app.londonappleadmins.org.uk"
    app.vm.provision "shell", inline: <<-SHELL
    #
    # This bootstraps Puppet Server on Ubuntu 16.04 LTS.
    #
    repo_deb_path=$(mktemp)
    wget --output-document=${repo_deb_path} https://download.docker.com/linux/ubuntu/gpg
    apt-key add ${repo_deb_path}
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    apt-get update > /dev/null
    apt-get install -y docker-ce
    sh /vagrant/hiera_backend_app/build_and_run.sh
    SHELL

  end
  config.vm.define "client" do |client|
    # Every Vagrant development environment requires a box. You can search for
    # boxes at https://atlas.hashicorp.com/search.
    client.vm.box = "darwin-1012"
    client.ssh.insert_key = false
    client.vm.provider "vmware_fusion" do |v|
      v.gui = true
      v.vmx["memsize"] = "4096"
      v.vmx["numvcpus"] = "2"
      v.vmx["SMBIOS.use12CharSerialNumber"] = "TRUE"
      v.vmx["serialNumber"] = "VMVJK4SQ9NV1"
    end
    client.vm.provision "file", source: "client_puppet.conf", destination: "/tmp/puppet.conf"
    client.vm.provision "shell", inline: <<-SHELL
    mkdir -p /etc/puppetlabs/puppet
    cp /tmp/puppet.conf /etc/puppetlabs/puppet/puppet.conf
    /opt/puppetlabs/bin/puppet apply /vagrant/manifests/client.pp
    SHELL
  end
end
