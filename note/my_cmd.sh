# server
sudo redis-server /opt/local/etc/redis.conf

python auth.py > auth.log 2>&1 &
python show_log.py 8081 > show_log.log 2>&1 &

nohup ./auth > /home/tratao/auth.log 2>&1 &

# add storage user
useradd lee
usermod -a -G storage lee
smbpasswd -a lee
service samba restart

# change owner
sudo chgrp -R storage .
sudo chmod -R 775 .


# Git config
git config --global color.diff auto
git config --global color.status auto
git config --global color.branch auto

git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
