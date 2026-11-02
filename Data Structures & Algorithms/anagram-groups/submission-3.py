class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        for s in strs:
            sort = ''.join(sorted(s))
            if sort not in out:
                out[sort] = [s]
            else:
                out[sort].append(s)

        return list(out.values())
