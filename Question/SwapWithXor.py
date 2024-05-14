a, b = 10, 20

print(f"Before {a, b}")
a = a ^ b
b = a ^ b
a = a ^ b

print(f"After Swap: {a, b}")