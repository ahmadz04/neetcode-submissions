class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Using a hashset:
        # Hashset works but I have to pass test cases such as xx and x. That means one needs to have count

        # Using a hashmap to keep count:
        # Initialize a hashmap
        # For every element in s:
            # Add it to the hashmap with count 1. If it's being repeated, increase the count
        # For every element in t:
            # Add it to the hashmap in the same manner.
        
        
            # If it doesn't already exist in the hashmap:
                # return False
            # Add increase it's count in the hashmap
        hashmap = {}
        hashmap1 = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        for j in t:
            hashmap1[j] = hashmap1.get(j, 0) + 1

        if hashmap == hashmap1:
            return True
        return False
        
 
        

        