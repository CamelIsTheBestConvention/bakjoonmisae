import sys
input = sys.stdin.readline

def popular_book():
    n = int(input())
    books = {}
    count = 0

    for i in range(n):
        name = input()

        if name in books:
            books[name] += 1
        else:
            books[name] = 1
        
        count = max(count, books[name])

    best_seller = []
    for name, cnt in books.items():
        if cnt == count:
            best_seller.append(name)

    best_seller.sort()
    print(best_seller[0])

popular_book()
