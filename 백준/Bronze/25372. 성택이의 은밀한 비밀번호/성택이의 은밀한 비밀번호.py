n = int(input());
for _ in range(n):
    password = len(input())
    if 6 <= password and password <= 9:
        print("yes")
    else:
        print("no")