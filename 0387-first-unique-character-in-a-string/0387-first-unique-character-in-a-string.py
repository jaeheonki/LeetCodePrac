class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = {}
        for c in s :
            if c in cnt : 
                cnt[c] += 1
            else :
                cnt[c] = 1
        i = 0
        while i < len(s) :
            c = s[i]
            if cnt[c] == 1:
                return i
            i += 1
        return -1