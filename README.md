ビルド
docker build . -t bolt-docker  

docker run
docker run -it -d --name slack-messages bolt-docker 


export SLACK_BOT_TOKEN=xoxb-4051031086081-4051041571265-qH8YDWZOetmdkG1iBIUIOH1a   
export SLACK_APP_TOKEN=xapp-1-A041H0YHNFK-4077265939473-c1b5f6da64228277f3bfd57e124407adf5913a7a8a662968e374f77cc266ae6e
export DEEPL_API_TOKEN=d857ebc3-1537-41ac-968f-e280bcb43793    
