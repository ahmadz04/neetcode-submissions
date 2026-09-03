class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtrack():
            # Check if done
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            # What choice do I have?
            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack()
                    path.pop()
        backtrack()
        return result

        