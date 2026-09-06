class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        l = 0
        r = len(nums) - 1
        result = []
        
        while l < r:
            if nums[l] + nums[r] > target:
                r -= 1
            if nums[l] + nums[r] < target:
                l += 1
            if nums[l] + nums[r] == target:
                return [l + 1, r + 1]  
        