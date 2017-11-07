import math
def isSquare(n):
    l4 = n & 15
    if l4 != 0 and l4 != 1 and l4 != 4 and l4 != 9:
        return False
    a = int(math.sqrt(n))
    return a * a == n

n = 10 ** 12
b = 2 * n * (n - 1) + 1
a = math.ceil(math.sqrt(b))
c = (a * a - 1) // 8
print(c % 4)
"""while True:
    b = 2 * n *(n - 1) + 1
    if isSquare(b):
        break
    n = n + 1
    b = 2 * n *(n - 1) + 1
    if isSquare(b):
        break
    n = n + 3
a = int(math.sqrt(b)) + 1
print(a // 2)"""

