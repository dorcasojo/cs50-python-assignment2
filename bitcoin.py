import os
import sys

import requests

API_URL = "https://rest.coincap.io/v3/assets/bitcoin"


def get_amount():
    """Read and validate the number of Bitcoins from the command line."""
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    try:
        return float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")


def get_price():
    """Return the current Bitcoin price in USD as a float."""
    api_key = os.environ.get("COINCAP_API_KEY", "")
    try:
        response = requests.get(API_URL, params={"apiKey": api_key}, timeout=10)
        response.raise_for_status()  # turns HTTP errors (401, 500...) into exceptions
        return float(response.json()["data"]["priceUsd"])
    except (requests.RequestException, KeyError, ValueError):
        sys.exit("Could not retrieve the Bitcoin price")


def main():
    amount = get_amount()  
    cost = amount * get_price()
    print(f"${cost:,.4f}")


if __name__ == "__main__":
    main()

