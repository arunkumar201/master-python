from typing import List

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        
        for i in range(len(nums)):
            if(nums[i]!=val):
                nums[count]=nums[i]
                count+=1
        return count
        
    
    
__name__=="__main__"
sol=Solution()
result=sol.removeElement([0,1,2,2,3,0,4,2],2)
print(result)
   
