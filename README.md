net_scanner
A lightweight network security scanner implemented in Python, developed as a portfolio project demonstrating practical cybersecurity skills.
Overview
This tool performs basic network reconnaissance by scanning a target host for open TCP ports and identifying the services running on them. It generates a structured report summarizing the findings.
Project Structure
net_scanner/
├── scanner/
│   ├── port_scanner.py      # TCP port scanning
│   ├── service_detector.py  # Service identification
│   └── reporter.py          # Report generation
├── reports/                 # Scan reports saved here
├── main.py                  # Entry point
└── README.md
How It Works

The user provides a target IP address
The scanner attempts a TCP connection on each port from 1 to 1024
Open ports are identified and matched to known services
A report is generated and saved to the reports/ directory

Technical Details
Port Scanning
Each port is tested using a TCP socket connection via Python's built-in socket module. A timeout of 1 second is applied per port to avoid indefinite blocking. If the connection returns 0, the port is open.
Service Detection
Open ports are matched against a dictionary of well-known port-to-service mappings (e.g. port 22 → SSH, port 80 → HTTP). Unknown ports are labeled accordingly.
Report Generation
Reports include the target host, scan timestamp, and a list of open ports with their associated services. Reports are saved as .txt files in the reports/ directory.
Usage
bashcd net_scanner
source venv/bin/activate
python3 main.py
When prompted, enter the target IP address (e.g. 127.0.0.1 for localhost).
Example Output
========================================
Network Security Scan Report
Host: 127.0.0.1
Date: 2026-03-16 15:18:49
========================================
Found 1 open port(s):
  Port 631: IPP (Printing)
========================================
Report saved to reports/scan_127.0.0.1.txt
Security Notice
This tool is intended for use on your own systems or systems you have explicit permission to scan. Unauthorized port scanning may be illegal.
Motivation
This project complements the crypto_lab repository by demonstrating practical network security skills alongside the theoretical cryptographic foundations developed there. Together, they reflect an approach to cybersecurity that bridges mathematical understanding with real-world application.
