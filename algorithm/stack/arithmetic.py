# -*- coding: utf8 -*-

"""
realize +,-,*,/ using stacks, ignoring brackets
"""

from typing import Optional

from algorithm.stack.my_array_stack import ArrayStack

operations = ['+', '-', '*', '/']
nums = '0123456789'


def calc_level(operation) -> int:
    if operation in ['+', '-']:
        return 1
    if operation in ['*', '/']:
        return 2


def is_low_priority(op1, op2) -> bool:
    op1_level = calc_level(op1)
    op2_level = calc_level(op2)
    return op1_level <= op2_level


def arithmetic(to_calc: str) -> Optional[float]:
    to_calc = "".join(to_calc.split())
    input_type = []
    for i in to_calc:
        if i in nums:
            input_type.append('num')
        elif i in operations:
            input_type.append('operation')
        else:
            input_type.append('invalid')

    if 'invalid' in input_type:
        return None
    if input_type[0] == 'operation' or input_type[-1] == 'operation':
        return None

    number_stack = ArrayStack(100)
    operation_stack = ArrayStack(100)
    num_start = 0
    for idx, in_type in enumerate(input_type):
        if in_type == 'num':
            continue
        operation = to_calc[idx]
        num = to_calc[num_start: idx]
        num_start = idx + 1
        pre_operation = operation_stack.peek
        if pre_operation is None or not is_low_priority(operation, pre_operation):
            number_stack.push(num)
            operation_stack.push(operation)
        else:
            cur_operation = operation_stack.pop()
            cur_post_number = num
            cur_pre_number = number_stack.pop()
            cur_calc = str(round(eval(cur_pre_number + cur_operation + cur_post_number), 2))
            while not operation_stack.is_empty:
                cur_operation = operation_stack.pop()
                cur_pre_number = number_stack.pop()
                cur_calc = str(round(eval(cur_pre_number + cur_operation + cur_calc), 2))
            number_stack.push(cur_calc)
            operation_stack.push(operation)
    cur_post_number = to_calc[num_start:]
    cur_pre_number = number_stack.pop()
    cur_operation = operation_stack.pop()
    cur_calc = str(round(eval(cur_pre_number + cur_operation + cur_post_number), 2))
    while not operation_stack.is_empty:
        cur_operation = operation_stack.pop()
        cur_pre_number = number_stack.pop()
        cur_calc = str(round(eval(cur_pre_number + cur_operation + cur_calc), 2))

    return float(cur_calc)


def test_arithmetic():
    assert arithmetic('3 +5* 8- 6 ') == 37.00
    assert arithmetic('5*10- 2') == 48.00
    assert arithmetic('5*10/ 2 +7*2-1') == 38.00


if __name__ == '__main__':
    test_arithmetic()
