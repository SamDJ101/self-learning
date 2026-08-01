class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Charset = set()
        max_length = 0
        l = 0
        for r in range(len(s)):
            while(s[r] in Charset):
                Charset.remove(s[l])
                l+=1
            Charset.add(s[r])
            max_length = max(max_length, len(Charset))
            

        return max_length




                
                
                

