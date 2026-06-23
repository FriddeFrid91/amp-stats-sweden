import json
from pathlib import Path
import requests


BASE_URL = (
    "https://sdb.socialstyrelsen.se/api/v1/sv/"
    "operationerislutenvard"
)

PROJECT_ROOT = Path(__file__).resolve().parents[1]

CONFIG_PATH = (
    PROJECT_ROOT
    / "config"
    / "amputation_groups.json"
)


def load_amputation_groups() -> dict:
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_json(url: str) -> object:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.json()


def main() -> None:
    operations = get_json(f"{BASE_URL}/operation")

    output_path = Path("data/raw/operations.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(
            operations,
            file,
            ensure_ascii=False,
            indent=2,
        )

    print("Operationskoder sparade i data/raw/operations.json")
    print("\nTräffar som innehåller 'amput':")

    if isinstance(operations, list):
        for operation in operations:
            operation_text = json.dumps(
                operation,
                ensure_ascii=False,
            ).lower()

            if "amput" in operation_text:
                print(json.dumps(
                    operation,
                    ensure_ascii=False,
                    indent=2,
                ))


if __name__ == "__main__":
    main()
