"""Problem 07: Return all indexes of the maximum in one pass."""


def solution(numbers):
    maximum = numbers[0]
    maxidx = []
    for i, x in enumerate(numbers):
        if x > maximum:
            maximum = x
            maxidx = [i]
        elif x == maximum:
            maxidx.append(i)
    return maxidx


print(solution([3, 8, 8, 2, 10, 10, 5]))
