from typing import Callable, List
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_int(s: str) -> bool:
            return s.isnumeric() or (len(s) > 1 and s[0] in '-+' and s[1:].isnumeric())

        def fn_from_op(op: str) -> Callable[[int, int], int]:
            match op:
                case '+':
                    return lambda a, b: a + b
                case '-':
                    return lambda a, b: a - b
                case '*':
                    return lambda a, b: a * b
                case '/':
                    return lambda a, b: math.trunc(a / b) # `//` rounds down
                case _:
                    assert False

        stack = []
        for tok in tokens:
            if is_int(tok):
                stack.append(int(tok))
            else:
                b, a = stack.pop(), stack.pop()
                f = fn_from_op(tok)
                stack.append(f(a, b))

        assert len(stack) == 1
        return stack.pop()
