from fastapi import APIRouter
from iris.iris_classifier import IrisClassifier
from starlette.responses import JSONResponse

router = APIRouter()

@router.post('/classify_iris')
def classify_iris(iris_features: dict):
    '''
    iris_features={"sepal_l": 5, "sepal_w": 2, "petal_l": 3, "petal_w": 9}
    '''
    iris_classifier = IrisClassifier()
    return JSONResponse(iris_classifier.classify_iris(iris_features))
