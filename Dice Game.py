import random
random.seed()
no_of_tests = 2 ** 23
num = 0
for test_no in range(no_of_tests):
    sum1 = 0
    sum2 = 0
    for cntp in range(9):
        sum1 = sum1 + random.randrange(1, 4 + 1)
    for cntc in range(6):
        sum2 = sum2 + random.randrange(1, 6 + 1)
    if (sum1 > sum2):
        num = num + 1
print(num / float(no_of_tests))
