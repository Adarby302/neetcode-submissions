class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        chckr = set()

        for i in nums:
            if i in chckr:
                return True
            else:
                chckr.add(i)
    

        return False
         