class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(index, path, currentsum):
            if currentsum == target:
                result.append(path[:])
                return
            
            if currentsum > target or index == len(nums):
                return
            
            backtrack(index+ 1, path, currentsum)
            path.append(nums[index])
            backtrack(index, path, currentsum + nums[index])
            path.pop()
        backtrack(0, path, 0)
        return result        