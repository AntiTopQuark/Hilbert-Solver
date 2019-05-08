import numpy as np
def Calculator(matrix, b):
    """
    高斯消元法，求方程组的解
    :param matrix: 方阵  np.array([[],[]],dtype=float)
    :param b: b np.array([],dtype=float)
    :return: []
    """

    i = 0
    row = matrix.shape[0]

    # 化成三角矩阵
    while i < row:
        for j in range(i + 1, row):
            b[j] = b[j] - b[i] * (matrix[j][i] / matrix[i][i])
            matrix[j] = matrix[j] - matrix[i] * (matrix[j][i] / matrix[i][i])
        i += 1

    i = row - 1
    while i > 0:
        for j in range(i - 1, -1, -1):
            b[j] = b[j] - b[i] * (matrix[j][i] / matrix[i][i])
            matrix[j] = matrix[j] - matrix[i] * (matrix[j][i] / matrix[i][i])
        i -= 1

    res = []
    for i in range(matrix.shape[0]):
        res.append(b[i] / matrix[i][i])

    return np.array(res)


if __name__ == '__main__':
    res = Calculator(1,1)
    print(res)
