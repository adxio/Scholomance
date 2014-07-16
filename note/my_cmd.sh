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
git config --global alias.st 'status -sb'

git branch --set-upstream-to=origin/<branch> <my-branch>


tratao: 2984431774 FT9-aBB-c3R-pdz

00 3 * * * pg_dump -U tratao -d bms -f /home/tratao/backup/bms-`date +%Y%m%d`.sql

mbp:
高度: 2.41 厘米 (0.95 英寸)
宽度：32.5 厘米 (12.78 英寸)
深度：22.7 厘米 (8.94 英寸)
重量：2.06 千克 (4.5 磅)2

云梯，用户名：brucewilliam；密码：0085818588
