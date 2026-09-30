import json

from src import export_json


def test_export_json_creates_file(tmp_path):
    output_file = tmp_path / "results.json"
    data = {
        "target": "127.0.0.1",
        "open_ports": [80, 443]
    }
    export_json(data, str(output_file))
    assert output_file.exists()


def test_export_json_content(tmp_path):
    output_file = tmp_path / "results.json"
    data = {
        "target": "127.0.0.1",
        "open_ports": [80, 443]
    }
    export_json(data, str(output_file))

    with open(output_file, "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
    assert loaded_data == data
