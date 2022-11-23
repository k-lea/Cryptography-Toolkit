"""
Primitive Polynomials

Author: Kyri Lea

Determine whether a polynomial is primitive or just irreducible. 
Given a polynomial as a list of numbers, this will print out the 
length of the sequence that it will create. 
"""

print("-----------------------------------------------------------")
print("                   Primitive Polynomials                   ")
print()
print("   Determine if a polynomial is primitive or irreducible   ")
print("-----------------------------------------------------------")
print()

output = dict()

eqn = input("Enter the numbers (For example: '0,2,5'): ").split(",")
deg = int(eqn[-1])

max_rounds = pow(2,deg) - 1
print("Max rounds = ", max_rounds)
# Initialize the state with all 1s
initial = [1] * deg
output[0] = initial 
all = [initial]


def make_func(eqn, old):
    start = old[0] # The last number in the array. Will always be used
    for i in eqn:
        if int(i) == deg:
            return start
        elif int(i) == 0:
            pass # 0 is already accounted for in start
        else:
            res = start ^ old[int(i)]
            start = res

for i in range(1, max_rounds + 1):
    ind = i - 1
    past = output[ind]
    new = [0] * deg
    for j in range(0, deg-1):
        new[j] = past[j+1]
    new[deg-1] = make_func(eqn, past)
    output[i] = new
    if new in all:
        print("Done: ", i)
        break
    all.append(new)
