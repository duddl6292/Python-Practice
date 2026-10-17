"""Problem 06: Find maximum and count its occurrences in one pass."""


def solution(numbers):
    maximum = numbers[0]
    cnt = 0
    for x in numbers:
        if x > maximum:
            maximum = x
            cnt = 0
        if maximum == x:
            cnt += 1
    return [maximum, cnt]


print(solution([3, 8, 8, 2, 10, 10, 5]))
