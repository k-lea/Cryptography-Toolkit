"""
ModTabs

Author: Kyri Lea

Find the order associated with each number in a ring.
"""

import math

num = int(input("Enter Number: "))
chart = {}

print("Num".ljust(4 * num + 4), "Order/GCD")
for i in range(1, num):
    row = []
    for j in range(0, num):
        q, r = divmod(pow(i, j), num)
        row.append(r)
    chart[i] = row 

for row in chart:
    order = 1
    for i in range(1, num):
        if chart[row][i] == 1:
            break
        else:
            order += 1
    if order == num:
        order = math.gcd(row, num)
        print(str(row).ljust(4 * num + 5), order, "(GCD)")
    else:
        # Get the entire row
        print(str(row).ljust(4), str(chart[row]).ljust(4*num), str(order))

