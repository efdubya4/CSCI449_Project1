import random
import ipaddress

def generate_random_ip_addresses(ip_range, num_addresses):
    try:
        network = ipaddress.IPv4Network(ip_range, strict=False)
        legal_ips = []
        for _ in range(num_addresses):
            legal_ip = ipaddress.IPv4Address(random.randint(int(network.network_address), int(network.broadcast_address)))
            legal_ips.append(str(legal_ip))
        return legal_ips
    except ValueError:
        print("Invalid IP range")
        return []

def save_ips_to_file(ip_addresses, filename):
    with open(filename, 'w') as file:
        for ip in ip_addresses:
            file.write(ip + '\n')

# Specify the IP range and the number of addresses to generate
ip_range = "10.0.0.0/8"
num_addresses = 20

random_ips = generate_random_ip_addresses(ip_range, num_addresses)
if random_ips:
    filename = "random_ip_addresses.txt"
    save_ips_to_file(random_ips, filename)

