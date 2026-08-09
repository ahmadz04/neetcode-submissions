class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1 
        while k != 0:
            # Get the highest value from hashmap and append it to res
            highest_value = max(hashmap, key=hashmap.get)
            res.append(highest_value)
            hashmap.pop(highest_value)
            k -= 1
        return res
        

        