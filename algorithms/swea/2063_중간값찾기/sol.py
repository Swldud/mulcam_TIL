# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QPsXKA2UDFAUq

import sys
sys.stdin = open('input.txt')

# Test Case 개수
N = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

mid_idx = N // 2

print(numbers[mid_idx])

