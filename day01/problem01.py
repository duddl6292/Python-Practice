"""Problem 01: Count positive even numbers."""


def solution(numbers):
    cnt = 0
    for x in numbers:
        if x % 2 == 0 and x > 0:
            cnt += 1
    return cnt


print(solution([1, 2, 3, 4, 5, 6]))
