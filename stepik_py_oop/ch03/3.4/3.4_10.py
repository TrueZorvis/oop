class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix):
        for row in matrix:
            if len(row) != len(matrix[0]):
                raise ValueError("Неверный формат для первого параметра matrix.")

            if not all([type(x) in (int, float) for x in row]):
                raise ValueError("Неверный формат для первого параметра matrix.")

        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0

        if rows == 0:
            return [[]]

        h, w = self.size
        sh, sw = self.step

        rows_range = (rows - h) // sh + 1
        cols_range = (cols - w) // sw + 1

        res = [[0] * cols_range for _ in range(rows_range)]

        for i in range(rows_range):
            for j in range(cols_range):
                res[i][j] = max([item for row in matrix[i * sh: i * sh + h] for item in row[j * sw: j * sw + w]])

        return res


mp = MaxPooling(step=(2, 2), size=(2, 2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 4]])    # [[6, 8], [9, 7]]
print(res)
print('end')
