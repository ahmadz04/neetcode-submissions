class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap1 = {}
        for i in range(len(nums)):
            need_value = target - nums[i]
            if need_value in hashmap1:
                return [hashmap1[need_value], i]
            else:
                hashmap1[nums[i]] = i
