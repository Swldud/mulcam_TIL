# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]


# 2. 시작 점(r,c) + 오 +대각 +아래
        # 시작 점의 r
    maximum = 0

    for row in range(0, N-M+1):
            # 시작 점의 c
        for col in range(0, N-M+1):
            total = 0
            for i in range(M):
                for j in range(M):
                    total += matrix[row+i][col+j]

            if total > maximum:
                    maximum = total

    print(f'#{tc} {maximum}')


