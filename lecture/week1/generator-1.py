"""
Generators
"""
# =============================================================================
# Generators: Yield Keyword
# =============================================================================
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b  # reads: a = b and b = a+b

fib_gen = fibonacci(10)
for number in fib_gen:
    print(number)
