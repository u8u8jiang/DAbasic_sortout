from fastapi import APIRouter
from iris.iris_classifier import IrisClassifier
from starlette.responses import JSONResponse

router = APIRouter()

## post是RESTFUL中定義的一種資料傳輸的方式
## iris_features是一個字典，要傳入到一個類中的方法去預測我給的資料是哪一種花
@router.post('/classify_iris')
def classify_iris(iris_features: dict):
    iris_classifier = IrisClassifier()
    return JSONResponse(iris_classifier.classify_iris(iris_features))