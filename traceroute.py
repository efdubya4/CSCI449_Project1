from scapy.all import IP, UDP

# Function to trace route to a list of target IPs

def traceroute(destination, max_hops=30, dst_port=33434):
    output = []
    for ttl in range(1, max_hops + 1):
        packet = IP(dst=destination, ttl=ttl) / UDP(dport=dst_port)
        reply = sr1(packet, verbose=0, timeout=1)

        if reply is not None:
            output.append(reply.src)

        if reply is not None and reply.src == destination:
            print(f"Reached destination: {destination}")
            return output

    return output

def check_ip(ip):
    return ip.startswith(("10.", "138.238", "66."))

def ip_increment(ip, dif, increments=1):

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
