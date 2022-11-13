import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

class IrisClassifier:
    def __init__(self):
        self.X, self.y = load_iris(return_X_y=True)
        self.model_fname_ = "iris_model.pkl"
        try:
            self.rfc = joblib.load(self.model_fname_)
        except Exception as _:
            self.rfc = self.train_model()
            joblib.dump(self.rfc, self.model_fname_)
        self.iris_type = {
            0: 'setosa',
            1: 'versicolor',
            2: 'virginica'
        }

    def train_model(self):
        rfc = RandomForestClassifier()
        model = rfc.fit(self.X, self.y)
        return model

    def classify_iris(self, features: dict):
        X = [[features['sepal_l'], features['sepal_w'], features['petal_l'], features['petal_w']]]
        prediction = self.rfc.predict(X)
        probability = self.rfc.predict_proba(X).max()
        return {'class': self.iris_type[prediction[0]],
                'probability:': round(probability, 2)}