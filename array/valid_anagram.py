class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}

        for ch in s:
            seen[ch] = seen.get(ch,0)+1

        for ch in t:
            if ch not in seen:
                return False
            seen[ch] -=1
            if seen[ch] == 0:
                del seen[ch]
        return len(seen) ==0
