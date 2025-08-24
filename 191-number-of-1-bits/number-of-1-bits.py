class Solution:
    def hammingWeight(self, n: int) -> int:
        m = bin(n)
        k = str(m)
        return k.count('1')