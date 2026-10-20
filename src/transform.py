import json
from datetime import datetime

def lambda_handler(event, context):
    """Transforms the data to give the required rates against USD.

    The output should include the reverse rate to 6 decimal places.

    Args:
        event: a dictionary in the form output by the extract function.
        context: supplied by AWS

    Returns:
        dictionary e.g. {
            "eur": {
                "rate": 1.08167213,
                "reverse_rate": 0.924495
            }
        }

    """
    
    if "body" in event:
        event = json.loads(event["body"])
    date = event.get("date")
    rates= event.get("eur", {})
    transformed = {}
    for currency, rate in rates.items():
        if currency == "eur":
            continue
        if rate == 0:
            continue

        transformed[currency.lower()] = {
            "rate": round(rate, 6),
            "reverse_rate": round(1/ rate, 6)
        }

    return {
        "date": date,
        "base": "eur",
        "currencies": transformed
    }
