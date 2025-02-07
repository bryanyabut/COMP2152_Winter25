# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# result = [x**2 for x in numbers if x % 2 == 0 and x > 4]

# print(result)

# numbers = [1, 2, 3, 4, 5]
# result = [x * 3 for x in numbers if x % 2 != 0]
# print(result)

# text = "DeepLearning"
# result = text[4:10]
# print(result)

# count = 0
# for i in range(3):  # Outer loop
#     for j in range(2):  # Inner loop
#         count += 1
# print(count)

for i in range(2):  # Outer loop
    print(f"Outer loop iteration {i}")
    for j in range(3):  # Inner loop
        print(f"  Inner loop iteration {j}")