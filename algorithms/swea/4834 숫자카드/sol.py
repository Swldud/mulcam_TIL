# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open('input.txt')

# Test Case 개수
T = int(input())

for testcase_number in range(1, T + 1):
    N = int(input())
    numbers = input()
    pair = ''

    for i in range(0, 10):
        a = numbers.count(str(i))
        pair += str(a)
        continue

    max_value = pair[0]
    for ii in range(1, len(pair)):
        if max_value < pair[ii]:
            max_value = pair[ii]
            b = ii

        elif max_value == pair[ii]:
            max_value = pair[ii]
            b = ii
            ii += 1

        else:
            ii += 1

        continue
    break

print(f'#{testcase_number} {b} {max_value}')




