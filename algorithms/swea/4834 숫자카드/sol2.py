import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))  # [4, 7, 8, 7, 9]

    # 카드 개수 초기화 (0 ~ 9)
    card_counter = [0] * 10  # [0 for _ in range(10)]

    for card in cards:
        card_counter[card] += 1

    max_count = 0
    max_idx = 0

    for idx, count in enumerate(card_counter):
        # 0 => 9 로 가면서
        # 장수가 같거나 더 크면 갱신 => 장수가 같아도 숫자가 큰 카드가 남는다.
        if count >= max_count:
            max_count = count
            max_idx = idx

    print(f'#{tc} {max_idx} {max_count}')