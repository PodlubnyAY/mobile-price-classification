import uvicorn
from fastapi import FastAPI
from api_handler import FastAPIHandler
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram

app = FastAPI()
app.handler = FastAPIHandler()

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

prediction_metric = Histogram(
    'prediction_metric_histogram',
    'histogram of predicted prices',
    buckets=(0.9,1.9,2.9,3.9)
)


@app.get('/')
def root_dir():
    return({'Hello': 'world'})


@app.post('/api/prediction')
def make_prediction(phone_id: int, item_features: dict):
    prediction = app.handler.predict(item_features)[0]
    prediction_metric.observe(prediction)
    return {
        'price_range': str(prediction),
        'phone_id': phone_id
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)