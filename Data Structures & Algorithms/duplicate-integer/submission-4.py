class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0 
        num_dict = {}


        for i in nums: 
            if i in num_dict: 
                return True; 

            else: 
                num_dict[i] = 1
            
        return False
            