class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap = {}
        for c in s:
            if c not in smap:
                smap[c] = 1
            else:
                smap[c] = smap[c] + 1

        tmap = {}
        for c in t:
            if c not in tmap:
                tmap[c] = 1
            else:
                tmap[c] = tmap[c] + 1
        
        return smap == tmap