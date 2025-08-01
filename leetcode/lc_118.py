from typing import List


class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        global result
        result = []
        if num_rows == 1:
            return [[1]]
        if num_rows == 2:
            return [[1], [1, 1]]

        result.append([1])
        result.append([1, 1])

        for i in range(2, num_rows):
            new_list = [1]
            for j in range(len(result[i - 1]) - 1):
                row_sum = result[i - 1][j] + result[i - 1][j + 1]
                new_list.append(row_sum)
            new_list.append(1)
            result.append(new_list)

        return result


if __name__ == "__main__":
    sol = Solution()
    n = 5
    result = sol.generate(n)
    print("Result:", result)
