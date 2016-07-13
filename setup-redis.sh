sudo apt-get update
sudo apt-get upgrade
sudo apt-get install --yes python3-pip tcl
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make test
sudo make install
sudo pip3 install celery flower
cd ..
sudo rm -r redis-stable/
rm redis-stable.tar.gz
cp proj/celery.py proj/celery-amqp.py
mv proj/celery-redis.py proj/celery.py
redis-server &
