"""
Find Carmichael Numbers 

Author: Kyri Lea

Find all the Carmichael numbers less than a certain value.
"""

import random
from math import gcd, sqrt
from sq_mul import square_multiply, make_exp_arr


def fermat(p, s):
    """
    Returns 0 if composite, 1 if likely prime.
    """
    while s > 0:
        a = random.randint(2, p - 2)
        if gcd(a, p) != 1:
            continue
        exp = make_exp_arr(p - 1)
        result = square_multiply(a, exp, p)
        if result != 1:
            return 0
        s -= 1
    return 1


def prime_check(num):
    """
    Returns 0 if composite, 1 if prime.
    """
    root = int(sqrt(num))
    for i in range(2, root + 1):
        if (num % i) == 0:
            return 0
    return 1


def find_c(num, s):
    # We want a 1 from Fermat's and a 0 from prime check.
    print("Finding Carmichael Numbers less than", num, ". . .")
    for i in range(num, 500, -1):
        x = fermat(i, s)
        if x == 0: continue
        y = prime_check(i)
        if y == 0:
            print(i)


def main():
    print("-----------------------------------------------")
    print("           Carmichael Number Finder            ")
    print()
    print("   Find Carmichael numbers less than a value   ")
    print("-----------------------------------------------")
    print()

    num = int(input("Find all Carmichael numbers less than: "))
    s = int(input("Security parameter (10 - 20): "))
    print()
    find_c(num, s)


if __name__ == "__main__":
    main()
