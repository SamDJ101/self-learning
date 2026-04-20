class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
            

        freq_list = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        
        result = []
        for i in range(k):
            result.append(freq_list[i][0])
        
        return result


        
        