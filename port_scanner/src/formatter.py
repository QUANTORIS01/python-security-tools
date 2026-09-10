from src import ScanResult


def format_scan_results(results: list[ScanResult], max_banner_length: int = 40) -> str:
    """
    Format scan results for terminal output.
    """
    if not results:
        return "No open ports found."
    lines = [f"{'PORT':<8} {'STATUS':<8} {'SERVICE':<16} {'BANNER'}", "-" * 70]
    for result in results:
        banner = result.banner or "-"
        if len(banner) > max_banner_length:
            banner = banner[: max_banner_length - 3] + "..."
        lines.append(f"{result.port:<8} {'OPEN':<8} {result.service:<16} {banner}")

    return "\n".join(lines)
