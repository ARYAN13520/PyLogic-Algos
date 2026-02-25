data = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(data[:k])
max_sum = window_sum

for i in range(k, len(data)):
    window_sum += data[i]
    window_sum -= data[i - k]
    max_sum = max(max_sum, window_sum)

print(max_sum)