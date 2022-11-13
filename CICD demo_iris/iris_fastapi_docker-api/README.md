## iris_fastapi_docker 

# 20210812 update

1. 新增CI功能，可自動建立image
- {+ .gitlab-ci.yml +}是用kaniko建立CI流程；
- {+ .gitlab-ci_another.yml +}是用docker建立CI流程；

2. 新增CICD的Variables

# 20201231 update

參考自[本篇文章](https://towardsdatascience.com/deploying-iris-classifications-with-fastapi-and-docker-7c9b83fdec3a)，建立一個鳶尾花docker分析服務 

可在terminal執行: 

- {+ docker build . -t iris +}

- {+ docker run -i -d -p [localport]:[5000] iris +}

其中，localport=代表本機端口，port=「5000」代表暴露容器內5000端口；

執行成功後可以在以下兩個網址查看

- {- http://[localport]:[5000]/docs -}

- {- http://[localport]:[5000]/redoc -}

或是可以在terminal執行

* curl -X POST "http://localhost:[localport]/iris/classify_iris" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"sepal_l\":0,\"sepal_w\":0,\"petal_l\":0,\"petal_w\":0}" +}
