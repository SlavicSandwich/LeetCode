
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if (s[i].isalpha() or s[i].isdigit()) and (s[j].isalpha() or s[j].isdigit()):
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                    continue
                else:
                    return False

            if not s[i].isalpha() and not s[i].isdigit():
                i += 1

            if not s[j].isalpha() and not s[j].isdigit():
                j -= 1


        return True

print(Solution().isPalindrome("8V8K;G;K;V;"))