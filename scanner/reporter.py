from datetime import datetime

def generate_report(host, open_ports, services):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    lines = []
    lines.append("=" * 40)
    lines.append(f"Network Security Scan Report")
    lines.append(f"Host: {host}")
    lines.append(f"Date: {timestamp}")
    lines.append("=" * 40)
    
    if not open_ports:
        lines.append("No open ports found.")
    else:
        lines.append(f"Found {len(open_ports)} open port(s):")
        for port in open_ports:
            service = services.get(port, "Unknown")
            lines.append(f"  Port {port}: {service}")
    
    lines.append("=" * 40)
    return "\n".join(lines)

def save_report(report, host):
    filename = f"reports/scan_{host}.txt"
    with open(filename, "w") as f:
        f.write(report)
    return filename
