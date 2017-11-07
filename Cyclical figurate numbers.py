def octagonal(n):
    return n * (3 * n - 2)
def heptagonal(n):
    return n * (5 * n - 3) // 2
def list_all(f, num_dig):
    #print(f)
    out = set()
    n = 1
    m = f(n)
    while (m < 10 ** num_dig):
        if (m >= 10 ** (num_dig - 1)):
            #print(m)
            out.add(m)
        n = n + 1
        m = f(n)
    return out
oct_set = list_all(octagonal, 4)
hept_set = list_all(heptagonal, 4)

