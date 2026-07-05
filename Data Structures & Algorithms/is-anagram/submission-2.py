class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
   
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



        #string = set(s)