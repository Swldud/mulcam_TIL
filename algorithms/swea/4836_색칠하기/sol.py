import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 파란색일 경우 / [0]은 범위가 N이하인 i로 바꿔서 자동화 해야함.
    blue = set()
    red = set()
    for i in range(N):
        r_1, c_1, r_2, c_2, color = map(int, input().split())
        for r in range(r_1, r_2+1):
            for c in range(c_1, c_2+1):
                          if color == 1:
                              blue.add((r, c))
                          else:
                              red.add((r, c))

    inter_section = blue & red

    print(f'#{tc} {len(inter_section)}')







