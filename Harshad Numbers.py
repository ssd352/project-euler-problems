import math

def isPrime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n & 1 == 0:
        return False
    m = n % 6
    if m == 3:
        return False
    for cnt in range(5, math.floor(math.sqrt(n)) + 1):
        if n % cnt == 0:
            return False
    return True

def isHarshad(n, strong):
    sum1 = 0
    m = n
    while m > 0:
        sum1 = sum1 + m % 10
        m = m // 10
    if strong == False:
        return (n % sum1 == 0)
    else:
        return (n % sum1 == 0) and isPrime(n // sum1)



"""
r_t = {1 : 1, 2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 : 9}
for n in range(10, 10 ** 14):
    (m, rem) = divmod(n , 10)
    if (m in r_t):
        a = r_t[m] + rem 
        if (n % a == 0):
            r_t[n] = a

r_t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(r_t)):
    r_t.append(r_t[i] * 10)
    for j in range(1, 10):
        if 
for i in range(1, 30):
    if isPrime(i):
        print(i)"""
import queue
r_t = queue.PriorityQueue()
srt = set()
N = 10 ** 14
srt_limit = N / 10

for cnt in range(1, 10):
    r_t.put((cnt, cnt))

while not r_t.empty():
    a = r_t.get()

    if isPrime(a[0] // a[1]):
        srt.add(a[0])

    if (a[0] * 10 < srt_limit):
        r_t.put((a[0] * 10, a[1])) 

    for cnt in range(1, 10):

        new_num = a[0] * 10 + cnt
        sum_dig = a[1] + cnt

        if new_num < srt_limit and new_num % sum_dig == 0:
            r_t . put((new_num, sum_dig))
            
#print(str(len(srt))+'\n')
sum1 = 0
srtp = set()
for item in srt:
    #print('\n'+str(item)+'\n')
    for cnt in range(1, 10):
        x = item * 10 + cnt
        if isPrime(x) and x < N:
            srtp.add(x)
            #sum1 = sum1 + x
            #print(x)
"""for item in srtp:
    if not isPrime(item):
        print(str(item) + 'is not prime')
    elif not isHarshad(item // 10, True):
        print(str(item // 10)+'is not harshad')"""
print(sum(srtp))
        
