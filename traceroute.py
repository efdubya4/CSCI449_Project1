from scapy.all import *

# Define a list of target IP addresses to trace
target_ips = ["10.0.0.1"]  # Add more IP addresses as needed

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

def ip_increment(ip, dif, increments=1):
    # Increment IP Address by dif

    ip = [int(x) for x in ip.split('.')]

    total_ip = ip[3] + ip[2] * 255 + ip[1] * (255 ** 2)

    for i in range(increments):
        ip[3] += dif

        if ip[3] >= 256:
            ip[2] += 1
            ip[3] = ip[3] % 256
        
        if ip[2] == 256:
            ip[1] += 1
            ip[2] = 0

    ip = [str(x) for x in ip]

    ip = '.'.join(ip)
        
    return ip

# Run the trace_route function
trace_route(target_ips, ttl_range, destination_port)

'''
if __name__ == "__main__":
    target_ip = "10.0.0.0/8" # campus IP
    traceroute(target_ip)
'''
