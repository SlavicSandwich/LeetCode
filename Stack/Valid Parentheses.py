class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        inp = s
        flag = True
        op = ['(', '{', '[']
        cl = [')', '}', ']']
        dict = {"]":'[','}':'{', ')':'('}
        for i in range(len(inp)):
            try:
                if inp[i] in op:
                    stack.append(inp[i])
                elif inp[i] in cl and dict[inp[i]] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            except:
                return False

        if stack:
            return False
        return True