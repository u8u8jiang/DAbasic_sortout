import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

class IrisClassifier:
    def __init__(self):
        ## Load iris資料，分別賦予X, y
        self.X, self.y = load_iris(return_X_y=True)
        ## 預先定義一個名稱是我們訓練完的模型
        self.model_fname_ = "iris_model.pkl"
        try:
            # joblib是我載入訓練好的模型
            # 第一跑起來，是沒有iris_model.pkl這個檔案，所以會跑到except這邊
            self.rfc = joblib.load(self.model_fname_)
        except Exception as _:
            # 定義一個rfc呼叫自己的train_model()這個功能
            self.rfc = self.train_model()
            # 訓練完後，把模型儲存起來
            joblib.dump(self.rfc, self.model_fname_)
            # 我們把類別的數字轉成文字，方便閱讀
        self.iris_type = {
            0: 'setosa',
            1: 'versicolor',
            2: 'virginica'
        }

    def train_model(self):
        rfc = RandomForestClassifier()
        ## 拿到資料去做訓練
        model = rfc.fit(self.X, self.y)
        return model
    ##iris_classifier_router.py中就是調用這個函數去做預測
    def classify_iris(self, features: dict):
        ## features是一個字典格式，我可以用[]的方式得到數值，再轉為array的形式
        X = [[features['sepal_l'], features['sepal_w'], features['petal_l'], features['petal_w']]]
        ## 預測是哪一類
        prediction = self.rfc.predict(X)
        ## 最大的機率職from那個類
        probability = self.rfc.predict_proba(X).max()
        ## return一個json檔
        return {'class': self.iris_type[prediction[0]],
                'probability:': round(probability, 2)}