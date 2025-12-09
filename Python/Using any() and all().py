nums = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in nums)) # true
print(any(n > 5 for n in nums))  # true