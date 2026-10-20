import json
import pytest
from src.extract import lambda_handler


def test_extract_currency():
   result = lambda_handler({}, None)
   assert result is not None
   assert "date" in result
   assert "eur" in result
   assert "usd" in result["eur"]