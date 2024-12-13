from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        
        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Protocol: {protocol}")
        
        # Check for TCP or UDP payloads
        if TCP in packet or UDP in packet:
            print(f"Payload: {bytes(packet[IP].payload)}")
        print("-" * 50)

# Sniff packets on the network interface
def start_sniffer(interface):
    print(f"Starting packet capture on interface: {interface}")
    sniff(iface=interface, prn=packet_callback, store=False)

if __name__ == "__main__":
    # Replace 'eth0' with the name of your network interface
    interface = input("Enter the network interface (e.g., eth0, wlan0): ")
    start_sniffer(interface)
