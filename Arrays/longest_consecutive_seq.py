
'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

# Beats 71% in runtime, 28% in memory

# find streak length dynamically as you iterate through list only when you know you're at the edge of a streak

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_Set = set(nums)
        curr_seq = 0
        largest_seq = 0
        for num in nums_Set:
            curr_seq = 1
            if num + 1 in nums_Set:
                continue
            elif num-1 in nums_Set:
                while num-1 in nums_Set:
                    curr_seq = curr_seq + 1
                    num = num-1
            largest_seq = max(largest_seq, curr_seq)
        return largest_seq
                