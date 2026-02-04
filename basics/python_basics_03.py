# -----------------------------
# 1. List vs Tuple
# -----------------------------

lst = [10, 20, 30]
tup = (10, 20, 30)

lst[0] = 99
# tup[0] = 99   # uncommenting this will cause an error

print(lst)
print(tup)


# -----------------------------
# 2. Indexing (positive & negative)
# -----------------------------

data = [1, 2, 3, 4, 5]

print(data[0])
print(data[-1])
print(data[-2])


# -----------------------------
# 3. Slicing behavior
# -----------------------------

nums = [0, 1, 2, 3, 4, 5]

print(nums[1:4])
print(nums[:3])
print(nums[3:])
print(nums[::2])


# -----------------------------
# 4. Length and iteration
# -----------------------------

print(len(nums))

for i in range(len(nums)):
    print(nums[i])
