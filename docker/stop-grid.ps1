docker ps
docker stop $(docker ps -a  --format "{{.Names}}")
docker rm  $(docker ps -a  --format "{{.Names}}")
docker ps