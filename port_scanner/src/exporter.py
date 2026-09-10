import json


def export_json(data: dict, filename: str) -> None:
    """
    Export scan results to a JSON file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)