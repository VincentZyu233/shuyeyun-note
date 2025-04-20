```bash
docker run -d \
-e NAPCAT_GID=$(id -g) \
-e NAPCAT_UID=$(id -u) \
-p 13000:3000 \
-p 13001:3001 \
-p 16099:6099 \
--name napcat-awa \
--restart=always \
mlikiowa/napcat-docker:latest

sudo docker logs -f napcat-awa
sudo docker exec -it napcat-awa /bin/bash

```

```bash
docker run -d \
-e NAPCAT_GID=$(id -g) \
-e NAPCAT_UID=$(id -u) \
-p 23000:3000 \
-p 23001:3001 \
-p 26099:6099 \
--name napcat-ovo \
--restart=always \
mlikiowa/napcat-docker:latest


sudo docker logs -f napcat-awa
sudo docker exec -it napcat-awa /bin/bash

```


```bash
sudo docker stop $(sudo docker ps -aq)
sudo docker rm $(sudo docker ps -aq)
sudo docker images

```