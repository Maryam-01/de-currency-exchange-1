import requests
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



def lambda_handler(event, context):
    primary_url = (
        "https://cdn.jsdelivr.net/npm/"
        "@fawazahmed0/currency-api@latest/v1/currencies/eur.json"
    )

    fallback_url = (
        "https://latest.currency-api.pages.dev/"
        "v1/currencies/eur.json"
    )

    try:
        response = requests.get(primary_url, timeout=10)
        response.raise_for_status()
        return response.json()

    except Exception:
        response = requests.get(fallback_url, timeout=10)
        response.raise_for_status()
        return response.json()