from pydantic import BaseModel, Field

class ClassifyRequest(BaseModel):
    text: str = Field(..., description="Текст для классификации", examples=["Этот продукт просто отличный!"])

class ClassifyResponse(BaseModel):
    label: str = Field(..., description="Предсказанный класс", examples=["POSITIVE"])
    score: float = Field(..., description="Уверенность модели", examples=[0.95])
