
# TASK 8: Hamming Code, FEC and ARQ

print("=" * 60)
print(" HAMMING CODE AND ERROR CONTROL")
print("=" * 60)


# PART 1: HAMMING (7,4) ENCODING

def hamming_encode(data):
    if len(data) != 4 or any(bit not in "01" for bit in data):
        raise ValueError("Enter exactly four binary bits.")

    d1, d2, d3, d4 = map(int, data)

    # Positions: 1  2  3  4  5  6  7
    #            p1 p2 d1 p4 d2 d3 d4

    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p4 = d2 ^ d3 ^ d4

    return [
        p1, p2, d1, p4, d2, d3, d4
    ]


# PART 2: ERROR DETECTION AND CORRECTION

def hamming_correct(received):
    bits = received.copy()

    s1 = bits[0] ^ bits[2] ^ bits[4] ^ bits[6]
    s2 = bits[1] ^ bits[2] ^ bits[5] ^ bits[6]
    s4 = bits[3] ^ bits[4] ^ bits[5] ^ bits[6]

    error_position = s1 + (s2 * 2) + (s4 * 4)

    if error_position != 0:
        bits[error_position - 1] ^= 1

    return bits, error_position


print("\n1. HAMMING CODE - FORWARD ERROR CORRECTION")

data = "1011"

encoded = hamming_encode(data)

print("Original Data:       ", data)
print("Encoded Hamming Code:", "".join(map(str, encoded)))

# Simulate one transmission error
received = encoded.copy()
received[2] ^= 1

print("Received Data:       ", "".join(map(str, received)))

corrected, error_position = hamming_correct(received)

print("Error Position:      ", error_position)
print("Corrected Data:      ", "".join(map(str, corrected)))
print("Recovered Data:      ", "".join(map(str, corrected[2:3] +
                                           corrected[4:7])))


# PART 3: ARQ SIMULATION

print("\n2. AUTOMATIC REPEAT REQUEST (ARQ)")

transmission_attempts = 0
maximum_attempts = 3

acknowledgement_received = False

while transmission_attempts < maximum_attempts:

    transmission_attempts += 1

    print(f"\nTransmission Attempt: {transmission_attempts}")

    # Demonstration: first attempt fails, second succeeds
    if transmission_attempts == 1:
        print("Receiver: Error detected.")
        print("Receiver: NACK - Please retransmit.")
    else:
        print("Receiver: Data received correctly.")
        print("Receiver: ACK - Transmission successful.")
        acknowledgement_received = True
        break

if acknowledgement_received:
    print("\nARQ Status: Successful")
else:
    print("\nARQ Status: Transmission failed")


print("\n" + "=" * 60)
print(" TASK 8 COMPLETED")
print("=" * 60)
