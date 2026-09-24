from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from app.schemas import ClassifyRequest, ClassifyResponse

# Глобальная переменная для модели
model_instance = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model_instance
    print("🚀 STARTUP: Загружаем модель...")
    model_instance = {"name": "test_nlp_model", "status": "loaded"}
    print(f"✅ STARTUP: Модель загружена: {model_instance}")
    yield
    print("🛑 SHUTDOWN: Остановка...")
    model_instance = None

app = FastAPI(title="NLP Classification API", version="1.0.0", lifespan=lifespan)

@app.get("/health")
async def health_check():
    global model_instance
    return {"status": "ok", "model_loaded": model_instance is not None}

@app.post("/v1/classify", response_model=ClassifyResponse)
async def classify_text(request: ClassifyRequest):
    global model_instance
    if model_instance is None:
        raise HTTPException(status_code=500, detail="Модель не загружена")
    
    text_lower = request.text.lower()
    positive_words = ["отличн", "хорош", "класс", "прекрасн", "супер"]
    label = "POSITIVE" if any(word in text_lower for word in positive_words) else "NEGATIVE"
    
    return ClassifyResponse(label=label, score=0.95)
