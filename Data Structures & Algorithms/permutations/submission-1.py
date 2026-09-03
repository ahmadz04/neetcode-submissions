class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path):
            # Check if done
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            # What choice do I have?
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()
        backtrack([])
        return result

        