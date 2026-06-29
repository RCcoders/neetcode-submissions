from typing import List
import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv if hasattr(operator, 'truediv') else lambda a, b: float(a)/ b,
        }

        stack = []

        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()

                result = int(operators[token](a, b))
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]