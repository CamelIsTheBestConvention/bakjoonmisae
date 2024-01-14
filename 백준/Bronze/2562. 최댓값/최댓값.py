num = []
compare = []
max = 0
location = 0

for i in range(9):
    num.append(int(input()))
    compare.append(num[i])

compare.sort()
max = compare[len(compare)-1]
location = num.index(max)+1

print(max)
print(location)