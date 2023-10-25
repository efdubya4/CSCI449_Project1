import boto3
from botocore.exceptions import NoCredentialsError
from scapy.all import IP, UDP, sr1
from tqdm import tqdm
import sys

# Initialize
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ipAddresses')
print(table.creation_date_time)

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

def multi_traceroute(destination, max_num_of_hops, count):
    ip = destination
    with table.batch_writer() as batch: 
        batch.put_item =  (Item={ 'ipAddress' = "0", "edge" = "test",})
        # for m in range(count):
        #     output = traceroute(ip, max_num_of_hops)
        #     print(output)
        #     for i, edge in enumerate(output):
        #         if edge:
        #             item = {
        #                 'ip': edge,
        #                 'edges': []
        #             }
        #             print(item)
        #             if i != 0 and ip_is_valid(output[i - 1]):
        #                 item['edges'].append(output[i - 1])
        #             if i != len(output) - 1 and ip_is_valid(output[i + 1]):
        #                 item['edges'].append(output[i + 1])
        #             batch.put_item(Item=item)
        #     ip = ip_increment(ip, 8)

def ip_is_valid(ip):
    return ip.startswith(("10.", "138.238.", "66."))

if __name__ == '__main__':
    destination = "10.0.0.0/8"
    max_num_of_hops = 30  
    count = 328  
    multi_traceroute(destination, max_num_of_hops, count)
