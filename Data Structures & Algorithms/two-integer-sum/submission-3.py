class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = defaultdict(int)
        for i, value in enumerate(nums):
            result = target - value
            if result in x:
                return [x[result], i]
            else:
                x[value] = i
                