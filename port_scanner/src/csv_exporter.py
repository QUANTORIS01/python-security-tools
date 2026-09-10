import csv


def export_csv(data: dict, filename: str) -> None:
    """
    Export scan results to a CSV file.
    """
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["port", "service", "banner"])
        for item in data["open_ports"]:
            writer.writerow([item["port"], item["service"], item.get("banner")])
