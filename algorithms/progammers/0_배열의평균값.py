# https://school.programmers.co.kr/learn/courses/30/lessons/120817

def solution(numbers):
    cnt = len(numbers)
    answer = sum(numbers) / cnt
    return answer


# 5.5
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# 94.0
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))
