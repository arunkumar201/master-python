from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        for i in range(1, n - 1):
            # Skip if same as previous
            if nums[i] == nums[i - 1]:
                continue

            # Find closest non-equal to the left
            left = i - 1
            while left >= 0 and nums[left] == nums[i]:
                left -= 1

            # Find closest non-equal to the right
            right = i + 1
            while right < n and nums[right] == nums[i]:
                right += 1

            # Check if both sides exist
            if left >= 0 and right < n:
                if nums[i] > nums[left] and nums[i] > nums[right]:
                    count += 1  # Hill
                elif nums[i] < nums[left] and nums[i] < nums[right]:
                    count += 1  # Valley

        return count

    def countHillValley1(self, nums: List[int]) -> int:
        n = []
        count = 0
        n.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                n.append(nums[i])
        print("after rm consecutive. duplicates ", n)
        for i in range(1, len(n) - 1):
            if n[i] > n[i + 1] and n[i] > n[i - 1]:
                count += 1 #hill
            elif n[i] < n[i + 1] and n[i] < n[i - 1]:
                count += 1 #valley
        return count


if __name__ == "__main__":
    sol = Solution()
    arr = [6, 6, 5, 5, 4, 1]
    result = sol.countHillValley(arr)
    print("Result:", result)
    result = sol.countHillValley1(arr)
    print(f"using extra arr {result}")
