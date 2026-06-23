import json
import requests

BASE_URL = (
    "https://sdb.socialstyrelsen.se/api/v1/sv/"
    "operationerislutenvard"
)

def get_json(url: str) -> object:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.json()

def main() -> None:
    metadata = get_json(BASE_URL)
    print(json.dumps(metadata, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()