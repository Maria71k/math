import math

def combinations(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

n = 10  # Total number of items
k = 3   # Number of items to choose
result = combinations(n, k)
print(f"Number of combinations choosing {k} from {n}: {result}")
