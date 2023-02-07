from collections import Counter
n = int(input())
size_list = []
for _ in range(n):
    size = int(input())
    size_list.append(size)
x=Counter(size_list)
print(x)