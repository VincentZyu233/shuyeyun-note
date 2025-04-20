### bungeecord
```sh
#!/bin/bash

JAVA_OPTS="-Xms512M -Xmx1024M"
JAR_FILE="./BungeeCord.jar"
JAVA_PATH="/mnt/data/SSoftwareFiles/jdk21/jdk-21.0.5/bin/java"

cd "$(dirname "$0")"
echo "【qwq】pwd路径是：$(pwd)"
echo "使用的java版本："
$JAVA_PATH --version

$JAVA_PATH $JAVA_OPTS -jar $JAR_FILE nogui
```

### paper1.21.3-lobby
```sh
#!/bin/bash

JAVA_OPTS="-Xms1111M -Xmx2222M"
JAR_FILE="./paper-1.21.3-56.jar"
JAVA_PATH="/mnt/data/SSoftwareFiles/jdk21/jdk-21.0.5/bin/java"

cd "$(dirname "$0")"
echo "【qwq】pwd路径是：$(pwd)"
echo "使用的java版本："
$JAVA_PATH --version

$JAVA_PATH $JAVA_OPTS -jar $JAR_FILE nogui

```


