class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            ans = 0
            if i not in {'+','-','*','/'}:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()

                if i == '+':
                    ans = a+b
                elif i == '-':
                    ans = a-b
                elif i == '*':
                    ans = a*b
                elif i == '/':
                    ans = int(a/b)

                stack.append(ans)
        
        return stack[-1]
