class Solution:

    def encode(self, strs: List[str]) -> str:
        final = ""
        for i in strs:
            l = len(i)
            final = final + str(l)+ "#" + i
        return final


    def decode(self, s: str) -> List[str]:
        final = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j+length+1
            final.append(s[j+1:i])
        return final

