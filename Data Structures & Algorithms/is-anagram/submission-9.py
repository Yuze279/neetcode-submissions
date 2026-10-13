class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if len(sorted_s) != len(sorted_t): 
            return False

        
        if len(sorted_s) == len(sorted_t): 
            for i in range(len(sorted_s)):
                if sorted_s[i] != sorted_t[i]:
                    return False
            
        return True
            




        #return sorted(s) == sorted(t)
        
        # if len(s) != len(t): 
        #     return False
 
        # countS, countT = {}, {}

        # for i in range(len(s)): 
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # for c in countS:
        #     if countS[c] != countT.get(c, 0):
        #         return False

        # return True
            
        
    
        #return sorted(list(s)) == sorted(list(t))

        #.items .sorted in the neetcode 

        """
        if len(s) != len(t): 
            return False

        hashset = {}
        hashsett = {}


        for i in s: 
            if i in hashset: 
               hashset[i] +=1 
            else: 
               hashset[i] = 1
        
        for i in t: 
            if i in hashsett:
               hashsett[i] +=1 
            else: 
               hashsett[i] = 1
        
        return hashset == hashsett

        """

        #string = set(s)