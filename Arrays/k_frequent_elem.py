'''
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
 
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 
Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.'''

# Beats 98.8% in runtime, 91.6% in memory
# Sorting dictionary by value after dynamic programming
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        sorted_dict = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}    
        lst=list(sorted_dict.keys())
        lst = lst[::-1]
        return lst[:k]