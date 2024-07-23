L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A % C == 0:
    day_kor = A // C
else:
    day_kor = A // C + 1

if B % D == 0:
    day_math = B // D
else:
    day_math = B // D + 1

if day_kor > day_math:
    print(L - day_kor)
else:
    print(L - day_math)