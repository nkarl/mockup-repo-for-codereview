# Helper function, that uses a buffer to prevent an overflow
def fibo(i, prev, curr, buf):
    if i == 0:
        return buf
    else:
        return fibo(i-1, curr, prev+curr, prev+curr)

# Starter function
def fib(n):
    return fibo(n, 0, 1, 0)

# Manual tests
aa = fib(3)
print(f"result: {aa}")
bb = fib(5)
print(f"result: {bb}")
cc = fib(9)
print(f"result: {cc}")

# 0 1 2 3 4 5 6  7  8  9 10
# 0 1 1 2 3 5 8 13 21 34 55

# added newline char here, this only to practice reviewing code.
