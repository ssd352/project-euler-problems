distincts = {1}
row1 = [1]
row2 = [1]
for cnt in range(3, 51 + 1):
    tmp = row1
    row1 = row2
    row2 = tmp
    row2 = [1]
    for cn2 in range(len(row1) - 1):
        row2.append(row1[cn2] + row1[cn2 + 1])
    if cnt % 2 ==0:
        row2.append(2 * row1[len(row1) - 1])
    for item in row2:
        distincts.add(item)
print(distincts)
"""max1 = max(row2)
se = set()
import math
for i in range(2, math.floor(math.sqrt(max1))):
    for item in distincts:
        if item % (i * i) == 0:
            se.add(item)"""
