import sys

def coincoin(case):
    for i in range(case):
        cnt = int(sys.stdin.readline())
        coins = list(map(int, sys.stdin.readline().split()))
        price = int(sys.stdin.readline())
        
        money = [0 for _ in range(price+1)]
        money[0] = 1

        for coin in coins:
            for i in range(coin, price+1):
                money[i] += money[i-coin]

        print(money[price])

case = int(sys.stdin.readline())
coincoin(case)