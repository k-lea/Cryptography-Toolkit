"""
RSA Signature Forgery 

Author: Kyri Lea

Find the signature value needed for a specific message x and
public key (n, e). 

Requires sq_mul.py
"""

from sq_mul import make_exp_arr, square_multiply


print("--------------------------------------------")
print("           RSA Signature Forgery            ")
print()
print("   Find a valid signature for a message x   ")
print("--------------------------------------------")
print()


x = int(input("x: "))
e = int(input("e: "))
n = int(input("n: "))

exp = make_exp_arr(e)

for s in range(0, n):
    xp = square_multiply(s, exp, n)
    if xp == x:
        print("s = ", s)
        break

