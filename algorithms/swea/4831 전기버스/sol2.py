import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 충전 회수
    charge_count = 0
    # K: 이동 가능 거리, N: 정류장 개수, M: 충전기 개수
    K, N, M = map(int, input().split())
    charge_stations = list(map(int, input().split()))

    bus_loc = K
    last_charge = 0

    while 1:
        if bus_loc >= N:
            break

        if bus_loc in charge_stations:
            charge_count += 1
            last_charge = bus_loc
            bus_loc += K
        else:
            bus_loc -= 1

        if bus_loc == last_charge:
            charge_count = 0
            break

    print(f'#{tc} {charge_count}')