import sys
input = sys.stdin.readline

n = input()
a = list(n)

if(a[0] == '0' and a[1] == 'x'):
    print(int(n,16))
elif (a[0] == '0'):
    print(int(n, 8))
else:
    print(n)