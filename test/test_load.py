from unittest.mock import patch
from src.load import lambda_handler
import boto3
import os

@patch("src.load.s3.put_object")
def test_load(mock_put_object):

    os.environ["BUCKET_NAME"] = "test-bucket"

    fake_transformed_data = {
        "date": "2026-07-20",
        "base": "eur",
        "currencies": {
            "usd": {
                "rate": 1.2,
                "reverse_rate": 0.833333
            }
        }
    }

    result = lambda_handler(fake_transformed_data, None)

    # ✅ Check S3 was called
    mock_put_object.assert_called_once()

    # ✅ Check return message
    assert result["message"] == "Data successfully written to S3"