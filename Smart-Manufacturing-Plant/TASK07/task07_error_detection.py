
# TASK 7: CRC, Parity and Checksum Error Detection

print("=" * 60)
print(" NETWORK ERROR DETECTION TECHNIQUES")
print("=" * 60)

# Part 1: Parity Check

def calculate_parity(data):
    ones = data.count("1")
    parity_bit = "0" if ones % 2 == 0 else "1"
    return parity_bit

data = "1011011"

print("\n1. PARITY CHECK")
print("Original Data:", data)

parity = calculate_parity(data)
transmitted_data = data + parity

print("Even Parity Bit:", parity)
print("Transmitted Data:", transmitted_data)

# Part 2: Checksum

def calculate_checksum(data):
    total = sum(int(bit) for bit in data)
    checksum = (~total) & 0xFF
    return checksum

print("\n2. CHECKSUM")

binary_data = "10101010"
checksum = calculate_checksum(binary_data)

print("Original Data:", binary_data)
print("Calculated Checksum:", format(checksum, "08b"))

# Part 3: CRC

def crc_remainder(data, generator):
    dividend = list(map(int, data))
    divisor = list(map(int, generator))

    for i in range(len(dividend) - len(divisor) + 1):
        if dividend[i] == 1:
            for j in range(len(divisor)):
                dividend[i + j] ^= divisor[j]

    remainder = "".join(map(str, dividend[-(len(divisor) - 1):]))
    return remainder


print("\n3. CYCLIC REDUNDANCY CHECK (CRC)")

message = "1101011011"
generator = "10011"

# Append zeros before division
padded_message = message + "0" * (len(generator) - 1)

remainder = crc_remainder(padded_message, generator)

transmitted_frame = message + remainder

print("Original Message:", message)
print("Generator Polynomial:", generator)
print("CRC Remainder:", remainder)
print("Transmitted Frame:", transmitted_frame)

print("\n" + "=" * 60)
print(" ERROR DETECTION ANALYSIS COMPLETED")
print("=" * 60)
