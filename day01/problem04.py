"""Problem 04: Find the maximum without max() or sorting."""


def solution(numbers):
    maximum = numbers[0]
    for x in numbers:
        if x > maximum:
            maximum = x
    return maximum


print(solution([3, 8, 2, 10, 5]))
