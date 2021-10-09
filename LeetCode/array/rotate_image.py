class Solution(object):
    def rotate(self, matrix: list[list[int]]):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                print(f"i:{i}, j:{j}")
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                print(f"{matrix[0]}")
                print(f"{matrix[1]}")
                print(f"{matrix[2]}")

        for i in range(n):
            matrix[i] = matrix[i][::-1]

        print(matrix)


Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
