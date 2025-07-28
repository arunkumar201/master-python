class Solution:
    def fib(self, n: int) -> int:
        pass

    def fib_brute_force(self, n: int) -> int:
        """
         Time Complexity - O(2^N)
         space Complexity- O(N)
        :param n:
        :return:
        """
        if n <= 1:
            return n
        return self.fib_brute_force(n - 1) + self.fib_brute_force(n - 2)

    def fib_using_dp(self, n: int) -> int:
        """
         Time Complexity - O(N)
         space Complexity- O(N)
        :param n:
        :return:
        """
        dp = []
        dp=[0]*(n+1)


        if n <= 1:
            return n

        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def fib_optimal_sol(self,n:int)->int:
        if n<=1:
            return n

        prev=0
        nextPrev=1

        for i in range(2,n+1):
            curr_sum=prev+nextPrev
            temp=prev
            prev=curr_sum
            nextPrev=temp

        return nextPrev+prev




if __name__ == "__main__":
    sol = Solution()
    n = 12
    result = sol.fib_brute_force(n)
    print("Brute Force Solution", result)
    result = sol.fib_using_dp(n)
    print("Using DP", result)
    result=sol.fib_optimal_sol(n)
    print("Optimal Solution",result)

