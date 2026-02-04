# -----------------------------
# 1. for-loop and range()
# -----------------------------

for i in range(3):
    print(i)

print("done")


# -----------------------------
# 2. range with start and step
# -----------------------------

for i in range(2, 10, 2):
    print(i)


# -----------------------------
# 3. while-loop behavior
# -----------------------------

count = 0
while count < 3:
    print(count)
    count += 1


# -----------------------------
# 4. print vs return
# -----------------------------

def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

x = add_print(2, 3)
y = add_return(2, 3)

print("x:", x)
print("y:", y)
