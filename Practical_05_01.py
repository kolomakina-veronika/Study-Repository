nums = [32,14,2,6,7,13,8]
nums_sorted = nums.copy()
nums_sorted.sort()
count = 0
total = 0
min_number = nums[0]
max_number = nums[0]
avg_number = 0
for i in nums:
    count += 1
    total += i
    if min_number > i:
        min_number = i
    if max_number < i:
        max_number = i
avg_number = total / count
print(f"Масив: {nums} \nВідсортований:{nums_sorted}")
print(f"Кількість чисел: {count} \nСума загалом: {total}")
print(f"Найменше число: {min_number} \nНайбільше число: {max_number} \nСереднє арифметичне: {avg_number:.2f}")