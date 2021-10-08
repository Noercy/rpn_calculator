# package calculator

from math import nan
from enum import Enum

# A calculator for rather simple arithmetic expressions.
# Your task is to implement the missing functions so the
# expressions evaluate correctly. Your program should be
# able to correctly handle precedence (including parentheses)
# and associativity - see helper functions.
# The easiest way to evaluate infix expressions is to transform
# them into postfix expressions, using a stack structure.
# For example, the expression 2*(3+4)^5 is first transformed
# to [ 3 -> 4 -> + -> 5 -> ^ -> 2 -> * ] and then evaluated
# left to right. This is known as Reverse Polish Notation,
# see: https://en.wikipedia.org/wiki/Reverse_Polish_notation
#
# NOTE:
# - You do not need to implement negative numbers
#
# To run the program, run either CalculatorREPL or CalculatorGUI

MISSING_OPERAND: str = "Missing or bad operand"
DIV_BY_ZERO: str = "Division with 0"
MISSING_OPERATOR: str = "Missing operator or parenthesis"
OP_NOT_FOUND: str = "Operator not found"
OPERATORS: str = "+-*/^"



class Assoc(Enum):
    LEFT = 1
    RIGHT = 2


tokens = "7+(8*(3^2)+4)"
tokenss = "4+4*2/(1-5)"
tokensss = "2+1*((9^2)+1-10)/7"


def get_associativity(op: str):
    if op in "+-*/":
        return Assoc.LEFT
    elif op in "^":
        return Assoc.RIGHT
    else:
        return ValueError(OP_NOT_FOUND)


def get_precedence(op: str):
    op_switcher = {
        "+": 2,
        "-": 2,
        "*": 3,
        "/": 3,
        "^": 4
    }
    return op_switcher.get(op, ValueError(OP_NOT_FOUND))

# all numbers over 9 turns into multiple tokens and should be put together, that or not use strings for this
# actually doesnt matter since you want to convert it back into ints for the actual calculation
def infix_to_postfix(tokens):
    temp = []
    postfix = []  # make it stack later
    for i in tokens:
        if i in "+-*/^":  # could make into a class or dictionary
            print("")
            print(i)
            print(temp)
            print("new line")
            if len(temp) == 0:
                temp.append(i)
                print("empty")
            elif temp[-1] == "(":
                print("only twice")
                print(temp[-1])
                temp.append(i)
            else:
                print("rsad")
                print(i)
                print(temp)
                print(postfix)
                precd_val = get_precedence(i)
                temp_precd_val = get_precedence(temp[-1])
                print("for last +")
                print(precd_val)
                print(temp_precd_val)
                current_assoc = get_associativity(i)
                if ((current_assoc == Assoc.LEFT) and (precd_val <= temp_precd_val)) or ((current_assoc == Assoc.RIGHT) and (precd_val < temp_precd_val)):
                    postfix.append(temp[-1])
                    print(postfix)
                    print(temp[-1])
                    print("look here")
                    temp.pop()
                    print(temp)
                temp.append(i)
                print(temp)
        elif i == "(":
            temp.append(i)
        elif i == ")":
            for q in reversed(temp):
                if q == "(":
                    temp.pop()
                    break
                postfix.append(q)
                temp.pop()
        else:
            postfix.append(i)
            print(postfix)
    for remaining_operator in reversed(temp):
        print(temp)
        print("test")
        postfix.append(remaining_operator)
        temp.pop()
    temp.clear()
    return postfix


test = infix_to_postfix(tokensss)
print(test)


def apply_operator(op: str, d1: float, d2: float):
    op_switcher = {
        "+": d1 + d2,
        "-": d2 - d1,
        "*": d1 * d2,
        "/": nan if d1 == 0 else d2 / d1,
        "^": d2 ** d1
    }
    return op_switcher.get(op, ValueError(OP_NOT_FOUND))


# -----  Evaluate RPN expression -------------------
def eval_postfix(postfix_tokens):
    op = "+-*/^"
    stack = []
    for i in postfix_tokens:
        if i in op:
            d1 = stack[-1]
            d2 = stack[-2]
            y = apply_operator(i, d1, d2)
            stack.pop()
            stack.pop()
            stack.append(y)
        else:
            i = float(i)
            stack.append(i)
    return stack[0]


   # return 0  # TODO


# Method used in REPL
def eval_expr(expr: str):
    if len(expr) == 0:
        return nan
    tokens = expr.split()
    postfix_tokens = infix_to_postfix(tokens)
    return eval_postfix(postfix_tokens)



def get_precedence(op: str):
    op_switcher = {
        "+": 2,
        "-": 2,
        "*": 3,
        "/": 3,
        "^": 4
    }
    return op_switcher.get(op, ValueError(OP_NOT_FOUND))






# ---------- Tokenize -----------------------
def tokenize(expr: str):
    return expr.split(" ")  # TODO

# TODO Possibly more methods
