import pytest
from app.schemas import ClassifyRequest, ClassifyResponse

def test_request_schema():
    """Test request schema"""
    request = ClassifyRequest(text="Test")
    assert request.text == "Test"
    print("✅ Request schema test passed")

def test_response_schema():
    """Test response schema"""
    response = ClassifyResponse(label="POSITIVE", score=0.95)
    assert response.label == "POSITIVE"
    assert response.score == 0.95
    print("✅ Response schema test passed")

def test_positive_words():
    """Test positive word detection"""
    text = "Отличный продукт"
    positive_words = ["отличн", "хорош", "класс"]
    result = any(word in text.lower() for word in positive_words)
    assert result == True
    print("✅ Positive words test passed")

def test_negative_words():
    """Test negative word detection"""
    text = "Ужасное качество"
    positive_words = ["отличн", "хорош", "класс"]
    result = any(word in text.lower() for word in positive_words)
    assert result == False
    print("✅ Negative words test passed")
