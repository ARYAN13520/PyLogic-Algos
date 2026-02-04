# -----------------------------
# 1. Assignment and References
# -----------------------------

x = 5
y = x
x = 10

print("x:", x)
print("y:", y)


# -----------------------------
# 2. Mutable vs Immutable
# -----------------------------

a = [1, 2, 3]
b = a
a.append(4)

print("a:", a)
print("b:", b)


# -----------------------------
# 3. Type Inspection
# -----------------------------

num = 10
flt = 10.0
text = "10"

print(type(num))
print(type(flt))
print(type(text))


# -----------------------------
# 4. Basic Math Behavior
# -----------------------------

print(5 / 2)
print(5 // 2)
print(5 % 2)


# -----------------------------
# 5. Truthy and Falsy Values
# -----------------------------

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("python"))
print(bool([]))
print(bool([1, 2]))


# -----------------------------#
# # 6. Copy vs Reference (CRITICAL)
# -----------------------------

c = [10, 20]
d = c.copy()
c.append(30)

print("c:", c)
print("d:", d)
