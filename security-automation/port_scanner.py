import socket
from datetime import datetime


def validate_port_range(start_port: int, end_port: int) -> bool:
    if start_port < 1 or end_port > 65535:
        print("[SCANNER] Error: Port numbers must be between 1 and 65535.")
        return False
    if start_port > end_port:
        print("[SCANNER] Error: Start port must be less than or equal to end port.")
        return False
    return True


def scan_ports(host: str, start_port: int, end_port: int) -> None:
    if not validate_port_range(start_port, end_port):
        return

    print(f"[SCANNER] Starting scan on {host}")
    print(f"[SCANNER] Port range: {start_port}-{end_port}")
    print(f"[SCANNER] Timestamp: {datetime.now()}")
    print("-" * 50)

    try:
        target_ip = socket.gethostbyname(host)
        print(f"[SCANNER] Resolved {host} to {target_ip}")
    except socket.gaierror:
        print("[SCANNER] Error: Hostname could not be resolved.")
        return

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((host, port))

            if result == 0:
                print(f"Port {port}: OPEN")
            else:
                print(f"Port {port}: CLOSED")

            sock.close()

        except KeyboardInterrupt:
            print("\n[SCANNER] Scan stopped by user.")
            return
        except Exception as error:
            print(f"[SCANNER] Error scanning port {port}: {error}")

    print("-" * 50)
    print("[SCANNER] Scan complete.")


if __name__ == "__main__":
    print("Authorized targets only: 127.0.0.1 or scanme.nmap.org")
    host = input("Enter target host: ").strip()
    start_port = int(input("Enter start port: ").strip())
    end_port = int(input("Enter end port: ").strip())

    if host not in ["127.0.0.1", "localhost", "scanme.nmap.org"]:
        print("[SCANNER] Error: Unauthorized target. Use only localhost or scanme.nmap.org.")
    else:
        scan_ports(host, start_port, end_port)