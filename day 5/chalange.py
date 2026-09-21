import random
import time

start = time.time()
numbers = [random.randint(1, 1000000) for _ in range(1000000)]
numbers.sort()
print(time.time() - start)