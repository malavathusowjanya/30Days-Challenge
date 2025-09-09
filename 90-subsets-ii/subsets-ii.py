class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        l=[[]]
        nums.sort()
        s=0

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                n = [curr + [nums[i]] for curr in l[s:]]
            else:
                n = [curr + [nums[i]] for curr in l]

        
            s = len(l)
            l.extend(n)

        return l

        