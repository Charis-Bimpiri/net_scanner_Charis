from scanner.port_scanner import scan_host
from scanner.service_detector import detect_service
from scanner.reporter import generate_report, save_report

def main():
    host = input("Enter host to scan: ")
    print(f"\nScanning {host}...")
    
    open_ports = scan_host(host)
    services = {port: detect_service(port) for port in open_ports}
    
    report = generate_report(host, open_ports, services)
    print(report)
    
    filename = save_report(report, host)
    print(f"\nReport saved to {filename}")

if __name__ == "__main__":
    main()
