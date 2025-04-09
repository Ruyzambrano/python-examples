# for, while loops iterate or repeat

names = ["Ann", "Chris", "Ruy"]

# index
print("Using indices")
for i in range(len(names)):
    print(i, names[i])

# iterating a list
print("Iterating")
for name in names:
    print(name)

# while loop
i = 0
print("Using Loops")
while i < len(names):
    print(i, names[i])
    i += 1

# continue
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Using continue")
for num in numbers:
    if num > 3:
        print(num)
    else:
        continue
    print("Hi")

print("Using break")
for num in numbers:
    if num > 8:
        break
    print(num)

# ship example
ship_capacity = 100
items = [10, 33, 45, 2, 5, 99, 2, 54, 12, 3]
ship_weight = 0

for item in items:
    if item + ship_weight > ship_capacity:
        continue
    else:
        ship_weight += item
        print(f"Adding {item} to ship, ship weight is now {ship_weight}")

# a better example
for item in items:
    if item + ship_weight <= ship_capacity:
        ship_weight += item
        print(f"Adding {item} to ship, ship weight is now {ship_weight}")

print(f"Ship weight is {ship_weight}")