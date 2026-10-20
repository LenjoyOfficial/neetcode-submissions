class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        amap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in amap:
                if i < amap[diff]:
                    return [i, amap[diff]]
                else:
                    return [amap[diff], i]
            else:
                amap[nums[i]] = i