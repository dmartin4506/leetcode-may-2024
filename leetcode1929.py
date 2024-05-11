"""Prompt is as follows:
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
"""

#Solution is below:

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #the length of the input array 
        n = len(nums) 
        #set ans array to be twice the length of nums
        ans = [0] * (2 * n)

        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]

        return ans