class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        l=0
        maxi=0
        r=0
        while r<len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            r+=1
            maxi=max(maxi,r-l)
        return maxi

