import numpy as np


def Calculator(matrix, b, num):
    """
    高斯塞德尔迭代
    :param matrix: 系数矩阵 np.array([[],[]],dtype=float)
    :param b:  bnp.array([],dtype=float)
    :param num: 迭代次数
    :return: 结果 【】
    """

    res = np.zeros(matrix.shape[1], dtype=float)

    for index in range(num):
        line = res.copy()
        for i in range(res.size):
            tmp = b[i]
            for j in range(res.size):
                if i == j:
                    continue
                else:
                    tmp = tmp - matrix[i][j] * res[j]
            res[i] = tmp / matrix[i][i]

        Flag = True
        for i in range(len(res)):
            if abs(res[i]  -1) >= 1e-5:
                Flag = False
        if Flag:
            print("误差小于1e-2所需要的迭代次数为：", index + 1)
            for i in res:
                print(i, end=" ")
            print()
            return res

    print("误差未小于1e-5")
    return res



