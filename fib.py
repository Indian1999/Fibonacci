import time
from functools import cache
import numpy as np
    
def fib_basic(n):
    if (n > 30):
        time.sleep(1)
        return "Thats too large for me man"
    if n <= 2:
        return 1
    else:
        return fib_basic(n-2) + fib_basic(n-1)
    
@cache
def fib_cache(n):
    if n <= 2:
        return 1
    else:
        return fib_cache(n-2) + fib_cache(n-1)
    
def fib_memo(n):
    memo = {0:0, 1:1, 2:1}
    def f(n):
        if n in memo:
            return memo[n]
        else:
            memo[n] = f(n-2) + f(n-1)
            return memo[n]
    return f(n)

def fib_binet(n):
    phi = (1+5**(1/2)) / 2
    psi = (1-5**(1/2)) / 2
    return round((phi**n - psi**n) / (5**(1/2)))

def fib(n):
    a = 1
    b = 1
    fib_num = 0
    for i in range(n-2):
        fib_num = a + b
        a = b
        b = fib_num
    return fib_num

def fib_matrix(n):
    #Seems to not give the proper value on larger n-s (overlow?) yes, using floats fixed it
    arr = np.array([[1.0,1.0],[1.0,0.0]])
    arr = np.linalg.matrix_power(arr, n-1)
    return round(arr[0][0])

results = {}
num = 100

start = time.perf_counter()
print("Basic:", fib_basic(num))
end = time.perf_counter()
print(end-start)
results["basic"] = end-start 

start = time.perf_counter()
print("Cache:", fib_cache(num))
end = time.perf_counter()
print(end-start)
results["cache"] = end-start

start = time.perf_counter()
print("Memo:", fib_memo(num))
end = time.perf_counter()
print(end-start)
results["memo"] = end-start

start = time.perf_counter()
print("Binet's formula:", fib_binet(num))
end = time.perf_counter()
print(end-start)
results["binet"] = end-start

start = time.perf_counter()
print("Non recursive:", fib(num))
end = time.perf_counter()
print(end-start)
results["non_recursive"] = end-start

start = time.perf_counter()
print("Matrix:", fib_matrix(num))
end = time.perf_counter()
print(end-start)
results["matrix"] = end-start

from pprint import pprint
results = dict(sorted(results.items(), key = lambda item: item[1],reverse=False))
for item in results.items():
    print(item)


