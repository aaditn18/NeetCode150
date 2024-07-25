'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
'''

# Beats 83% in runtime, 64% in memory

# Implementation w stack: keep start w stack size 1, pop and append operated partial results onto stack
# when operated partial result is fully computed pop it off and push it on to a final answer
# do this repeatedly

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = ["("]
        length = 1
        ans =[]
        while stack != []:
            elem = stack.pop()
            if len(elem) == 2*n:
                ans.append(elem)
                continue
            countL = elem.count("(")
            countR = elem.count(")")
            if countL == countR:
                stack.append(elem + "(")
            elif countL == n:
                stack.append(elem + ")") 
            else:
                stack.append(elem + "(") 
                stack.append(elem + ")")
            
        return ans
            
        # Following code works, but no stack used
        # ans = ["("]
        # i=1
        # while i<2*n:
        #     ans_copy = []
        #     for comb in ans:
        #         countL = comb.count("(")
        #         countR = comb.count(")")
        #         if countL == countR:
        #             ans_copy.append(comb + "(")
        #         elif countL == n:
        #             ans_copy.append(comb + ")") 
        #         else:
        #             ans_copy.append(comb + "(") 
        #             ans_copy.append(comb + ")")
        #     ans = ans_copy   
        #     i=i+1
        # return ans

        