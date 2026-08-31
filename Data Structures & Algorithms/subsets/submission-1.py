class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            

            # Don't pick num
            backtrack(i + 1)

            # Pick num
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
        backtrack(0)
        return res