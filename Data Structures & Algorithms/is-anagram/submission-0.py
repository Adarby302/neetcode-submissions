class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wrdbk = {} 
        wrdbk2 = {} 
        res = True

        for i in s:
            if i not in wrdbk:
                wrdbk[i] = 1
            else:
                wrdbk[i] += 1 
        
        for i in t:
            if i in wrdbk:
                wrdbk[i] -= 1
            else:
                print("Returning false word", i)
                return False

        for key in wrdbk:
            if wrdbk[key] == 0:
                continue
            else:
                print("Returning false", key, wrdbk[key])
                return False
        
        return True
            


        
        

    
            
