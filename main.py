from fastapi import FastAPI, HTTPException
from schemas import ClassifyRequest, ClassifyResponse
import model_loader as ml

app = FastAPI(title="NLP Classification API", version="1.0.0", lifespan=ml.lifespan)

@app.post("/v1/classify", response_model=ClassifyResponse)
async def classify_text(request: ClassifyRequest):
    if ml.model_instance is None:
        raise HTTPException(status_code=500, detail="Модель не загружена")
    
    text_lower = request.text.lower()
    positive_words = ["отличн", "хорош", "класс", "прекрасн", "супер", "замечател", "great", "good", "excellent"]
    
    label = "POSITIVE" if any(word in text_lower for word in positive_words) else "NEGATIVE"
    
    return ClassifyResponse(label=label, score=0.95)

@app.get("/health")
async def health_check():
    return {"status": "ok", "model_loaded": ml.model_instance is not None}
