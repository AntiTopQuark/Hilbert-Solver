import numpy

import Generate_Matrix, Gauss, Gauss_Seidel, Jacobi, SOR

if __name__ == '__main__':


    for num in range(6,34,2):
        matrix = Generate_Matrix.Hilbert(num)
        b = Generate_Matrix.b(num)


        ### 选择所需要的取消注释
        print("维数",num)
        # res_of_Gauss = Gauss.Calculator(matrix, b)
        # print("高斯消元法结果：",res_of_Gauss)

        # print("Jacobi结果：",Jacobi.Calculator(matrix, b, 10000000))

        print("Gauss_Seidel结果：",Gauss_Seidel.Calculator(matrix, b, 10000000))
        # x = SOR.Calculator(matrix, b, 10000000,1.5)
        # print(x)
