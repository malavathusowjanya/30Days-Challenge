class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num == pow(floor(sqrt(num)), 2)