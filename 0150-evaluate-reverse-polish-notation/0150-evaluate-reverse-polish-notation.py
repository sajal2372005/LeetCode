class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {'+','-','*','/'}
        for i in range(len(tokens)):
            if tokens[i] not in operator:
                stack.append(int(tokens[i]))
            elif tokens[i] in operator:
                first = stack.pop()
                second = stack.pop()
                result = 0
                if tokens[i] == '*':
                    result = second * first
                elif tokens[i] == '+':
                    result = second + first
                elif tokens[i] == '-':
                    result = second - first
                elif tokens[i] == '/':
                    result = int(second / first)
                stack.append(result)
        return stack.pop()