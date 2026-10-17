"""Problem 02: Count passing and failing scores (60-point threshold)."""


def solution(scores):
    p = 0
    np = 0
    for x in scores:
        if x >= 60:
            p += 1
        else:
            np += 1
    return [p, np]


print(solution([80, 45, 70, 50, 90]))
