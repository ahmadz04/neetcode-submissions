class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array in place
        nums.sort()
        result = []
        # set up pointers and res arr
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # <-- skip duplicate first elements
            left = i + 1
            right = len(nums) - 1
            if nums[i] > 0:
                return result
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    newlist = [nums[i], nums[left], nums[right]]
                    result.append(newlist)
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1   # skip duplicate left values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1  # skip duplicate right values
                if total > 0:
                    right -= 1
                if total < 0:
                    left += 1
        return result
