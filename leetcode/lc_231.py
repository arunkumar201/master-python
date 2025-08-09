class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        isPowerOfTwo=False

        while n!=0:
            n=n/2
            if n==1:
                return True

        return isPowerOfTwo




if __name__=="__main__":
    sol=Solution()
    n=16
    result=sol.isPowerOfTwo(n)
    print(n,"is Power of two",result)
