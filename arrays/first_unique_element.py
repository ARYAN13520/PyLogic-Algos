data = [4, 5, 1, 2, 0, 4, 5, 2]

freq = {}

for num in data:
    freq[num] = freq.get(num, 0) + 1

for num in data:
    if freq[num] == 1:
        print(num)
        break


'''First loop:

Builds the complete frequency map
After this, we know how many times every element appears

Second loop:

Preserves the original order
Returns the first element whose frequency is 1

If we only iterated over freq, we’d lose ordering. Dictionaries don’t guarantee original list order logic for this problem.

So:

First pass = counting
Second pass = ordered selection

This pattern is extremely common in DSA.'''