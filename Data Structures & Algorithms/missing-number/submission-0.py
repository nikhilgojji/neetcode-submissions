class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start = 0
        while start <= len(nums):
            if start not in nums:
                return start
            start += 1
        