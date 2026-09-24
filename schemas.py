from pydantic import BaseModel, Field

class ClassifyRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Текст для классификации")

class ClassifyResponse(BaseModel):
    label: str
    score: float
