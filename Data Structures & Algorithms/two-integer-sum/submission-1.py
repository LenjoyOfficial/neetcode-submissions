class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        amap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in amap:
                return [amap[diff], i]
            else:
                amap[num] = i