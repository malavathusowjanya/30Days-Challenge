class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c=0
        l=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    c+=1
            l.append(c)
            c=0
        return l