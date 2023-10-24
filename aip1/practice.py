a = [11, 3, 7, 40, 72, 89, 100]
print(a)
print(range(1, len(a)))
for i in range(1, len(a)):
    distance = a[i] - a[i-1]
    print(distance)