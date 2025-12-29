class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {')' : '(', '}' : '{', ']' : '['}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'

                if mapping[char] != top_element:
                    return False

            else:
                stack.append(char)

        return not stack
        '''
        Stack to keep track of opening brackets
            '(', '{', '[' -> push it to the stack
            ')', '}', ']' -> 
                - check if the stack is empty
                    if yes : False
                - pop from stack and check the closing bracket
                    if no match : False
        
        Dry run:
            s = "()"
                '(' - push to the stack => ['(']
                ')' - pop '('
                    check that it matches
                        stack -> []
                    return True

        '''
        # bracket_map = {')': '(', '}': '{', ']': '['}

        # stack = []

        # for char in s:
        #     if char in bracket_map:
        #         top_element = stack.pop() if stack else '#'

        #         if bracket_map[char] != top_element:
        #             return False
            
        #     else:
        #         stack.append(char)

        # return len(stack) == 0



'''
Input: s = "()"
Output: true

Iterate through '(': Push '(' -> Stack: ['(']
Iterate through ')': 
'''
        
