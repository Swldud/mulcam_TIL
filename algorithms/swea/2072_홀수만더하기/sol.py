# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1

import sys
sys.stdin = open('input.txt')

# Test Case 개수
T = int(input())

for testcase_number in range(T):
    result = 0
    numbers = list(map(int, input().split()))
    for num in numbers:
        if num % 2:
            result += num

    print(f'#{testcase_number+1} {result}')






