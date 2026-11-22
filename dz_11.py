import time

n = 500_000
target = 499_999
data_list = list(range(n))
data_set = set(data_list)
repeats = 1_000_000

start = time.perf_counter()
for i in range(repeats):
    target in data_set
set_time = (time.perf_counter() - start) / repeats

start = time.perf_counter()
for i in range(10):
    target in data_list
list_time = (time.perf_counter() - start) / 10

print(f"List search: ~{list_time:.6f} сек")
print(f"Set search: ~{set_time:.9f} сек")