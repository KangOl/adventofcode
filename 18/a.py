#!/usr/bin/env python3
import sys
from expecter import expect


def compute(expr):
    stack = []

    for token in expr:
        if token == " ":
            continue
        if not token.isdigit():
            if token in "*+(":
                stack.append(token)
                continue
            assert token == ")"
            token = stack.pop(-1)

        if not stack:
            stack.append(int(token))
        elif stack[-1] == "(":
            stack[-1] = int(token)
        else:
            if stack[-1].isdigit():
                stack[-1] = (stack[-1] * 10) + int(token)
                continue
            op = stack.pop(-1)
            value = stack.pop(-1)
            if op == "+":
                stack.append(value + int(token))
            elif op == "*":
                stack.append(value * int(token))

    assert len(stack) == 1
    return stack[0]

def aoc(homework):
    return sum(map(compute, homework.splitlines()))


expect(compute("1 + 2 * 3 + 4 * 5 + 6")) == 71
expect(compute("1 + (2 * 3) + (4 * (5 + 6))")) == 51
expect(compute("2 * 3 + (4 * 5)")) == 26
expect(compute("5 + (8 * 3 + 9 + 3 * 4 * 3)")) == 437
expect(compute("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")) == 12240
expect(compute("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")) == 13632

print(aoc(sys.stdin.read()))
