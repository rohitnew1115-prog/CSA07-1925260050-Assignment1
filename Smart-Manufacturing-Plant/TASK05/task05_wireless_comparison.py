
# TASK 5: Wi-Fi 6 vs Private 5G vs LoRaWAN
# Smart Manufacturing Plant

print("=" * 65)
print(" WIRELESS TECHNOLOGY COMPARISON")
print("=" * 65)

# Technology comparison
technologies = {
    "Wi-Fi 6": {
        "standard": "IEEE 802.11ax",
        "speed": "High",
        "latency": "Low under suitable conditions",
        "mobility": "Good",
        "power": "Moderate",
        "best_use": "Office users, laptops and local wireless access"
    },

    "Private 5G": {
        "standard": "3GPP 5G",
        "speed": "High",
        "latency": "Can support low-latency applications",
        "mobility": "Excellent",
        "power": "Device dependent",
        "best_use": "AGVs and mobile industrial equipment"
    },

    "LoRaWAN": {
        "standard": "LoRaWAN",
        "speed": "Very low",
        "latency": "Not suitable for time-critical control",
        "mobility": "Limited compared with cellular networks",
        "power": "Very low",
        "best_use": "Small sensor readings and environmental monitoring"
    }
}

# Display comparison
for technology, details in technologies.items():
    print(f"\nTECHNOLOGY: {technology}")
    print("-" * 45)

    for feature, value in details.items():
        print(f"{feature.replace('_', ' ').title()}: {value}")

# Manufacturing plant recommendations
print("\n" + "=" * 65)
print(" RECOMMENDED TECHNOLOGY FOR THE PLANT")
print("=" * 65)

recommendations = {
    "Office laptops and users": "Wi-Fi 6",
    "Automated Guided Vehicles (AGVs)": "Private 5G",
    "Low-power environmental sensors": "LoRaWAN",
    "High-speed industrial backbone": "Wired Ethernet / Optical Fiber"
}

for application, technology in recommendations.items():
    print(f"{application}: {technology}")

# AGV information
agv_count = 50

print("\n" + "=" * 65)
print(" AGV CONNECTIVITY ANALYSIS")
print("=" * 65)

print(f"Number of AGVs planned: {agv_count}")
print("Recommended wireless technology: Private 5G")
print("Reason: Supports mobility and managed industrial connectivity.")
print("Final performance must be verified through site testing.")

print("\n" + "=" * 65)
print(" WIRELESS TECHNOLOGY ANALYSIS COMPLETED")
print("=" * 65)
