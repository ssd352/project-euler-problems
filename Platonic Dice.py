all_sum = 0
# all_dict = {i: 0 for i in range(1, 4 * 6 * 8 * 12 * 20 + 1)}
var = 0
mean = 0
for sum1 in range(1, 4 + 1):
    for sum2 in range(sum1 * 1, sum1 * 6 + 1):
        for sum3 in range(sum2 * 1, sum2 * 8 + 1):
            for sum4 in range(sum3 * 1, sum3 * 12 + 1):
                # for sum5 in range(sum4 * 1, sum4 * 20 + 1):
                # all_sum += 1
                all_sum += (sum4 * 19 + 1)  # 1
                n = sum4 * 20
                var += ((sum4 * 10) * (n + 1) * ((n << 1) + 1)) / 3 - (sum4 * (sum4 - 1) * ((sum4 << 1) - 1)) / 6
                mean += (sum4 * 10) * (n + 1) - (((sum4 - 1) * sum4) >> 1)
mean = mean / all_sum
var = var / all_sum - mean * mean

print(var)
# 51698924.7923262