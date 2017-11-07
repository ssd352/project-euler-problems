"""def urn_rec(index, num_balls, sum_temp, sum_all, num_solutions):
    #print('index is ' + str(index))
    if (index == 0):
        return
    
    for cnt in range(10 + 1):
        #print('iteration no. ' + str(cnt))
        sum_temp = sum_temp + cnt
        
        if cnt is not 0:
            num_balls = num_balls + 1
        
        if sum_temp > 20:
            return

        if sum_temp == 20:
            num_solutions = num_solutions + 1 
            sum_all = sum_all + num_balls
            return [sum_all, num_solutions]
        
        a = urn_rec(index - 1, num_balls, sum_temp, sum_all, num_solutions)
        if a:
            sum_all = sum_all + a[0]
            num_solutions = num_solutions + a[1]
            
    return [sum_all, num_solutions]

def good_move(index):
    if (index == 0):
        print('\n')
        return
    for cnt in range(2):
        print(str(cnt), end = '')
        good_move(index - 1)
    
good_move(8)
sum_all = 0
num_balls = 0
num_solutions = 0
hello = urn_rec(7, num_balls, 0, sum_all, num_solutions)
print(hello, sum_all, num_balls, num_solutions)"""
sum_all = 0
num_balls = 0
num_solutions = 0
"""for x1 in range (10 + 1):
    
    if (x1 == 0):
        num_balls = 0
    else:
        num_balls = 1
        
    for x2 in range(10 + 1):
        
        if not (x2 == 0):
            num_balls = num_balls + 1
            
        if (x1 + x2 == 20):
            num = num_solutions
            sum_all = sum_all + num_balls
            break
        for x3 in range(10 + 1):
"""
def binomial(n, k):
        if k < 0 or n < 0 or n < k:
            return 0
        if k > n - k:
            return binomial(n, n - k)
        result = 1
        for i in range(k):
            result = result * (n - i) // (i + 1)
        return result
    
def num_balls(arr):
    num = 0
    for item in arr:
        if item != 0:
            num = num + 1
    return num
def prs(s):
    fact = 1
    for item in s:
        fact = fact * binomial(10, item)
    return fact
        
sum_all = 0
num_solutions = 0
for x1 in range(10 + 1):
    for x2 in range(10 + 1):
        for x3 in range(10 + 1):
            for x4 in range(10 + 1):
                for x5 in range(10 + 1):
                    for x6 in range(10 + 1):
                        for x7 in range(10 + 1):
                            s = [x1, x2, x3, x4, x5, x6, x7]
                            if sum(s) == 20:
                                sum_all = sum_all + num_balls(s) * prs(s)
                                #num_solutions = num_solutions + 1
num_solutions = binomial(70, 20)
"""for x1 in range(10 + 1):   
    for x2 in range(10 + 1):
        s2 = [x1, x2]
        if sum(s2) == 20:
                sum_all = sum_all + num_balls(s2)
                num_solutions = num_solutions + 1
                break
                
        for x3 in range(10 + 1):
            s3 = [x1, x2, x3]
            if (sum(s3) > 20):
                break
            elif sum(s3) == 20:
                sum_all = sum_all + num_balls(s3)
                num_solutions = num_solutions + 1
                break
            
            
            for x4 in range(10 + 1):
                s4 = [x1, x2, x3, x4]
                if (sum(s4) > 20):
                    break
                elif sum(s4) == 20:
                    sum_all = sum_all + num_balls(s4)
                    num_solutions = num_solutions + 1
                    break
                    
            
                for x5 in range(10 + 1):
                    s5 = [x1, x2, x3, x4, x5]
                    if (sum(s5) > 20):
                        break
                    elif sum(s5) == 20:
                        sum_all = sum_all + num_balls(s5)
                        num_solutions = num_solutions + 1
                        break
                        
            
                    for x6 in range(10 + 1):
                        s6 = [x1, x2, x3, x4, x5, x6]
                        if (sum(s6) > 20):
                            break
                        elif sum(s6) == 20:
                            sum_all = sum_all + num_balls(s6)
                            num_solutions = num_solutions + 1
                            break
                    
                        for x7 in range(10 + 1):
                            s7 = [x1, x2, x3, x4, x5, x6, x7]
                            if (sum(s7) > 20):
                                break
                            elif sum(s7) == 20:
                                sum_all = sum_all + num_balls(s7)
                                num_solutions = num_solutions + 1
                                break"""
print(sum_all)
print(num_solutions)
print(float(sum_all)/num_solutions)
                            
