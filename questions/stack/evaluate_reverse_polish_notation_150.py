class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                number2 = stack.pop()
                number1 = stack.pop()

                if token == '+':
                    result = number1 + number2
                elif token == '-':
                    result = number1 - number2
                elif token == '*':
                    result = number1 * number2
                elif token == '/':
                    result = int(number1 / number2)

                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]
                    
        '''
        COmplexities = O(n)
        tokens = ["2","1","+","3","*"] | o/p : 9 | ((2 + 1) * 3) = 9
        Stack
            if number
                push to stack
            if operator

        tokens = ["2","1","+","3","*"]
        push 2, push 1 -> stack = [2,1]
        "+" : pop 1,2 -> 1+2 = 3 -> push 3
        push 3 -> [3,3]
        "*" : pop 3,3 -> 3*3 = 9 -> push 9
        return result -> 9

        tokens = ["4","13","5","/","+"]
        push 4, push 13, push 5 -> [4, 13, 5]
        "/" -> pop 5, 13 -> 13/5 = 2 -> [4, 2]
        "+" -> pop 2, 4 -> 4 + 2 -> [6]
        return result -> 6

        Steps:
            1. Handle when to pop
            2. Assign the operator's operations
            3. Add respective result
            4. Return the stack
        '''
