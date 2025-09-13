# port_scanner.py
# Simple TCP port scanner (beginner-friendly)
import socket
import sys

def scan_port(host, port, timeout=0.5):
    """Return True if port is open on host, False otherwise."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            return s.connect_ex((host, port)) == 0
    except Exception:
        return False

def parse_ports(s):
    """Parse strings like '22,80,100-110' into a list of ints."""
    parts = s.split(',')
    ports = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if '-' in part:
            a, b = part.split('-', 1)
            ports.extend(range(int(a), int(b) + 1))
        else:
            ports.append(int(part))
    return ports

def main():
    # allow optional command-line host and ports, otherwise prompt
    host = sys.argv[1] if len(sys.argv) >= 2 else input("Target host (IP or domain) [127.0.0.1]: ") or "127.0.0.1"
    ports_input = sys.argv[2] if len(sys.argv) >= 3 else input("Ports (e.g. 22,80,443 or 1-1024) [22,80,443]: ") or "22,80,443"

    try:
        ports = parse_ports(ports_input)
    except Exception:
        print("Invalid ports. Use formats like '22,80,443' or '1-100'.")
        sys.exit(1)

    print(f"\nScanning {host} ({len(ports)} ports)...\n")
    open_ports = []
    for p in ports:
        if scan_port(host, p):
            print(f"[+] Port {p} OPEN")
            open_ports.append(p)
        else:
            print(f"[-] Port {p} closed")

    print("\nScan finished.")
    if open_ports:
        print("Open ports:", ", ".join(map(str, open_ports)))
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
