'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'
'''

# Beats 68% in runtime, 40% in memory

# Stack functions: .append(), .pop() or stack[:-1], stack[-1] for top elem, 
# len(stack) == 0 for empty check 

class Solution:
    def isValid(self, s: str) -> bool:
        # Stack functions: .append(), .pop(), stack[-1] for top elem, 
        stack = []
        check = {'(':0, '{':1, '[':2, ')':0, '}':1, ']':2}
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                elif check[c] == check[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

        