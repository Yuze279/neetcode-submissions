class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap = {}

        for i, n, in enumerate(nums):
            diff = target - n
            if diff in preMap:
                return [preMap[diff], i] #sub Value
            #pass a list and check the values before it
            
            preMap[n] = i
        return 
        


        """
        for i in range(0, len(nums)): 
            for j in range(i+1, len(nums)): 
                if nums[i] + nums[j] == target: 
                    return [i, j]
        """