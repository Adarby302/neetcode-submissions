class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Subtract target from i, so 7 - 3 -> place into dictionary.
        if key is found in dictionary return the position. 
        so 

        7-3 -> 4 
        key[4]  = 0 

        7-4 -> 3
        key[4] = 0, current index

        '''
        sums = {}

        for i in range(len(nums)):
            if nums[i] in sums:
                return [sums[nums[i]], i]
            
            k = target - nums[i]
            print("entering ", k, "and", i)
            sums[k] = i
            

        
        return []


            
