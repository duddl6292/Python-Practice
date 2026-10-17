"""Problem 05: Find max-min without built-in extrema or sorting."""


def solution(numbers):
    maximum = numbers[0]
    minimum = numbers[0]
    for x in numbers:
        if x > maximum:
            maximum = x
        if x < minimum:
            minimum = x
    return (maximum - minimum)


print(solution([3, 8, 2, 10, 5]))
