def factorial(num):
    # 입력값이 0보다 클 때 입력값 * 본인 함수의 입력값-1값
    # 즉 for문처럼 1씩 떨어지면서 0이 되기 전까지 반복
    if num > 0:
        return num * factorial(num - 1)
    # 입력값이 0이 되었을 땐 1을 반환
    else:
        return 1
    
num = int(input())
print(factorial(num))