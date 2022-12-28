def checkBalance(expr):
    stack = []
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:

            # Here we check if the current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            curr_char = stack.pop()
            if curr_char == '(':
                if char != ")":
                    return False
            if curr_char == '{':
                if char != "}":
                    return False
            if curr_char == '[':
                if char != "]":
                    return False

                    # Here we check empty stack
    if stack:
        return False
    return True

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        string = '('
        permuts = []
        self.permuteParanthesis(n, n - 1, string, permuts)
        return permuts


    def permuteParanthesis(self, closed, opened, string, permuts):
        newstring = string
        if opened > 0 and closed > 0:
            newstring += '('
            self.permuteParanthesis(closed, opened - 1, newstring, permuts)

        elif opened > 0 and closed == 0:
            return

        newstring = string
        if closed > 0:
            newstring += ')'
            self.permuteParanthesis(closed - 1, opened, newstring, permuts)

        if closed == 0 and opened == 0:
            if checkBalance(newstring):
                permuts.append(newstring)