class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = []
        
        # go through list - nums and find the index at that number
        for i in range(len(nums)):  
            diff = target - nums[i]

            #how TF to optimize? 

            # if diff in mset: #         
            for j in range(i+1, len(nums)):
                if diff == nums[j]: 
                    return [i, j]
                

        return []

                # a = nums.index(i)
                # j = nums.index(diff)

                #     list.append(nums.index(i))
                #     list.append(j)
                #     break


    

            # if list.index(diff) == -1: 

                # if 
                # list.append(nums.index(i))
                # list.append(nums.index(diff))
    


       
       
       
       
       
        # preMap = {}

        # for i, n, in enumerate(nums):
        #     diff = target - n
        #     if diff in preMap:
        #         return [preMap[diff], i] #sub Value
        #     #pass a list and check the values before it
            
        #     preMap[n] = i
        # return 
        


        # """
        # for i in range(0, len(nums)): 
        #     for j in range(i+1, len(nums)): 
        #         if nums[i] + nums[j] == target: 
        #             return [i, j]
        # """