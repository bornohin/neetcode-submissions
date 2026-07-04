class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            curr = nums[i]
            if target - curr in seen:
                return [seen[target - curr], i]
            else:
                seen[curr] = i
        