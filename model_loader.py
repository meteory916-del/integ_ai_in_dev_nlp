from contextlib import asynccontextmanager
from fastapi import FastAPI
from transformers import pipeline

model_instance = None

def load_model():
    print("🔄 Загрузка HuggingFace модели...")
    model = pipeline(
        "sentiment-analysis",
        model="blanchefort/rubert-base-cased-sentiment-rusentiment"
    )
    print("✅ Модель загружена")
    return model

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model_instance
    print("🚀 STARTUP: Загружаем модель...")
    model_instance = load_model()
    print(f"✅ STARTUP: Модель загружена: {model_instance is not None}")
    yield
    print("🛑 SHUTDOWN: Остановка...")
    model_instance = None
