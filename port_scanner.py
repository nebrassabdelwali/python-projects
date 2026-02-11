import socket
import argparse
from datetime import datetime


def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            return True
        return False

    except socket.gaierror:
        print("Hostname could not be resolved.")
        return False
    except socket.error:
        print("Couldn't connect to server.")
        return False


def main():
    parser = argparse.ArgumentParser(description="Simple TCP Port Scanner")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("--start", type=int, default=1, help="Start port")
    parser.add_argument("--end", type=int, default=1024, help="End port")

    args = parser.parse_args()

    print(f"\nScanning target: {args.target}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    for port in range(args.start, args.end + 1):
        if scan_port(args.target, port):
            print(f"[OPEN] Port {port}")

    print("-" * 50)
    print("Scan completed.")


if __name__ == "__main__":
    main()
