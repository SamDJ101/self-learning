class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        for i in strs:
            s = ''.join(sorted(i))
            dict1[s].append(i)
        return dict1.values()
        