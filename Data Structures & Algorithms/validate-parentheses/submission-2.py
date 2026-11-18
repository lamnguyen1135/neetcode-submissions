class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        # if len(s) == 1:
        #     return False
            
        stack = []
        open = ['(', '{', '[']
        close =  [')', '}', ']']
        for i in range(len(s)):
            if s[i] in open:
                stack.append(s[i])
            elif s[i] in close:
                if len(stack) == 0:
                    return False
                k = stack[-1]
                if s[i] == ')' and k != '(':
                    return False
                elif s[i] == '}' and k != '{':
                    return False
                elif s[i] == ']' and k != '[':
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False
        