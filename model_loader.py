from contextlib import asynccontextmanager
from fastapi import FastAPI
from typing import Optional

model_instance: Optional[dict] = None

def load_model():
    print("🔄 Загрузка модели в память...")
    return {"name": "test_nlp_model", "status": "loaded", "version": "1.0"}

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model_instance
    print("🚀 Запуск приложения, загружаем модель...")
    model_instance = load_model()
    print(f"✅ Модель загружена: {model_instance}")
    yield
    print("🛑 Остановка приложения...")
    model_instance = None
