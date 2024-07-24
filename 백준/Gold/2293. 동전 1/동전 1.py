a, b = map(int, input().split())
coin = []
for i in range(a):
    coin.append(int(input()))

dp = [0] * (b+1)
dp[0] = 1

for won in coin:
    for i in range(won, b+1):
        gyungwoo = dp[i - won]
        dp[i] += gyungwoo

print(dp[b])