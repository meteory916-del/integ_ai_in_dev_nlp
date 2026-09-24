import pytest
from schemas import ClassifyRequest, ClassifyResponse
from pydantic import ValidationError

def test_valid_request():
    request = ClassifyRequest(text="test")
    assert request.text == "test"

def test_valid_response():
    response = ClassifyResponse(label="POSITIVE", score=0.95)
    assert response.label == "POSITIVE"

def test_score_range():
    response = ClassifyResponse(label="NEGATIVE", score=0.5)
    assert 0.0 <= response.score <= 1.0

def test_empty_text():
    with pytest.raises(ValidationError):
        ClassifyRequest(text="")

def test_special_chars():
    request = ClassifyRequest(text="!@#")
    assert len(request.text) > 0

def test_unicode():
    request = ClassifyRequest(text="test")
    assert len(request.text) > 0

def test_long_text():
    request = ClassifyRequest(text="A" * 10000)
    assert len(request.text) == 10000
