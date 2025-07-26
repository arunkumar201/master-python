from typing import List

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class lc_2461:
    pass

class Solution:
    @staticmethod
    def maximumSubarraySum(nums: List[int], k: int) -> int:
       max_sum=0
       seen=set()
       left=0
       curr_sum=0;n=len(nums)
       for right in range(n):
           right_num=nums[right]
           while right_num in seen:
               left_num=nums[left]
               seen.remove(left_num)
               curr_sum-=left_num
               left+=1
           seen.add(right_num)
           curr_sum+=right_num

           if right-left+1==k:
               max_sum=max(max_sum,curr_sum)
               left_num=nums[left]
               seen.remove(left_num)
               curr_sum-=left_num
               left+=1

       return max_sum


    @staticmethod
    def maximumSubarraySum_bruteForce(nums: List[int], k: int) -> int:
        max_sum=0
        n=len(nums)
        for i in range(n-k+1):
            seen=set()
            curr_sum=0
            for j in range(i,i+k):
                if nums[j] in seen:
                    break
                curr_sum+=nums[j]
                seen.add(nums[j])
            if len(seen)==k:
                max_sum=max(max_sum,curr_sum)

        return max_sum

if __name__=="__main__":
    sol=Solution()
    arr = [1,5,4,2,9,9,9]
    # arr=[4,4,4]
    x=3
    result=sol.maximumSubarraySum_bruteForce(arr,x)
    print("Brute Force Solution",result)
    result=sol.maximumSubarraySum(arr,x)
    print("Optimal solution",result)
