### 在233机器上做：
sudo docker build -t vincentzyu/awa-bot-docker:latest .
sudo docker build --no-cache -t vincentzyu/awa-bot-docker:latest .

sudo docker login --username=vincentzyu crpi-70a5fdkixq7r47ok.cn-hangzhou.personal.cr.aliyuncs.com

sudo docker images

sudo docker tag vincentzyu/awa-bot-docker:latest crpi-70a5fdkixq7r47ok.cn-hangzhou.personal.cr.aliyuncs.com/qwq_namespace/awa-bot-docker:latest

sudo docker push crpi-70a5fdkixq7r47ok.cn-hangzhou.personal.cr.aliyuncs.com/qwq_namespace/awa-bot-docker:latest

### 在241Windows机器上做：
docker build -t vincentzyu/awa-bot-docker:latest .
docker build --no-cache -t vincentzyu/awa-bot-docker:latest .


docker login --username=vincentzyu crpi-70a5fdkixq7r47ok.cn-hangzhou.personal.cr.aliyuncs.com

docker images

docker tag vincentzyu/awa-bot-docker:latest crpi-70a5fdkixq7r47ok.cn-hangzhou.personal.cr.aliyuncs.com/qwq_namespace/awa-bot-docker:latest

docker push crpi-70a5fdkixq7r47ok.cn-hangzhou.personal.cr.aliyuncs.com/qwq_namespace/awa-bot-docker:latest


### 在84机器上做
sudo docker login --username=vincentzyu crpi-70a5fdkixq7r47ok.cn-hangzhou.personal.cr.aliyuncs.com

sudo docker pull crpi-70a5fdkixq7r47ok.cn-hangzhou.personal.cr.aliyuncs.com/qwq_namespace/awa-bot-docker:latest


sudo docker ps -a
sudo docker images -a

sudo docker stop awa-name
sudo docker rm awa-name

sudo docker run \
--name awa-name \
-p 5140:5140 \
-v /home/bawuyinguo/SSoftwareFiles/koishi/images/images:/app/images \
crpi-70a5fdkixq7r47ok.cn-hangzhou.personal.cr.aliyuncs.com/qwq_namespace/awa-bot-docker:latest

#### 看一下docker中的位置
sudo docker exec -it awa-name bash
