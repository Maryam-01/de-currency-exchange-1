import json
import pytest
from datetime import datetime
from src.extract import lambda_handler
from src.transform import lambda_handler


def test_transform():
    fake_extract_output = {
        "date": "2026-07-20",
        "eur": {
            "usd": 1.2,
            "gbp": 0.8,
            "eur": 1
        }
    }
    result = lambda_handler(fake_extract_output, None)
    print(result)
    assert result is not None
    assert result["date"] == "2026-07-20"
    assert result["base"] == "eur"
    assert result["currencies"]["usd"]["rate"] == 1.2
    assert result["currencies"]["usd"]["reverse_rate"] == round(1 / 1.2 , 6)
    assert "usd" in result["currencies"]