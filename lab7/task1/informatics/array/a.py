# Задача №63. A[0], A[2], A[4], ...
n = input()
n = input()
a = n.split(" ")
for i in range(len(a)):
    if i % 2 == 0:
        print(a[i], end=" ")