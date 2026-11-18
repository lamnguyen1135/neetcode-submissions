class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0]*n
        j = 0
        for i in range(n):
            temp = temperatures[i]
            j = 1
            while stack and temp > temperatures[stack[-1]]: 
                result[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)
            print(stack)

        return result


            