class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: If the string is empty
        if not t:
            return ""

        # Two Hashmaps keeping track of chars
        countT = {}
        currentwindow = {}
        res = [-1, -1]
        resLen = float("inf")
        # Add t to the map (because it's just not going to change)
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # Two variables: Have and Need (keeping track of the amount of vars)
        have = 0
        need = len(countT)

        # Start iterating through s
        leftpointer = 0
        for rightpointer in range(len(s)):
            c = s[rightpointer] # Get the char we just reached
            currentwindow[c] = 1 + currentwindow.get(c, 0) # Put c into the currentwindow hashmap

            # Does this count satisfy what we were looking for? Does the char exist in T and also match the count
            if c in countT and currentwindow[c] == countT[c]:
                have += 1

            # Does have equal need? If so we need to run a loop
            while have == need:
                # If the len of the current window is less than the stored result, update it to this window
                if (rightpointer - leftpointer + 1) < resLen:
                    res = [leftpointer, rightpointer]
                    resLen = (rightpointer - leftpointer + 1)
                    
                    # Pop from the left to minimize the window
                currentwindow[s[leftpointer]] -= 1
                # If the character popped is one of the needed chars AND the count in hashmap is less now
                if s[leftpointer] in countT and currentwindow[s[leftpointer]] < countT[s[leftpointer]]:
                    have -= 1
                leftpointer += 1
        leftpointer, rightpointer = res
        return s[leftpointer:rightpointer + 1] if resLen != float("infinity") else ""



