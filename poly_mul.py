"""
Multiply Polynomials

Author: Kyri Lea

Multiply polynomials expressed in hex in GF(2^8)
"""

def alg(num1, num2):
    sum = int("0", 16)
    if num2 % 2 != 0:
        sum = num1
    while num2 > int("1", 16):
        num1 = num1 * 2
        num2 = num2 // 2
        if num2 % 2 != 0:
            sum = sum ^ num1
        sum = mod(sum)
    return sum


def mod(prod):
    aes = int("11b", 16)
    if prod > int("3ff", 16):
        aes = aes * 4 
        prod = prod ^ aes
    elif prod > int("1ff", 16):
        aes = aes * 2 
        prod = prod ^ aes
    elif prod > int("FF", 16):
        prod = prod ^ aes
    return prod


num1 = int(input("First hex number: "), 16)
num2 = int(input("Second hex number: "), 16)
prod = alg(num1, num2)
ans = mod(prod)
print(hex(ans))
