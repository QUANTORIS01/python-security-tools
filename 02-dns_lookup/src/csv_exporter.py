import csv


def export_csv(data: dict, filename: str) -> None:
    """
    Export DNS results to a CSV file.
    """
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['domain', 'record_type', 'value'])
        for item in data['records']:
            writer.writerow([item['domain'], item['record_type'], item['value']])
