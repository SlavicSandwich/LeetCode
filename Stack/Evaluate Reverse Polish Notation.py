def get_znak(val):
    if val > 0:
        return 1
    if val == 0:
        return 0
    if val < 0:
        return -1
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for k in tokens:
            if k.isnumeric() or len(k) > 1 and int(k):
                stack.append(int(k))
            else:
                digit1 = stack.pop(-1)
                digit2 = stack.pop(-1)
                match k:

                    case '+':
                        stack.append(digit2 + digit1)
                    case '-':
                        stack.append(digit2 - digit1)
                    case '/':
                        stack.append(get_znak(digit2) * get_znak(digit1) * (abs(digit2) // abs(digit1)))
                    case '*':
                        stack.append(digit2 * digit1)

        return stack[0]