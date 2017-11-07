checked = set()
reversible = set()
reverse_dict = {}

def reverse(n):
    """if n in reverse_dict:
        return reverse_dict[n]"""
    """m = n
    rev = 0
    while m > 0:
        rev = rev * 10
        rev = rev + m % 10
        m = m // 10"""
    rev = int(str(n)[::-1])
    #reverse_dict[n] = rev
    #reverse_dict[rev] = n
    return rev
def isReversible(n):
    if (n & 1) == (reverse(n) & 1):
        return False
    a = n + reverse(n)
    while a > 0:
        if (a % 10) & 1 == 0:
            return False
        a = a // 10
    return True

N = 10 ** 7
import time
start_time = time.time()
for i in range(11, N):
    if i % 10 == 0:
        continue
    #if i in checked:
       # continue
    r = reverse(i)
    #checked.add(i)
    #checked.add(r)
    if isReversible(i):
        reversible.add(i)
        reversible.add(r)
print(len(reversible))
print("--- %s seconds ---" % (time.time() - start_time))
