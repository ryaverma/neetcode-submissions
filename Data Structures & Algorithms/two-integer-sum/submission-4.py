class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = {}
        for i, val in enumerate(nums):
            diff = target-val
            if diff in two_sum:
                return [two_sum[diff], i]
            two_sum[val] = i