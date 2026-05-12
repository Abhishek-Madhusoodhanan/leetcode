# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        # hashmap
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


