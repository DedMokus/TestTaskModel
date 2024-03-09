from catboost import CatBoostClassifier
import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel
from fastapi.responses import FileResponse

model = CatBoostClassifier().load_model('model', format='cbm')
app = FastAPI()

@app.post('/predict')
def predict(data = Body()):
    features = [float(feature) for feature in data['features'].split(',')]
    prediction = model.predict_proba(features).tolist()
    print(data)

    return {'prediction' : f"Class 0 is {prediction[0]} chance, Class 1 is {prediction[1]} chance"}

@app.get("/")
def root():
    return FileResponse("index.html")

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=80)
