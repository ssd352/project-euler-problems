def extended_gcd(a, b):
    s = 0;    old_s = 1
    t = 1;    old_t = 0
    r = b;    old_r = a
    while r != 0:
        quotient = old_r // r
        (old_r, r) = (r, old_r - quotient * r)
        (old_s, s) = (s, old_s - quotient * s)
        (old_t, t) = (t, old_t - quotient * t)
    return old_s, old_t

n = 10 ** 6
lim = n + 1
m = lim
power = []
while m != 0:
    # print('hello')
    if m & 1 != 0:
        power.append(True)
    else:
        power.append(False)
    m >>= 1
sum1 = 0
for k in range(2, n + 1):
    # print(k)
    q = (1 - k * k) % 1000000007
    a = q
    p = 1
    """for cnt in range(1, n + 1):
        p = (p * q) % 1000000007
        sum1 = (sum1 + p) % 1000000007"""
        
    for cnt in range(len(power)):
        # print('hello')
        if power[cnt]:
            p = (p * a) % 1000000007
        a = (a * a) % 1000000007
    num = (q - p) % 1000000007
    den = (k * k) % 1000000007
    (a1, a2) = extended_gcd(den, 1000000007)
    if ((a1 * num) % 1000000007 * den - num) % 1000000007 != 0:
        print('wrong again keith')
    sum1 = (sum1 + a1 * num) % 1000000007
print(sum1)
