#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Div.py
@time: 2019/9/15 19:55
@desc: 除法(div)指令
"""

import math

from ch10.instructions.base.Instruction import NoOperandsInstruction


# double div
class DDIV(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        v2 = stack.pop_double()
        v1 = stack.pop_double()
        if v2 == 0.0:
            result = math.inf
        else:
            result = v1 / v2
        stack.push_double(result)


# float div
class FDIV(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        v2 = stack.pop_float()
        v1 = stack.pop_float()
        if v2 == 0.0:
            result = math.inf
        else:
            result = v1 / v2
        stack.push_float(result)


# int div
class IDIV(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        if v2 == 0:
            raise RuntimeError("java.lang.ArithmeticException: / by zero")
        result = int(v1 / v2)
        stack.push_numeric(result)


# long div
class LDIV(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        if v2 == 0:
            raise RuntimeError("java.lang.ArithmeticException: / by zero")
        result = int(v1 / v2)
        stack.push_numeric(result)
