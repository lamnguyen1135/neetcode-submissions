class Solution:
    def isValid(self, s: str) -> bool:
        
        openChar = "({["
        closedChar = ")}]"
        stack = []
        i = 0
        
        for i in range(len(s)):
            if s[i] in openChar:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if s[i] == ")" and stack[-1] == "(":
                    stack.pop()
                elif s[i] == "}" and stack[-1] == "{":
                    stack.pop()
                elif s[i] == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False

        if stack:
            return False
        else:
            return True
            
                
                


