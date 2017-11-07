from operator import itemgetter
gcd_table = {}
gcd_ref = {}


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def gc():
    keys = []
    for k, v in gcd_ref.items():
        if v == 1:
            keys.append(k)
    for k in keys:
        del gcd_ref[k]
        del gcd_table[k]
    del keys
# print(gcd(20, 3))
# print(gcd(10, 3))
# print(gcd_table)


def xv(n):
    g = 13
    g += gcd(g, n)
    # if len(gcd_table) >= 7000000:  # 11000000:
    #     gc()
    print(g)

# for n in range(5, 10 ** 9 + 1):
# map(xv, range(5, 10 ** 9 + 1))
g = 15
limit = 10 ** 9
num = 0
for n in range(5, limit + 1):
    a = gcd(g, n)
    g += a
    if not a == 1:
        if a == 3:
            print('n = {} a = {}'.format(n, a))
        if a not in gcd_table:
            gcd_table[a] = 0
        gcd_table[a] += 1
        # num += 1
# print('\n{}'.format(num))
# print(g)
gt = list(gcd_table.items())
gt.sort(key=itemgetter(1), reverse=True)
print(gt)
"""for k, v in gcd_ref.items():
    if v > 2:
        print(k[0], k[1], v, sep=',')"""
