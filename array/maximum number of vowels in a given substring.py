# Maximum Number of Vowels in a Substring of Given Length
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.



#  answers

class Solution:
    def maxVowels(self, s: str, k: int) -> int:

         

# Correct Thinking Flow 🧠
# Step 1

# Count vowels in first window.
        left = 0
        max_count = 0
        count = 0
        for right in range(k):
            if s[right] in "aeiou":
                count +=1        
# Step 2

# Store:
            max_count = count


# Step 3

# Slide window.

# When sliding:

# add new char
        for right in range(k,len(s)):
            if s[right] in "aeiou":
                count +=1
# remove old char
            if s[left] in "aeiou":
                count -=1

# update max
            left +=1

            max_count = max(max_count,count)
# move left
            
        return max_count

