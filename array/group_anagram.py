class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap

        seen = {}
    # scan the strings and return in sort the word alphabetically
        for ch in strs:
            key = " ".join(sorted(ch))
            if key not in seen:
                seen[key] = []
            seen[key].append(ch)
        return list(seen.values())