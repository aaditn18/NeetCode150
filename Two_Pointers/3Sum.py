
'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 
Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

# Beats 20% in runtime and 32% in memory, but same time complexity, n^2

# Solution: sort list first to avoid duplicate triplets in result, then
#           for all possible left most elems of triplets, do two sum 
#           (using 2 pointers, one on each end of the sublist) 

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        ans = []
        for i in range(length-1):
            if i>0 and nums[i] == nums[i-1]:
                continue
            m, r = i+1, length-1
            targ = -nums[i]
            while m < r:
                if nums[m] == nums[m-1] and m-1 > i:
                    m=m+1
                    continue
                elif r+1 < length and nums[r] == nums[r+1]:
                    r=r-1
                    continue
                elif nums[m] + nums[r] == targ:
                    ans.append([nums[i], nums[m], nums[r]])
                    m = m+1
                    r = r-1
                elif nums[m] + nums[r] > targ:
                    r = r-1
                else:
                    m = m+1
        return ans