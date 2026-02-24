data = [1, 2, 1, 3, 2, 1]

freq = {}

for num in data:
    freq[num] = freq.get(num, 0) + 1

print(freq)