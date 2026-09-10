import csv

from src import export_csv


def test_export_csv_creates_file(tmp_path):
    output_file = tmp_path / "results.csv"
    data = {
        "target": "127.0.0.1",
        "open_ports": [
            {
                "port": 80,
                "service": "http",
            },
            {
                "port": 443,
                "service": "https",
            },
        ],
    }
    export_csv(data, str(output_file))
    assert output_file.exists()


def test_export_csv_content(tmp_path):
    output_file = tmp_path / "results.csv"
    data = {
        "target": "127.0.0.1",
        "open_ports": [
            {
                "port": 80,
                "service": "http",
                "banner": "HTTP/1.1 200 OK",
            },
            {
                "port": 443,
                "service": "https",
                "banner": "HTTPS Server",
            },
        ],
    }
    export_csv(data, str(output_file))

    with open(output_file, "r", newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))
    assert rows == [
        ["port", "service", "banner"],
        ["80", "http", "HTTP/1.1 200 OK"],
        ["443", "https", "HTTPS Server"],
    ]
