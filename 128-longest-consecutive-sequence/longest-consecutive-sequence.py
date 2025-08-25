from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(set(nums))  
        longest = 1
        cur_streak = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:  
                cur_streak += 1
            else: 
                longest = max(longest, cur_streak)
                cur_streak = 1
        
        return max(longest, cur_streak)
