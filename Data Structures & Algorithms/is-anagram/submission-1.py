class Solution: #solution not using a second dictionary. space = O(N), 1 dictionary extra space. Time is O(N) have to iterate through all keys
    def isAnagram(self, s: str, t: str) -> bool:
        wrdbk = {} 
        for i in s:
            if i not in wrdbk:
                wrdbk[i] = 1
            else:
                wrdbk[i] += 1     
        for i in t:
            if i in wrdbk:
                wrdbk[i] -= 1
            else:
                return False
        for key in wrdbk:
            if wrdbk[key] == 0:
                continue
            else:
                return False   
        return True
            


        

    
            
