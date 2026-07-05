class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return Counter(s) == Counter(t)

        if len(s) != len(t):
            return False

        countS = {}
        countT = {} 

        #2 pointer
        #sort the list 
        # or keep a list for every single 
        #value in the list which is cool

        #Built in functions for LIST would be so easy 

        for i in range(len(s)): 
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:  
            #what if it not in T? 
            if countS[c] != countT.get(c, 0):
                return False

        return True