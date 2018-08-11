Param([int] $count)
docker ps
docker stop $(docker ps -a  --format "{{.Names}}")
docker rm  $(docker ps -a  --format "{{.Names}}")
docker-compose up -d
docker-compose scale chromenode=$count firefoxnode=$count
docker ps