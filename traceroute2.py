from scapy.all import *
from pymongo import MongoClient

# Define a list of target IP address ranges
private_ip_range = "10.0.0.0/8"
public_ip_range = "138.238.0.0/16"

# Modify TTL range and destination port as necessary
ttl_range = range(1, 28)  # Adjust the TTL range
destination_port = 33434  # Adjust the destination port if needed

# Function to trace route to a list of target IPs
def trace_route(target_ips, ttl_range, destination_port):
    for ipaddr in target_ips:
        print(f"Tracing route to {ipaddr}:")

        for ttl in ttl_range:
            pkt = IP(dst=ipaddr, ttl=ttl) / UDP(dport=destination_port)
            reply = sr1(pkt, verbose=0, timeout=1)  # Adjust the timeout as needed

            if reply is None:
                print(f"{ttl} hops away: No reply")
            elif reply.type == 3:
                print(f"Done! {ipaddr} reached at {reply.src}")
                break
            else:
                print(f"{ttl} hops away: {reply.src}")

        print("\n")

# Function to generate a list of IP addresses in a given range
def generate_ip_addresses(ip_range):
    ip_addresses = [str(ip) for ip in IP(ip_range)]
    return ip_addresses

if __name__ == "__main":
    # Generate a list of private IP addresses
    private_ip_addresses = generate_ip_addresses(private_ip_range)
    trace_route(private_ip_addresses, ttl_range, destination_port)

    # Generate a list of public IP addresses
    public_ip_addresses = generate_ip_addresses(public_ip_range)
    trace_route(public_ip_addresses, ttl_range, destination_port)
