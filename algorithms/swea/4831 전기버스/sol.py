# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open('input.txt')

# Test Case 개수
T = int(input())

for tc in range(1, T+1):
    # 충전 회수
    charge_count = 0
    # K: 이동 가능 거리, N: 정류장 개수, M: 충전기 개수
    K, N, M = map(int, input().split())
    charge_stations = list(map(int, input().split()))
    all_stations = [0] * (N+1)
    for charge_idx in charge_stations:
        all_stations[charge_idx] = 1


    # 0. 마지막 정류장 도착하면 끝
    # 1. 최대한 멀리 가봄
    # 2. 충전소라면, 위치갱신 + 충전
    # 3. 아니라면 한칸씩 뒤로오기
    # 4. 뒤로오다 이전 위치 오면 실패

    bus_loc = K  # 버스의 위치(정류장)
    last_charge_location = 0

    while bus_loc < N:
        # 현재 위치가 충전소라면 충전 및 마지막 충전위치 갱신
        if all_stations[bus_loc] == 1:
            charge_count += 1
            last_charge_location = bus_loc
            bus_loc += K
        else:
            bus_loc -= 1

        # 버스의 위치가 뒤로 오다 마지막 충전소까지 와버렸다.
        if bus_loc == last_charge_location:
            charge_count = 0
            # 실패
            break

    print(f'#{tc} {charge_count}')



