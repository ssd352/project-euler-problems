"""def isPalindromic(n):
    m = n
    inver = 0
    while m > 0:
        inver = inver * 10
        inver = inver + m % 10
        m = m // 10
    return inver == n
limit = 1
N = 10 ** 8
while limit ** 2 + (limit - 1) ** 2 < N:
    limit = limit + 1
limit = limit - 1
se = set()
for cnt in range(1, limit):
    sum1 = cnt * cnt
    for part in range(cnt + 1, limit + 1):
        sum1 = sum1 + part * part
        if sum1 >= N:
            break
        if isPalindromic(sum1):
            se.add(sum1)
#print(se)
print(sum(se))"""
class A:
    def __init__(self, val):
        self._val = val
class B(A):
    def __init__(self, val):
        super(B, self).__init__(val)
    def print_val(self):
        print(self._val)
b = B(5)
b.print_val()
