class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l=[]
        sum1=0
        for i in range(len(nums)):
            sum1+=nums[i]
            l.append(sum1)

        return l
