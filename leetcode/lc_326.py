import math


class Solution:
    def isPowerOfThree_iterative(self, n: int) -> bool:
        '''
        time complexity O(log(n) of base 3) and  space complexity O(1) 
        :param n: 
        :return: 
        '''
        if n <= 0:
            return False

        # I'm going to divide by 3 until
        # it is divisible by 3 if final num is 1 then it is power of 3 else not
        while n % 3 == 0:
            n = n / 3
        return n == 1 if True else False

    def isPowerOfThree_recursive(self, n: int) -> bool:
        '''
         time complexity O(logN of base 3) same space complexity
        :param n: 
        :return: 
        '''
        if n <= 0:
            return False

        if n == 1:
            return True

        # I'm going to divide by 3 until
        # it is divisible by 3 if final num is 1 then it is power of 3 else not
        if n % 3 != 0:
            return False
        return self.isPowerOfThree_recursive(n // 3)

    def isPowerOfThree_log(self, n: int) -> bool:
        '''
        time complexity O(1)
        space complexity O(1)
        :param n:
        :return:
        '''
        if n <= 0:
            return False
        # how we are going to log to check
        # as we know n is power of 3
        # if 3^x==n or x==log(n)/log(3) is a valid integer then it is a power of 3
        # in java log(n)/log(3) is written as Math.log(n)/Math.log(3) we stored them in Double type
        x = math.log(n, 3)
        y = int(round(x))
        return abs(x - y) < 1e-12

    def isPowerOfThree(self, n: int) -> bool:
        # max integer is 2^31-1
        # max integer that is power of 3 is 1162261467 or 3^19
        if n <= 0:
            return False
        max_power_of_3 = math.pow(3, 19)
        return max_power_of_3 % 3 == 0


if __name__ == "__main__":
    sol = Solution()
    n = 243
    print("Iterative solution")
    result: bool = sol.isPowerOfThree_iterative(n)
    print(f"Result {result}")
    print("Recursive solution")
    result: bool = sol.isPowerOfThree_recursive(n)
    print(f"Result {result}")
    print("Math log solution")
    result: bool = sol.isPowerOfThree_log(n)
    print(f"Result {result}")
    print("direct solution")
    result: bool = sol.isPowerOfThree(n)
    print(f"Result {result}")

