class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set()
        for num in nums:
            if num in x:
                return True
            if num not in x:
                x.add(num)
        return False
