#!/usr/bin/env python3
import re
import sys
from expecter import expect


def parenthesize(expr, operator):
    expr = re.sub(r"\s+", "", expr)

    i = len(expr)
    while i != 0:
        i -= 1
        if expr[i] != operator:
            continue

        if expr[i + 1].isdigit():
            j = i + 2
            while j < len(expr) - 1 and expr[j].isdigit():
                j += 1
            expr = expr[:j] + ")" + expr[j:]
        else:
            assert expr[i + 1] == "("
            j = i + 1
            c = 1
            while c != 0:
                j += 1
                if expr[j] == ")":
                    c -= 1
                elif expr[j] == "(":
                    c += 1
            expr = expr[:j] + ")" + expr[j:]

        if expr[i - 1].isdigit():
            j = i - 2
            while j >= 0 and expr[j].isdigit():
                j -= 1
            expr = expr[:j + 1] + "(" + expr[j + 1:]
        else:
            assert expr[i - 1] == ")"
            j = i - 1
            c = 1
            while c != 0:
                j -= 1
                if expr[j] == "(":
                    c -= 1
                elif expr[j] == ")":
                    c += 1
            expr = expr[:j + 1] + "(" + expr[j + 1:]

        i += 1

    return expr


def compute(expr):
    stack = []

    expr = parenthesize(expr, "+")

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


expect(compute("1 + 2 * 3 + 4 * 5 + 6")) == 231
expect(compute("1 + (2 * 3) + (4 * (5 + 6))")) == 51
expect(compute("2 * 3 + (4 * 5)")) == 46
expect(compute("5 + (8 * 3 + 9 + 3 * 4 * 3)")) == 1445
expect(compute("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")) == 669060
expect(compute("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")) == 23340

print(aoc(sys.stdin.read()))
