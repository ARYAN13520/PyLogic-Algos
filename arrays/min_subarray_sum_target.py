data = [2, 3, 1, 2, 4, 3]
target = 7

window_sum = 0
min_length = float('inf')
start = 0

for end in range(len(data)):
    window_sum += data[end]

    while window_sum >= target:
        min_length = min(min_length, end - start + 1)
        window_sum -= data[start]
        start += 1

print(min_length if min_length != float('inf') else 0)

'''
once window_sum >= target, we must shrink the window as much as possible to get the minimum length.
If we used if, we would shrink only once and stop, possibly leaving a larger-than-necessary window.

Example:

window = [3,1,2,4] → sum = 10 ≥ 7

We can shrink repeatedly:
remove 3 → [1,2,4] sum=7
remove 1 → [2,4] sum=6 (<7 stop)
The smallest valid window is [1,2,4] length 3, not 4.

That repeated shrinking is why we need while.
'''