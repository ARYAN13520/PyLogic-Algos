data = [1, 2, 1, 3, 2, 1]

freq = {}

for num in data:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)
'''
 A dictionary is used because:

It provides O(1) average lookup
Keys map directly to counts
Numbers may be non-contiguous or large
A list would require index mapping and wasted space


When a number appears for the first time:
This creates a new key-value pair in the dictionary.

So:
First time → initialize count = 1
Next times → increment existing count

This is the core frequency counting pattern used everywhere in ML preprocessing and text analytics.
'''