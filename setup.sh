sudo apt-get update
sudo apt-get upgrade
sudo apt-get install --yes python3-pip tcl rabbitmq-server
sudo rabbitmq-plugins enable rabbitmq_management
sudo pip3 install celery flower
