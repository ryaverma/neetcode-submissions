class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = {}
        for i, val in enumerate(nums):
            two_sum[val] = i
        for i, val in enumerate(nums):
            diff = target-val
            if diff in two_sum and two_sum[diff]!=i:
                return [i, two_sum[diff]]
        return []