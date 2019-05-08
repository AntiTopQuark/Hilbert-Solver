import numpy as np


def Hilbert(num):
    """
    生成Hilbert矩阵
    :param num: 阶数
    :return: np.array
    """

    res = np.zeros((num, num), dtype=float)
    for i in range(num):
        for j in range(num):
            res[i][j] = 1 / (i + j + 1)
    return res

def b(num):
    """
    生成b
    :param num:维数
    :return:np.array
    """
    matrix = Hilbert(num)
    res = np.zeros(num)
    for i in range(num):
        for j in matrix[i]:
            res[i] += j
    return res




