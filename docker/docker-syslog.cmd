vim /etc/docker/daemon.json


{
  "log-driver": "syslog",
  "log-opts": {
    "syslog-address": "udp://192.168.1.10:514",
    "tag": "docker/{{.Name}}/{{.ID}}"
  }
}


{
  "log-driver": "syslog",
  "log-opts": {
    "syslog-address": "tcp://127.0.0.1:514",
    "syslog-facility": "daemon",
    "syslog-format": "rfc5424",
    "tag": "docker/{{.Name}}/{{.ID}}"
  }
}


RFC5424

/dev/log

docker run -d --name uat-web-app -p 8010:80 ubuntu/nginx

"tag": "docker/{{.Name}}/{{.ID}}"


docker inspect test-web --format '{{.HostConfig.LogConfig.Type}}'



log_format custom_format '$remote_addr - $remote_user "$request" $status $body_bytes_sent '
                          '"$http_referer" "$http_user_agent" response_time: $request_time';

access_log /dev/stdout custom_format;
