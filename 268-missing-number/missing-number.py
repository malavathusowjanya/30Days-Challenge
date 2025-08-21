class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = len(nums)
        s = 0
        for i in range(m+1):
            s += i

        k = sum(nums)
        v = s-k
        return v