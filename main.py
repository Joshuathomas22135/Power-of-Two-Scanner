""" In this assignment, you will build a Power of Two Scanner using Python bitwise operations. They will learn how to remove the rightmost set bit, check
powers of 2, 4, and 8, and calculate powers quickly using binary exponentiation."""

print("Power of 2 Scanner")

numbers = [1, 2, 4, 6, 8, 12, 16, 18, 32]

print("The n & (n-1) Trick")
n = 18
print(n&(n-1))
print()

print("Power of 2 Check")

def isPowerOf2(n):
    return n > 0 and n & (n-1) == 0

for i in numbers:
    print(f"{i}, Check of Power: {isPowerOf2(i)}")
print()

print("Power of 4 Check")

def isPowerOf4(n):
    if not isPowerOf2(n):
        return False

    pos = 0

    if n > 1:
        n = n >> 1
        pos+=1
    return pos % 2 == 0

for i in numbers:
    print(f"{i}, Check of Power: {isPowerOf4(i)}")
print()

print("Power of 8 Check")
def isPowerOf8(n):
    if not isPowerOf2(n):
        return False

    pos = 0

    while n > 1:
        n = n >> 1
        pos+=1

    return pos % 3 == 0

for i in numbers:
    print(f"{i}, Check of Power: {isPowerOf8(i)}")
print()

print("Binary Exponentiation")

def binaryPower(base, exponent):
    a = 1

    while exponent > 0:
        if exponent & 1:
            a = a * base

        base = base * base
        exponent = exponent >> 1

    return a

print(f"2^5: {binaryPower(2,5)}")
print(f"3^4: {binaryPower(3,4)}")
print(f"5^3: {binaryPower(5,3)}")