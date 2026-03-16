COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    631: "IPP (Printing)",
    3306: "MySQL",
    5432: "PostgreSQL",
    8080: "HTTP-Alt"
}

def detect_service(port):
    return COMMON_PORTS.get(port, "Unknown")

