# simple-domain-check.py

import socket

def check_domain(domain):
    try:
        socket.gethostbyname(domain)
        return False  # domain resolves, so probably taken
    except socket.gaierror:
        return True  # domain does not resolve, likely available

if __name__ == "__main__":
    with open('domains.txt', 'r') as f:
        domains = [line.strip() for line in f if line.strip()]

    for domain in domains:
        if check_domain(domain):
            print(f"✅ Available: {domain}")
        else:
            print(f"❌ Taken: {domain}")
