FROM harbor-k8s.wzs.wistron.com.cn/datteam/python:3.7-slim-buster
LABEL maintainer="ci/cd iris classifier api"

RUN mkdir -p /usr/src/iris
WORKDIR /usr/src/iris

COPY requirements.txt .
RUN pip3 install --trusted-host nexusoss.wistron.com -i https://nexusoss.wistron.com/repository/pypi-proxy/simple -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "5000", "iris.app:app", "--reload"]
