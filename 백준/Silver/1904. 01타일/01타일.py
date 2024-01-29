import sys

n = int(sys.stdin.readline())

pibo = [0, 1]
m1 = 0
m2 = 0
i = 0

while i != n:
    m1 = pibo[0] + pibo[1]
    m2 = pibo[1]
    pibo[0] = m2 % 15746
    pibo[1] = m1 % 15746
    i += 1

result = pibo[1]

print(result)