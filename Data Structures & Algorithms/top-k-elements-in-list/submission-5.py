class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [[] for i in range(len(nums) + 1)]
        # Create a hashmap for for each num and it's freq
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        for num,count in hashmap.items():
            freq[count].append(num)

        res = []
        freq_rev = freq[::-1]
        for bucket in freq_rev:
            for num in bucket:
                res.append(num)
            if len(res) == k:
                return res
        return res
        
        
        