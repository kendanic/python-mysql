
docker pull ubuntu/mysql

docker run -d --log-driver syslog --log-opt syslog-address=udp://192.168.1.10:514 tag="docker-{{.Name}}-{{.ID}}" "syslog-format": "rfc5424micro" "syslog-facility": "daemon" --name test_db -e TZ=IST -p 3310:3306 -e MYSQL_ROOT_PASSWORD=Passwd@123 ubuntu/mysql:latest

docker logs -f test_db

docker exec -it test_db /bin/bash

sudo docker exec -it test_db mysql -uroot -p

docker exec -it test_db service mysql restart

sudo docker inspect test_db | grep -i port

sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' test_db


ALTER USER 'ken'@'localhost' IDENTIFIED BY 'NewPassword';
ALTER USER 'ken'@'%' IDENTIFIED BY 'Pass@12345';


CREATE USER 'ken'@'%' IDENTIFIED BY 'Ken@123';
GRANT ALL PRIVILEGES ON *.* TO 'ken'@'%';
FLUSH PRIVILEGES;

GRANT ALL PRIVILEGES ON kendanic.* TO 'ken'@'%' IDENTIFIED BY 'Ken@123';
FLUSH PRIVILEGES;


docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mysql-container


https://www.rsyslog.com/doc/installation/rsyslog_docker.html

https://betterstack.com/community/guides/logging/rsyslog-explained/

https://dev.to/danielfavour/configuring-docker-syslog-logging-driver-for-docker-dameon-containers-1aoj

