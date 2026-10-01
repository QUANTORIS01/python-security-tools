from src import DNSRecord


def format_dns_results(results: list[DNSRecord]) -> str:
    """
    Format DNS lookup results for terminal output.
    """
    if not results:
        return 'No DNS records found.'

    lines = [f"{'DOMAIN':<30} {'TYPE':<8} {'VALUE'}", '-' * 70]
    for result in results:
        lines.append(
            f'{result.domain:<30} '
            f'{result.record_type:<8} '
            f'{result.value}'
        )

    return '\n'.join(lines)
