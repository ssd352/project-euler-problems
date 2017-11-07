p = {2, 3}
limit = 10 ** 8


def isPrime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n & 1 == 0:
        return False
    for cnt in p:
        if n % cnt == 0:
            return False
    p.add(n)
    return True

n = 5
for cnt in range(4, n + 1):
    isPrime(cnt)

ham_dict = {0: 0, 1: 1, 2: 2}


def ham(n):
    if n not in ham_dict:
        sum1 = 0
        for prime in p:
            if n < prime:
                break
            sum1 += ham(n // prime)
        ham_dict[n] = sum1

    return ham_dict[n]


print(p)
print(ham(limit))
"""
import queue
ham_set = {1}
dr = queue.PriorityQueue()    
dr.put((1, 0))    
while not dr.empty():
    q = dr.get()[0]
    for prime in p:
        this_num = q * prime 
        if this_num <= limit:
            if this_num not in ham_set:
                dr.put((this_num, 0))
                ham_set.add(this_num)
        else:
            break
print(p)
print(len(ham_set))
"""
