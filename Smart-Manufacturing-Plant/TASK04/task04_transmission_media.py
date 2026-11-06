
# TASK 4: Transmission Media, Nyquist and Shannon Theorems

import math

print("=" * 60)
print(" TRANSMISSION MEDIA AND CHANNEL CAPACITY ANALYSIS")
print("=" * 60)

# Part 1: Transmission Media Comparison

print("\n1. TRANSMISSION MEDIA COMPARISON")

media = {
    "Twisted Pair Cable": "Low cost, suitable for short-distance Ethernet",
    "Coaxial Cable": "Good shielding and resistance to interference",
    "Optical Fiber": "High bandwidth, long distance, immune to electromagnetic interference",
    "Wireless": "Flexible connectivity without physical cables"
}

for name, description in media.items():
    print(f"\n{name}:")
    print(description)

print("\nRecommended media for the manufacturing plant:")
print("Optical fiber for backbone connections near electrically noisy areas.")
print("Shielded Ethernet cabling for suitable short-distance connections.")

# Part 2: Nyquist Theorem

print("\n" + "=" * 60)
print("2. NYQUIST THEOREM")
print("=" * 60)

bandwidth = float(input("Enter channel bandwidth in Hz: "))
levels = int(input("Enter number of signal levels: "))

if bandwidth <= 0 or levels < 2:
    print("Invalid input. Bandwidth must be positive and levels must be at least 2.")
else:
    nyquist_rate = 2 * bandwidth * math.log2(levels)

    print(f"Maximum Nyquist Bit Rate: {nyquist_rate:.2f} bits/second")

# Part 3: Shannon Theorem

print("\n" + "=" * 60)
print("3. SHANNON CAPACITY THEOREM")
print("=" * 60)

shannon_bandwidth = float(input("Enter channel bandwidth in Hz: "))
snr_db = float(input("Enter Signal-to-Noise Ratio (SNR) in dB: "))

if shannon_bandwidth <= 0:
    print("Invalid bandwidth. It must be positive.")
else:
    snr_linear = 10 ** (snr_db / 10)

    shannon_capacity = (
        shannon_bandwidth * math.log2(1 + snr_linear)
    )

    print(f"Linear SNR: {snr_linear:.4f}")
    print(f"Maximum Shannon Capacity: {shannon_capacity:.2f} bits/second")

print("\n" + "=" * 60)
print(" TRANSMISSION MEDIA ANALYSIS COMPLETED")
print("=" * 60)
