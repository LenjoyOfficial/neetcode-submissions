class Solution:
    def encode(self, strs: list[str]) -> str:
        enc = ""
        for s in strs:
            enc += str(len(s)) + "#" + s
        return enc
        
    def decode(self, s: str) -> list[str]:
        dec = []
        while len(s) > 0:
            out = self.parse_next(s)
            dec.append(out)

            l = len(str(len(out))) + len(out) + 1
            s = s[l:]
        return dec

    def parse_next(self, s: str) -> str:
        ls = ""
        i = 0
        while s[i] != '#':
            ls += s[i]
            i+=1

        l = int(ls)
        i+=1
        out = ""
        while l > 0:
            out += s[i]
            i+=1
            l-=1

        return out