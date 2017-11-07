import math
gcd_table = {}


def gcd(a, b):
    if a == 1 or b == 1:
        return 1
    elif a == 0:
        # gcd_table[(b, a)] = b
        return b
    elif b == 0:
        # gcd_table[(a, b)] = a
        return a
    else:
        a1 = max([a, b])
        b1 = min([a, b])
        if (a1, b1) not in gcd_table:
            gcd_table[(a1, b1)] = gcd(b1, a1 % b1)
        return gcd_table[(a1, b1)]

np_table = {}


def np(a, b):
    a1 = max([a, b])
    b1 = min([a, b])
    if (a1, b1) in np_table:
        return np_table[(a1, b1)]
    else:
        np_table[(a1, b1)] = ((a - 1)*(b - 1) - gcd(a, b) + 1) // 2
        return np_table[(a1, b1)]
        

def isSquare(n):
    m = int(math.sqrt(n))
    return m * m == n
square_table = {}

m = 100
num = 0
for a in range(1, m + 1):
    print(a)
    for b in range(1, m + 1):
        for c in range(a, m + 1):
            for d in range(b, m + 1):
                l1 = tuple(sorted([a, c]))
                l2 = tuple(sorted([b, d]))
                if (l1, l2) not in square_table:
                    nop = np(a, b) + np(a,d) + np(c, b) + np(c, d) + a + c + b + d - 3
                    square_table[(l1, l2)] = isSquare(nop)
                    square_table[(l2, l1)] = square_table[(l1, l2)]
                if square_table[(l1, l2)]:
                    num += 1
print(num)

