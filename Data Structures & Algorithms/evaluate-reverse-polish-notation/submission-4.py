class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = "+-*/"
        stack = []
        for i in range(len(tokens)):
            #print(stack)
            if tokens[i] not in operators:
                stack.append(tokens[i])
            else:
                numOne = int(stack.pop())
                numTwo = int(stack.pop())
                
                if tokens[i] == "+":
                    stack.append(numOne + numTwo)
                elif tokens[i] == "-":
                    stack.append(numTwo - numOne)
                elif tokens[i] == "*":
                    stack.append(numOne * numTwo)
                elif tokens[i] == "/":
                    stack.append(int(numTwo / numOne))
            # print(stack)
            # print()
        return int(stack[0])
