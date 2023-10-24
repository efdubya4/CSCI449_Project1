from scapy.all import *

# Define a list of target IP addresses to trace
target_ips = ["10.0.0.1"]  # Add more IP addresses as needed

# Modify TTL range as necessary
ttl_range = range(1, 28)  # Adjust the TTL range

# Function to trace route to a list of target IPs
def trace_route(target_ips, ttl_range):
    for ipaddr in target_ips:
        print(f"Tracing route to {ipaddr}:")

        for ttl in ttl_range:
            pkt = IP(dst=ipaddr, ttl=ttl) / ICMP()
            reply = sr1(pkt, verbose=0, timeout=1)  # Adjust the timeout as needed

            if reply is None:
                print(f"{ttl} hops away: No reply")
            elif reply.type == 0:  # ICMP Echo Reply
                print(f"Done! {ipaddr} reached at {reply.src}")
                break
            else:
                print(f"{ttl} hops away: {reply.src}")

        print("\n")

# Run the trace_route function
trace_route(target_ips, ttl_range)
