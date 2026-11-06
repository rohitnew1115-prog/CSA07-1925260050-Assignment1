
# TASK 9: Sliding Window Protocol, ARQ and Network Utilisation

print("=" * 60)
print(" SLIDING WINDOW AND ARQ ANALYSIS")
print("=" * 60)


# PART 1: STOP-AND-WAIT ARQ

print("\n1. STOP-AND-WAIT ARQ SIMULATION")

total_frames = 5

for frame in range(1, total_frames + 1):
    print(f"\nSender: Sending Frame {frame}")
    print(f"Receiver: Frame {frame} received successfully")
    print(f"Receiver: Sending ACK {frame}")
    print(f"Sender: ACK {frame} received")


# PART 2: SLIDING WINDOW PROTOCOL

print("\n" + "=" * 60)
print("2. SLIDING WINDOW PROTOCOL")

total_frames = 10
window_size = 4

base = 0

while base < total_frames:

    end = min(base + window_size, total_frames)

    print(f"\nCurrent Window: Frames {base + 1} to {end}")

    for frame in range(base, end):
        print(f"Sender: Sending Frame {frame + 1}")

    print(f"Receiver: Acknowledging Frames {base + 1} to {end}")

    base = end

print("\nAll frames transmitted successfully.")


# PART 3: NETWORK UTILISATION

print("\n" + "=" * 60)
print("3. NETWORK UTILISATION CALCULATION")

transmission_delay = float(
    input("Enter transmission delay (ms): ")
)

propagation_delay = float(
    input("Enter one-way propagation delay (ms): ")
)

window_size = int(
    input("Enter sliding window size: ")
)

if transmission_delay <= 0 or propagation_delay < 0 or window_size < 1:
    print("Invalid input. Check the delay and window values.")

else:
    a = propagation_delay / transmission_delay

    utilisation = min(1, window_size / (1 + 2 * a))

    print(f"\nPropagation ratio (a): {a:.3f}")
    print(f"Window size: {window_size}")
    print(f"Link utilisation: {utilisation * 100:.2f}%")

    print("\nEfficiency Analysis:")

    if utilisation >= 1:
        print("The sliding window can fully utilise the link.")
    else:
        print("The link is not fully utilised.")
        print("Increasing the window size may improve utilisation.")


print("\n" + "=" * 60)
print(" TASK 9 COMPLETED")
print("=" * 60)
