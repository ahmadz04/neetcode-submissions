class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(index, path, current_sum):
            if current_sum == target:
                result.append(path[:])
                return
            
            if current_sum > target or index == len(nums):
                return

            backtrack(index + 1, path, current_sum)

            path.append(nums[index])
            backtrack(index, path, current_sum + nums[index])
            path.pop()
        backtrack(0, [], 0)
        return result        