'''
Problem Statement:Given an array arr[] containing integers and an integer k,
your task is to find the length of the longest subarray where the sum of its
elements is equal to the given value k.
If there is no subarray with sum equal to k, return 0.
'''
class Solution:
    """
    Problem Statement:Given an array arr[] containing integers and an integer k,
    your task is to find the length of the longest subarray where the sum of its
    elements is equal to the given value k.
    If there is no subarray with sum equal to k, return 0.
    """
    def longest_subarray_brute_force(self, arr, k):
        '''
        Time Complexity=O(N^2)
        Space Complexity= O(N)
        :param arr:
        :param k:
        :return:
        '''
        n = len(arr)
        max_len = 0

        for left in range(n):
            curr_sum = 0
            for right in range(left, n):
                curr_sum += arr[right]
                if curr_sum == k:
                    max_len = max(max_len, right - left + 1)
        return max_len

    def longest_subarray_optimized(self, arr, k):
        '''
        Time Complexity=O(N+N) ~O(2N) ~O(N)
        Space Complexity= O(1)
        :param arr:
        :param k:
        :return:
        '''
        n = len(arr)
        left, right = 0, 0
        max_len = 0
        curr_sum = 0
        prefix_sum_map = {0: -1}
        while right < n:
            curr_sum += arr[right]

            if (curr_sum - k) in prefix_sum_map:
                max_len = max(max_len, right - prefix_sum_map[curr_sum - k])

            if curr_sum not in prefix_sum_map:
                prefix_sum_map[curr_sum] = right

            right += 1
        return max_len


if __name__ == "__main__":
    sol = Solution()
    arr = [10, 5, 2, 7, 1, -10]
    k = 15
    print("Brute Force Solution")
    result = sol.longestSubarray_bruteForce(arr, k)
    print("Result:Brute Force", result)
    print("Better Solution")
    result = sol.longest_subarray_optimized(arr, k)
    print("Result:Better", result)
