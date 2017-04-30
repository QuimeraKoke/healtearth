# General Config (Init)
echo "Gen. Config"
sudo apt-get update
sudo apt-get install python-pip -y
sudo pip install virtualenv
mkdir $HOME/virtual_envs
virtualenv $HOME/virtual_envs/healtearth
source $HOME/virtual_envs/healtearth/bin/activate
pip install --upgrade pip
pip install -r /vagrant/requirements.txt

echo "Provisioning Code "
sudo mkdir /var/healtearth
sudo chown ubuntu:www-data /var/healtearth
ln -s /vagrant/Healtearth /var/healtearth/Code

echo "Gunicorn"
sudo cp /vagrant/assets/gunicorn.conf /etc/systemd/system/
sudo mv /etc/systemd/system/gunicorn.conf /etc/systemd/system/healtearth.service
sudo systemctl start healtearth.service
sudo systemctl enable healtearth.service
sudo systemctl status healtearth.service

echo "Nginx"
sudo apt-get install nginx -y
sudo cp /vagrant/assets/nginx.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/codedeploy
sudo nginx -t
sudo systemctl reload nginx