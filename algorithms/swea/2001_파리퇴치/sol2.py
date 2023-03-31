import sys
sys.stdin = open('input.txt')

def hit(r, c, size):
    global matrix
    total = 0
    # 파리채를 r, c 기준으로 휘두르기
    for nr in range(size):
        for nc in range(size):
            total += matrix[r + nr][c + nc]
    return total


T = int(input())

for tc in range(1, T + 1):
    # N은 맵의 크기, M은 파리채의 크기
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    maximum = 0

    # 파리채 시작점의 row
    for row in range(0, N - M + 1):
        # 파리채 시작점의 col
        for col in range(0, N - M + 1):
            kill = hit(row, col, M)
            if kill > maximum:
                maximum = kill

    print(f'#{tc} {maximum}')