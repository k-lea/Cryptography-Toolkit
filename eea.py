"""
Extended Euclidean Algorithm Calculator 

Author: Kyri Lea

Calculate the inverse of a mod b.
"""

print("-----------------------------------------------")
print("    Extended Euclidean Algorithm Calculator    ")
print()
print("       Calculate the inverse of a mod b        ")
print("-----------------------------------------------")
print()


quotients = {}
start = int(input("Enter the first number: "))
modu = int(input("Enter the second number: "))


def calibrate(inv, mod):
    """
    If the result is negative, calibrate so it is positive.
    """
    while inv < 0:
        inv += mod 
    return inv

def first(a, b, count):
    if b == 0:
        if a == 1:
            x, y = second(a, b, count)
            if x < 0:
                x = calibrate(x, modu)
            print("The inverse is", x)
        else:
            print("Not relatively prime.")
    else:
        q, r = divmod(a, b)
        quotients[count] = q
        count += 1
        first(b, r, count)


def second(xp, yp, count): 
    x = 0
    y = 0
    for row in range(count - 1, 0, -1):
        q = quotients[row]
        x = yp
        y = xp - (yp * q)
        xp = x
        yp = y
    return x, y


first(start, modu, 1)


