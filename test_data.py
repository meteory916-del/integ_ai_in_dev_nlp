import pytest
from app.schemas import ClassifyRequest, ClassifyResponse

def test_valid_request():
    """Test valid request creation"""
    request = ClassifyRequest(text="Good product")
    assert request.text == "Good product"
    print("✅ Valid request test passed")

def test_valid_response():
    """Test valid response creation"""
    response = ClassifyResponse(label="POSITIVE", score=0.95)
    assert response.label == "POSITIVE"
    assert response.score == 0.95
    print("✅ Valid response test passed")

def test_response_score_range():
    """Test score is between 0 and 1"""
    response = ClassifyResponse(label="NEGATIVE", score=0.5)
    assert 0.0 <= response.score <= 1.0
    print("✅ Score range test passed")

def test_special_characters():
    """Test special characters in text"""
    request = ClassifyRequest(text="!@#$%^&*()")
    assert len(request.text) > 0
    print("✅ Special characters test passed")

def test_unicode_text():
    """Test unicode characters"""
    request = ClassifyRequest(text="Привет 世界 🌍")
    assert "🌍" in request.text
    print("✅ Unicode test passed")

def test_long_text():
    """Test long text"""
    long_text = "A" * 10000
    request = ClassifyRequest(text=long_text)
    assert len(request.text) == 10000
    print("✅ Long text test passed")
