"""
Square and Multiply 

Author: Kyri Lea

An efficient algorithm for calculating exponents.
"""

def square_multiply(base, exp, mod):
    x = base
    for i in range (1, len(exp)):
        bit = exp[i]
        x = pow(x, 2) % mod 
        if bit == '1':
            x = x * base 
    x = x % mod
    return x


def make_exp_arr(power):
    """
    Make an array of the exponent in binary.
    """
    exp = bin(power)
    exp = exp[2:]
    return exp 


def main():
    print("-------------------------")
    print("   Square and Multiply   ")
    print("-------------------------")
    print()
    base = int(input("Base: "))
    power = int(input("Exponent: "))
    mod = int(input("Mod: "))

    exp = make_exp_arr(power)
    result = square_multiply(base, exp, mod)
    print(result)


if __name__ == "__main__":
    main()
