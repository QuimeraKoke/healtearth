Vagrant.configure("2") do |config|
  config.vm.box = "XenialXerus64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/xenial/current/xenial-server-cloudimg-amd64-vagrant.box"
  config.vm.provision :shell, path: "assets/bootstrap.sh", privileged: false
  # config.vm.provision :shell, path: "Assets/bootstrap.sh", privileged: false
  config.vm.network :forwarded_port, guest: 8000, host: 8001 
  config.vm.network :forwarded_port, guest: 27017, host: 27017
end
