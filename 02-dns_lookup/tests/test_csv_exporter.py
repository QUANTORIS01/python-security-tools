import csv

from src import export_csv


def test_export_csv_creates_file(tmp_path):
    output_file = (tmp_path / 'results.csv')
    data = {
        'records': [{
            'domain': 'google.com',
            'record_type': 'A',
            'value': '8.8.8.8',
        }]
    }
    export_csv(data, str(output_file))
    assert output_file.exists()


def test_export_csv_content(tmp_path):
    output_file = (tmp_path / 'results.csv')
    data = {
        'records': [{
            'domain': 'google.com',
            'record_type': 'A',
            'value': '8.8.8.8',
        }, {
            'domain': 'google.com',
            'record_type': 'MX',
            'value': 'smtp.google.com',
        }]
    }
    export_csv(data, str(output_file))
    with open(output_file, 'r', newline='', encoding='utf-8') as file:
        rows = list(csv.reader(file))
    assert rows == [[
        'domain',
        'record_type',
        'value',
    ], [
        'google.com',
        'A',
        '8.8.8.8',
    ], [
        'google.com',
        'MX',
        'smtp.google.com',
    ], ]
