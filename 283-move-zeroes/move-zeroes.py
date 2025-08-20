class Solution(object):
    def moveZeroes(self, nums):
        pos=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[pos]=nums[i]
                pos=pos+1
        while(pos<len(nums)):
            nums[pos]=0
            pos=pos+1
        print(nums)
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        