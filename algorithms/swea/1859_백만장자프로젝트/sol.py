# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc

import sys
sys.stdin = open('input.txt')

# Test Case 개수
T = int(input())

for testcase_number in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    total = 0
    max_price = 0

    for i in range(N-1, -1, -1):
        price = prices[i]

        if price < max_price:
            profit = max_price - price
            total += profit

        else:
            max_price = price

    print(f'#{testcase_number} {total}')




