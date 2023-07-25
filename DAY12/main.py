import argparse
import socket
import sys

def check_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            return "Open"
        else:
            return "Closed"
    except:
        return "Error"

def port_scan(host, start_port, end_port, filename=None):
    result = {}
    for port in range(start_port, end_port+1):
        status = check_port(host, port)
        result[port] = status

    if filename:
        with open(filename, "w") as f:
            for port, status in result.items():
                f.write("Port {}: {}\n".format(port, status))

    for port, status in result.items():
        print("Port {}: {}".format(port, status))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument("host", help="Host to scan")
    parser.add_argument("start_port", type=int, help="Start port")
    parser.add_argument("end_port", type=int, help="End port")
    parser.add_argument("-o", "--output", help="Output file name")
    args = parser.parse_args()

    host = args.host
    start_port = args.start_port
    end_port = args.end_port
    filename = args.output

    port_scan(host, start_port, end_port, filename)
