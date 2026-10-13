class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nset = []

        for i in nums: 
            if i in nset: 
                return True 
            nset.append(i)

        return False





        # count = {} 
        # for i in nums: 
        #     if i in count: 
        #         return True
        #     count[i] = count.get(i, 0) + 1
        # return False 





        # count = {}

        # for i in nums: 
        #     count[i] = count.get(i, 0) + 1
        #     if count[i] > 1:
        #         return True
        # return False




