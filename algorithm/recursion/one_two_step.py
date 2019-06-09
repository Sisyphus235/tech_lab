# -*- coding: utf8 -*-

"""
one or two steps each time
figure out how many ways to get n steps
"""

step_history = {}


def one_two_step_recursive(steps: int) -> int:
    if steps <= 0:
        return 0
    if steps == 1:
        return 1
    if steps == 2:
        return 2
    if steps in step_history:
        return step_history[steps]
    return one_two_step_recursive(steps - 1) + one_two_step_recursive(steps - 2)


def one_two_step_iterative(steps: int) -> int:
    if steps <= 0:
        return 0
    if steps == 1:
        return 1
    if steps == 2:
        return 2
    step = 2
    pre, cur = 1, 2
    while step < steps:
        pre, cur = cur, pre + cur
        step += 1
    return cur


def test_one_two_step():
    assert one_two_step_recursive(0) == 0
    assert one_two_step_recursive(1) == 1
    assert one_two_step_recursive(2) == 2
    assert one_two_step_recursive(3) == 3
    assert one_two_step_recursive(4) == 5
    assert one_two_step_recursive(7) == 21

    assert one_two_step_iterative(0) == 0
    assert one_two_step_iterative(1) == 1
    assert one_two_step_iterative(2) == 2
    assert one_two_step_iterative(3) == 3
    assert one_two_step_iterative(4) == 5
    assert one_two_step_iterative(7) == 21


if __name__ == '__main__':
    test_one_two_step()
