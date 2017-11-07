a = 1777


def hello(a, p):
    b = 1
    # all_num = set()
    all_dict = dict()
    dict_all = dict()
    ind = 0
    while b not in dict_all:
        all_dict[ind] = b
        dict_all[b] = ind
        # all_num.add(b)
        b *= a
        b %= p
        ind += 1
    return ind - dict_all[b]


lim = 10 ** 8
cnt = 0
arr = [10 ** 8]
while not lim == 1:
    lim = hello(a, lim)
    print(lim)
    arr.append(lim)
    cnt += 1
# arr.append(1)
c = 1
for iterate in reversed(arr):
    c = (a ** c) % iterate
print(c)
