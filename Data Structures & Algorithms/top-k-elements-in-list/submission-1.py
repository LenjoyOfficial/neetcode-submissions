class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for n in nums:
            if n in dict:
                dict[n] += 1
            else:
                dict[n] = 1
        buckets = {x: [] for x in range(len(nums) + 1)}
        for key, v in dict.items():
            buckets[v].append(key)
        
        out = []
        for i in range(len(nums), -1, -1):
            if len(out) < k:
                for n in buckets[i]:
                    out.append(n)
        return out