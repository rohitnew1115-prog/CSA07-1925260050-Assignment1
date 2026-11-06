
# TASK 3: Frame Analysis and OSI Encapsulation

print("=" * 55)
print(" DATA ENCAPSULATION IN COMPUTER NETWORKS")
print("=" * 55)

# Original application data
data = "Hello Smart Manufacturing Plant"

print("\n1. APPLICATION LAYER")
print("Original Data:", data)

# Transport Layer
transport_segment = (
    "TCP HEADER [Source Port: 5000, Destination Port: 80] "
    + data
)
print("\n2. TRANSPORT LAYER")
print("TCP Segment:", transport_segment)

# Network Layer
network_packet = (
    "IP HEADER [Source: 192.168.1.10, Destination: 192.168.1.20] "
    + transport_segment
)
print("\n3. NETWORK LAYER")
print("IP Packet:", network_packet)

# Data Link Layer
ethernet_frame = (
    "ETHERNET HEADER [Source MAC: AA:BB:CC:DD:EE:01, "
    "Destination MAC: AA:BB:CC:DD:EE:02] "
    + network_packet
    + " [FCS: CHECK]"
)
print("\n4. DATA LINK LAYER")
print("Ethernet Frame:", ethernet_frame)

# Physical Layer
binary_data = " ".join(format(ord(char), "08b") for char in ethernet_frame)

print("\n5. PHYSICAL LAYER")
print("Transmitted Bits (first 100 bits):")
print(binary_data[:100])

print("\n" + "=" * 55)
print(" ENCAPSULATION COMPLETED")
print("=" * 55)
