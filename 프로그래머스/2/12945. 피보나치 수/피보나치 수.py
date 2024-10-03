def solution(n):
    MOD = 1234567
    fib = [0, 1]
    
    for i in range(2, n + 1):
        fib.append((fib[i - 1] + fib[i - 2]) % MOD)
    
    return fib[n]
