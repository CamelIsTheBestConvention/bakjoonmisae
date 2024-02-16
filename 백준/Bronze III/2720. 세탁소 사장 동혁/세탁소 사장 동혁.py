import sys
input = sys.stdin.readline

def donghyuk():
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1

    n = int(input())

    for _ in range(n):
        c = int(input())
        price = 0
        q_count = 0
        d_count = 0
        n_count = 0
        p_count = 0

        q_count = c//quarter
        price = c%quarter
        d_count = price//dime
        price = price%dime
        n_count = price//nickel
        price = price%nickel
        p_count = price//penny

        print(q_count, d_count, n_count, p_count)
        
donghyuk()
