ビルド
docker build . -t bolt-docker  

docker run
docker run -it -d --name slack-messages bolt-docker 
