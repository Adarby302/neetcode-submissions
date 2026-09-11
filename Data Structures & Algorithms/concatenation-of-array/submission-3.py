class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        count, i = 0,0
        size = len(nums) * 2
        ans = [None] * size
        while i < size:
            ans[i] = nums[count]
            if count == len(nums) -1:
                count = -1 
            count+=1
            i+= 1
        return ans 

            
    
        
    
        