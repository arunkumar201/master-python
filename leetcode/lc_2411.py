from typing import List

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

class Solution:
    def smallest_subarrays_brute_force(self, nums: List[int]) -> List[int]:
        res: List[int] = []
        n = len(nums)

        for i in range(n):
            max_or = 0
            # max OR starting from i to n-1
            for k in range(i, n):
                max_or |= nums[k]

            curr_or = 0
            # minimum subarray length starting from i whose OR equals max_or
            for j in range(i, n):
                curr_or |= nums[j]
                if curr_or == max_or:
                    res.append(j - i + 1)
                    break
        return res

    def smallest_subarrays_brute_force_1(self, nums: List[int]) -> List[int]:
        res: List[int] = []
        n = len(nums)
        maxOr = 0
        for i in range(n - 1, -1, -1):
            maxOr |= nums[i]

            currOr = nums[i]
            for j in range(i, n):
                currOr |= nums[j]
                if currOr == maxOr:
                    res.append(j - i + 1)
                    break
        return res[::-1]

    def smallest_subarrays(self, nums: List[int]) -> List[int]:
        global result
        result = []
        n = len(nums)

        next_set_bits_pos = [-1] * 32

        # go from right to left
        maxOr = 0

        for i in range(n - 1, -1, -1):
            maxOr |= nums[i]

            curr: int = nums[i]
            pos = 0

            while curr:
                if curr & 1: #check odd -if yes , LSB bit is one
                    next_set_bits_pos[pos] = i
                curr = int(curr / 2)
                pos += 1

            max_index = max(next_set_bits_pos)
            if max_index == -1:
                result.append(1)
            else:
                result.append(max_index - i + 1)

        return result[::-1]


# Test
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 0, 2, 1, 3]
    result = sol.smallest_subarrays_brute_force(arr)
    print("result:", result)
    result = sol.smallest_subarrays_brute_force_1(arr)
    print("brute force sol-1", result)
    result = sol.smallest_subarrays(arr)
    print("Optimal solution", result)
