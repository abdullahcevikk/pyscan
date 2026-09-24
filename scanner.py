import socket
import sys
from concurrent.futures import ThreadPoolExecutor
import argparse
import random

def scan_single_port(target_ip, target_host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1.0)
        result = s.connect_ex((target_ip, port))

        if result == 0: 
            banner = "No Banner Recieved"
            try:
                if port in [80, 8080]:
                    s.sendall(b"HEAD / HTTP/1.1\r\nHost:" + target_host.encode() +b"\r\n\r\n")
                response = s.recv(1024)
                if response:
                    banner = response.decode(errors="ignore").strip().splitlines()[0]
            except (socket.timeout, socket.error):
                 pass
            
            print(f"[+] Port {port:<5} OPEN | Banner: {banner}")

def parse_ports(port_str):
        try:
            if "-" in port_str:
             start, end = map(int, port_str.split("-"))
             return list(range(start, end + 1))
            return [int(port_str)]
        except ValueError:
            print("[-] Error: Invalid port format! Example: 80 or 1-1024")
            sys.exit(1)

def main(): 
    parser = argparse.ArgumentParser(
    description="Fast Multi-threaded TCP Port Scanner with Banner Grabbing."
    )
    parser.add_argument("-t", "--target", required=True, help="Target domain or IP address")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range (default: 1-1024)")
    parser.add_argument("-w", "--workers", type=int, default=50, help="Number of threads (default: 50)")
    parser.add_argument("-r", "--randomize", action="store_true", help="Randomize port order")

    args = parser.parse_args()

    try:
        target_ip = socket.gethostbyname(args.target)
        print(f"[+]Resolved target: {target_ip} ({args.target})")
    except socket.gaierror: 
        print(f"[-]Could not resolve the hostname: {args.target}")
        sys.exit(1)

    ports = parse_ports(args.ports)

    if args.randomize:
        random.shuffle(ports)
        print("[*] Port order randomized.")

    print(f"[*] Starting scan on {target_ip} ({len(ports)} ports) with {args.workers} workers...\n")

    with ThreadPoolExecutor(max_workers=50) as executor:
        for port in ports:
            executor.submit(scan_single_port, target_ip, args.target, port)

    print("\n[*] Scan completed.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[-] Scan cancelled by user.")
        sys.exit(0)
