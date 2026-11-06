
# TASK 2: Collision Domains and Broadcast Domains

print("=" * 50)
print(" NETWORK DOMAINS AND STANDARDS")
print("=" * 50)

# Network device information
devices = {
    "Hub": {
        "collision_domains": 1,
        "broadcast_domains": 1
    },
    "Switch (without VLANs)": {
        "collision_domains": 8,
        "broadcast_domains": 1
    },
    "Router (2 interfaces)": {
        "collision_domains": 2,
        "broadcast_domains": 2
    }
}

for device, domains in devices.items():
    print(f"\nDevice: {device}")
    print(f"Collision Domains: {domains['collision_domains']}")
    print(f"Broadcast Domains: {domains['broadcast_domains']}")

print("\n" + "=" * 50)
print(" IMPORTANT NETWORK STANDARDS")
print("=" * 50)

standards = {
    "IEEE 802.3": "Ethernet wired networking",
    "IEEE 802.11": "Wireless LAN (Wi-Fi)",
    "IEEE 802.1Q": "VLAN tagging",
    "IEEE 802.1D": "Spanning Tree Protocol"
}

for standard, purpose in standards.items():
    print(f"{standard}: {purpose}")

print("\nTask 2 analysis completed.")
