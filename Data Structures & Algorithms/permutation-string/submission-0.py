class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: s1 cannot be in s2 if it's longer
        if len(s1) > len(s2):
            return False
            
        map1 = [0] * 26
        map2 = [0] * 26
        
        # 1. Initialize the first window of size len(s1)
        for i in range(len(s1)):
            map1[ord(s1[i]) - ord('a')] += 1
            map2[ord(s2[i]) - ord('a')] += 1
            
        # Check if the very first window is a match
        if map1 == map2:
            return True
            
        # 2. Slide the window across the rest of s2
        l = 0
        for r in range(len(s1), len(s2)):
            # Add the new character on the right
            map2[ord(s2[r]) - ord('a')] += 1
            
            # Remove the old character on the left
            map2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            
            # Check if the updated window matches
            if map1 == map2:
                return True
                
        return False