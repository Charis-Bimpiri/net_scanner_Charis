import socket

def scan_port(host, port, timeout=1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            return True
        return False
    except socket.error:
        return False

def scan_host(host, start_port=1, end_port=1024):
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            open_ports.append(port)
    return open_ports
