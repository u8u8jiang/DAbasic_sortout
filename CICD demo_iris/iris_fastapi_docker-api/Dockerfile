## FROM的意思是，我要拉一個基礎的印象檔(IMAGE)
## 因為我需要一台最基本的小電腦(類似一個新的APPLE M1, 甚麼東西都還沒有裝)
FROM harbor-k8s.wzs.wistron.com.cn/datteam/python:3.7-slim-buster
## LABEL的意思是，寫個標籤在這個IMANGE上
## 好處是我有了基礎鏡像檔之後，我裝上了個人需要的套件，再打包成有個標籤名稱為「ci iris classifier api」
## 方便我在HARBOR辨識，哪個是我的IMAGE
LABEL maintainer="ci iris classifier api"

## RUN的意思是，我要在一個終端機裡面執行程式碼
## mkdir的意思是，我要建立一個資料夾
## mkdir中的-p意思是， -p, --parents     no error if existing, make parent directories as needed
## 你可以通過執行一個程式碼加上help得到說明，比如說: mkdir --h或是mkdir --help
RUN mkdir -p /usr/src/iris
## WORKDIR的意思是，我目前要進去這個/usr/src/iris裡面
WORKDIR /usr/src/iris

## COPY requirements.txt這個檔案到/usr/src/iris裡面
COPY requirements.txt .

## RUN跟上面的一樣，我需要執行pip安裝，pip install pandas
## 常常會需要加一個參數，叫做-i，目的是掛外網去下載套件，https://nexusoss.wistron.com/repository/pypi-proxy/simple這個是緯創源(類似清華源)
## 這個是緯創需要的認證，--trusted-host nexusoss.wistron.com
## -r的意思是，我要遍歷requirements.txt這個檔案裡面所有的套件(package)
### requirements.txt包含以下五個需要安裝的套件
### fastapi, uvicorn: 就是在做API用的，可以參考這個官網: https://fastapi.tiangolo.com/
### numpy: 是做矩陣運算的
### scikit-learn: 是做科學運算的
### joblib: 訓練完的模型，需要用這個套件保存
RUN pip3 install --trusted-host nexusoss.wistron.com -i https://nexusoss.wistron.com/repository/pypi-proxy/simple -r requirements.txt

COPY . .
## EXPOSE的意思是我需要暴露一個端口出來，讓我去用網路的方式連結它
## 5000端口是指我在描述docker的特徵，或是請把5000暴露出來，8888:5000，8888我的電腦上端口，5000容器裡面的端口

EXPOSE 5000

## reload是指當我修改裡面內容時，服務會自動更新內容，通常是用在更新模型上
## iris.app:app就是去找iris這個資料夾中的app.py這個檔案
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "5000", "iris.app:app", "--reload"]
