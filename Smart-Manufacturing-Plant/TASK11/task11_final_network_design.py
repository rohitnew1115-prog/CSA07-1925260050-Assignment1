
print("=" * 60)
print("SMART MANUFACTURING PLANT - FINAL NETWORK DESIGN")
print("=" * 60)

network_design = {
    "Robot Controllers": {
        "Technology": "Industrial Ethernet",
        "Connection": "Shielded Ethernet / Fiber backbone",
        "Reason": "Reliable and low-latency communication"
    },

    "Vibration Sensors": {
        "Technology": "LoRaWAN / Industrial IoT",
        "Connection": "Wireless sensor gateways",
        "Reason": "Low power and suitable for periodic sensor data"
    },

    "CCTV Cameras": {
        "Technology": "Gigabit Ethernet",
        "Connection": "Managed switches and fiber backbone",
        "Reason": "Supports high-bandwidth video transmission"
    },

    "Office Users": {
        "Technology": "Wi-Fi 6",
        "Connection": "Wireless access points",
        "Reason": "Supports multiple users and high-speed access"
    },

    "Automated Guided Vehicles": {
        "Technology": "Private 5G",
        "Connection": "5G base stations and local 5G core",
        "Reason": "Supports mobility and controlled communication"
    },

    "Head Office": {
        "Technology": "WAN / VPN",
        "Connection": "Secure fiber or service-provider connection",
        "Reason": "Secure communication between distant locations"
    }
}

for device, details in network_design.items():
    print("\n" + device)
    for key, value in details.items():
        print(f"  {key}: {value}")

print("\n" + "=" * 60)
print("NETWORK SECURITY AND RELIABILITY")
print("=" * 60)

measures = [
    "Separate VLANs for robots, sensors, CCTV and office users",
    "Firewalls and access control lists",
    "Quality of Service (QoS) for priority traffic",
    "Redundant network links for critical systems",
    "Network monitoring and regular maintenance",
    "UPS power backup for important network devices"
]

for measure in measures:
    print("-", measure)

print("\nEstimated application bandwidth: 158.24 Mbps")
print("Additional bandwidth capacity should be reserved for growth.")
