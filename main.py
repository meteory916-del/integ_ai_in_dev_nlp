from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from schemas import ClassifyRequest, ClassifyResponse
import model_loader as ml

app = FastAPI(title="NLP Classification API", version="1.0.0", lifespan=ml.lifespan)

@app.post("/v1/classify", response_model=ClassifyResponse)
async def classify_text(request: ClassifyRequest):
    if ml.model_instance is None:
        raise HTTPException(status_code=500, detail="Модель не загружена")
    
    result = ml.model_instance(request.text)[0]
    
    label_mapping = {
        "POSITIVE": "POSITIVE",
        "NEGATIVE": "NEGATIVE",
        "NEUTRAL": "NEUTRAL"
    }
    
    label = label_mapping.get(result["label"], result["label"])
    score = round(float(result["score"]), 4)
    
    return ClassifyResponse(label=label, score=score)

@app.get("/health")
async def health_check():
    return {"status": "ok", "model_loaded": ml.model_instance is not None}
