import argparse
import sys
import time

from src import (
    scan_range, validate_ip, validate_port_range, validate_timeout, validate_workers, export_json, export_csv,
    setup_logger, build_scan_results, format_scan_results
)


def create_parser() -> argparse.ArgumentParser:
    """
    Create the command-line argument parser.
    """
    parser = argparse.ArgumentParser(description="TCP Port Scanner")
    parser.add_argument("ip", type=str, help="Target IPv4 address")
    parser.add_argument("start_port", type=int, help="Starting port number")
    parser.add_argument("end_port", type=int, help="Ending port number")
    parser.add_argument("-t", "--timeout", type=float, default=0.5, help="Connection timeout in seconds (default: 0.5)")
    parser.add_argument("-w", "--workers", type=int, default=100, help="Number of concurrent workers (default: 100)")
    parser.add_argument("--json", dest="json_file", type=str, help="Export results to a JSON file")
    parser.add_argument("--csv", dest="csv_file", type=str, help="Export results to a CSV file")
    return parser


def main() -> None:
    """
    Run the port scanner CLI.
    """
    parser = create_parser()
    args = parser.parse_args()
    if not validate_ip(args.ip):
        print(f"❌ Invalid IP address: {args.ip}")
        sys.exit(1)
    if not validate_port_range(args.start_port, args.end_port):
        print("❌ Invalid port range.")
        sys.exit(1)
    if not validate_timeout(args.timeout):
        print("❌ Timeout must be greater than 0.")
        sys.exit(1)

    if not validate_workers(args.workers):
        print("❌ Workers must be greater than 0.")
        sys.exit(1)
    logger = setup_logger("scan.log")
    print()
    print(f"🔍 Scanning {args.ip}")
    print(f"Port range: {args.start_port}-{args.end_port}")
    print(f"Timeout: {args.timeout}s")
    print(f"Workers: {args.workers}")
    print()
    start_time = time.perf_counter()
    logger.info("Scan started target=%s ports=%s-%s", args.ip, args.start_port, args.end_port)
    open_ports = scan_range(args.ip, args.start_port, args.end_port, timeout=args.timeout, workers=args.workers)
    results = build_scan_results(args.ip, open_ports, timeout=args.timeout)
    logger.info("Scan completed open_ports=%s", len(open_ports))
    elapsed_time = time.perf_counter() - start_time
    print("-" * 70)
    print(format_scan_results(results))
    print("-" * 70)
    print(f"Scan completed in {elapsed_time:.2f}s")
    print(f"Open ports found: {len(open_ports)}")
    export_data = {"target": args.ip, "start_port": args.start_port, "end_port": args.end_port, "open_ports": [
        {
            "port": result.port,
            "service": result.service,
            "banner": result.banner,
        } for result in results
    ]}
    if args.json_file:
        export_json(export_data, args.json_file)
        print(f"Results exported to {args.json_file}")

    if args.csv_file:
        export_csv(export_data, args.csv_file)
        print(f"Results exported to {args.csv_file}")


if __name__ == "__main__":
    main()
