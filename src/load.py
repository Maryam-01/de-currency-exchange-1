import json
import boto3
import os
from datetime import datetime

s3 = boto3.client("s3")

def lambda_handler(event, context):
    """
    Receives transformed currency data and stores it in S3
    using a date-partitioned folder structure.
    """


    # replace this code
    # Get today's date (UTC)
    BUCKET_NAME = os.environ["BUCKET_NAME"]
    today = datetime.utcnow()

    year = today.strftime("%Y")
    month = today.strftime("%m")
    day = today.strftime("%d")

    # Build S3 key (folder path)
    key = (
        f"currency-exchange/"
        f"year={year}/"
        f"month={month}/"
        f"day={day}/"
        f"rates.json"
    )

    # Upload to S3
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=json.dumps(event),
        ContentType="application/json"
    )

    return {
        "message": "Data successfully written to S3",
        "s3_key": key
        }




