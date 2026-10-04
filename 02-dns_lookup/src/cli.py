import argparse
import sys

from src import (
    validate_domain,
    validate_record_type,
    build_dns_results,
    format_dns_results,
    export_json,
    export_csv,
    setup_logger,
)

from .exception import DNSTimeoutError


def create_parser() -> argparse.ArgumentParser:
    """
    Create command-line argument parser.
    """
    parser = argparse.ArgumentParser(description='DNS Lookup Tool')
    parser.add_argument('domain', type=str, help='Target domain name')
    parser.add_argument('record_type', type=str, help='DNS record type')
    parser.add_argument('--json', dest='json_file', type=str, help='Export results to JSON')
    parser.add_argument('--csv', dest='csv_file', type=str, help='Export results to CSV')
    return parser


def main() -> None:
    """
    Run DNS lookup CLI.
    """
    parser = create_parser()
    args = parser.parse_args()
    if not validate_domain(args.domain):
        print(f'❌ Invalid domain: {args.domain}')
        sys.exit(1)
    if not validate_record_type(args.record_type):
        print(f'❌ Invalid record type: {args.record_type}')
        sys.exit(1)
    logger = setup_logger('dns.log')
    logger.info('Lookup started domain=%s type=%s', args.domain, args.record_type)
    try:
        results = build_dns_results(args.domain, args.record_type)
    except DNSTimeoutError:
        print('❌ DNS query timed out.')
        sys.exit(1)
    logger.info('Lookup completed records=%s', len(results))
    print(format_dns_results(results))
    export_data = {
        'domain': args.domain,
        'record_type': args.record_type,
        'records': [{
            'domain': result.domain,
            'record_type': result.record_type,
            'value': result.value,
        } for result in results]
    }
    if args.json_file:
        export_json(export_data, args.json_file)
        print(f'Results exported to {args.json_file}')
    if args.csv_file:
        export_csv(export_data, args.csv_file)
        print(f'Results exported to {args.csv_file}')


if __name__ == '__main__':
    main()
