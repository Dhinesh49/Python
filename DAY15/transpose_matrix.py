class Solution(object):
    def transpose(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        arr = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(matrix[j][i])
            arr.append(temp)
        return arr
