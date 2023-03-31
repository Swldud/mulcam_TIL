# https://www.acmicpc.net/problem/8958


T = int(input())

for char in range(T):
    ox = input()
    total = 0
    now = 0

    for char in ox:
        if char == 'O':
            now += 1
            total += now
        else:
            now = 0

    print(total)



