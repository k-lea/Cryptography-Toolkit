"""
Discrete Log Solver

Author: Kyri Lea

Brute force solver for the discrete log problem. Designed for use with small p values. 
Solve an equation of the form a^x = b mod p.
"""
print("-------------------------------")
print("      Discrete Log Solver      ")
print()
print("   Solve a^x = b mod p for x   ")
print("-------------------------------")
print()

a = int(input("a: "))
b = int(input("b: "))
p = int(input("p: "))

for x in range(1, p):
    if pow(a, x) % p == b:
        print("x =", x)
        break

