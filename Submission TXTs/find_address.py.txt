import ipaddress

network = ipaddress.IPv4Network("10.0.0.0/8")

f = open("ipaddresses.txt", "a")
f.write("10.0.0.0")

for ip in network:
    f.write(str(ip + 8)) 
    f.write("/n") 

f.close()