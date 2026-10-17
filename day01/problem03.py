"""Problem 03: Return elements greater than target, preserving order."""


def solution(numbers, target):
    y = []
    for x in numbers:
        if x > target:
            y.append(x)
    return y


print(solution([3, 8, 2, 10, 5], 5))
