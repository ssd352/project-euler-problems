import math
s_reps = {1}
for r in range(2, 10 ** 6 + 1):
    r_n = r * r
    sum1 = r_n + r + 1
    while (sum1 < 10 ** 12):
        s_reps.add(sum1)
        r_n = r_n * r
        sum1 = sum1 + r_n
sum2 = sum(s_reps)
print(sum2)
