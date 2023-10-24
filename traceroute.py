from scapy.all import *
from pymongo import MongoClient


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

# Run the trace_route function
trace_route(target_ips, ttl_range, destination_port)

'''
if __name__ == "__main__":
    target_ip = "10.0.0.0/8" # campus IP
    tracerout(target_ip)
'''
# MongoDB connection function
def mongo_client():
    db_username = "foster4ware"
    db_password = "yHCak8ay6pgiY8cC"
    uri = f"mongodb+srv://{db_username}:{db_password}@ipdb.rolcyvs.mongodb.net/"

    # Create a new client and connect to the server
    client = MongoClient(uri)

    # Use a specific database (replace 'traceroute_db' with your desired database name)
    db = client.traceroute_db

    # Create or use a collection for storing traceroute results
    collection = db.traceroute_results

    return collection


if __name__ == "__main":
    # Run the trace_route function
    results = trace_route(target_ips, ttl_range, destination_port)

    # Establish a MongoDB connection
    collection = mongo_client()

    # Insert the traceroute results into MongoDB
    for result in results:
        collection.insert_one(result)

    print("Traceroute results inserted into MongoDB.")