# https://school.programmers.co.kr/learn/courses/30/lessons/120876

def solution(lines):
    answer = 0

    for line in (lines):
        set_1 = set(range(line[0][0], line[0][1] + 1))
        set_2 = set(range(line[1][0], line[1][1] + 1))
        set_3 = set(range(line[2][0], line[2][1] + 1))

        if set_1 & set_2 != set():
            answer += len(set_1 & set_2)
            answer -= 1

        if set_3 & set_2 != set():
            answer += len(set_3 & set_2)
            answer -= 1

        if set_3 & set_1 != set():
            answer += len(set_1 & set_3)
            answer -= 1

        if set_3 & set_1 & set_2 != set():
            answer = answer - (len(set_1 & set_3 & set_2) - 1) * 2

        break

    return answer
# 2
print(solution([[0, 1], [2, 5], [3, 9]]))

# 0
print(solution([[-1, 1], [1, 3], [3, 9]]))

# 8
print(solution([[0, 5], [3, 9], [1, 10]]))