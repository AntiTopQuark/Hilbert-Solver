import random
import numpy as np
import  Generate_Matrix
class GA:
    def __init__(self, w, count):
        # 染色体长度
        self.length = w
        # 种群中的染色体数量
        self.count = count
        # 随机生成初始种群
        self.population = self.generate_inital(w, count)
        #希尔伯特矩阵
        self.matrix = Generate_Matrix.Hilbert(w)
        #b
        self.b = Generate_Matrix.b(w)

    def generate_inital(self,w, num):
        """
        获得随机基因型
        :param w:维数
        :param num: 生成基因型的数量
        :return: list
        """
        initial = []

        for _ in range(num):
            tmp = []
            for _ in range(w):
                tmp.append(random.randint(0, 200) / 100)
            #tmp = self.vector2code(tmp)
            initial.append(tmp)
        return initial

    def vector2code(self,vector):
        """
        将向量转成二进制编码
        :param vector: np.array
        :return: str based 2
        """
        res = ""
        for i in vector:
            num = i * 100
            code = bin(int(num))[2:]
            length = len(code)
            while length < 9:
                code = "0" + code
                length += 1
            res += code
        return res

    def code2vector(self ,string):
        """
        通过字符串获得向量
        :param string: 二进制编码
        :return: np.array
        """
        vector = []
        tmp = ""
        for i in range(len(string)):
            tmp += string[i]
            if (i + 1) % 9 == 0:
                num = int(tmp, 2) / 100
                tmp = ""
                vector.append(num)
        return np.array(vector)

    def fitness(self,x_gene):
        """
        计算适应度,越小适应度越高
        :param matrix: 希尔伯特矩阵
        :param b: n
        :param x_gene:基因型
        :return:
        """
        x = x_gene # x表现形
        val = 0
        for i in x:
            if(val < abs(i -1)):
                val = abs(i -1)
        return val

    def selection(self, retain_rate, random_select_rate):
        """
        选择
        先对适应度从大到小排序，选出存活的染色体
        再进行随机选择，选出适应度虽然小，但是幸存下来的个体
        """
        # 对适应度从大到小进行排序
        graded = [(self.fitness(chromosome), chromosome) for chromosome in self.population]
        graded = [x[1] for x in sorted(graded)]
        # 选出适应性强的染色体
        retain_length = int(len(graded) * retain_rate)
        parents = graded[:retain_length]
        # 选出适应性不强，但是幸存的染色体
        for chromosome in graded[retain_length:]:
            if random.random() < random_select_rate:
                parents.append(chromosome)
        return parents

    def crossover(self, parents):
        """
        染色体的交叉、繁殖，生成新一代的种群
        """
        # 新出生的孩子，最终会被加入存活下来的父母之中，形成新一代的种群。
        children = []
        # 需要繁殖的孩子的量
        target_count = len(self.population) - len(parents)
        # 开始根据需要的量进行繁殖
        while len(children) < target_count:
            male = random.randint(0, len(parents) - 1)
            female = random.randint(0, len(parents) - 1)
            if male != female:
                # 随机选取交叉点
                cross_pos = random.randint(0, self.length)
                # 生成掩码，方便位操作

                male = parents[male]
                female = parents[female]
                # 孩子将获得父亲在交叉点前的基因和母亲在交叉点后（包括交叉点）的基因
                child =  male[:cross_pos] + female[cross_pos:]
                children.append(child)
        # 经过繁殖后，孩子和父母的数量与原始种群数量相等，在这里可以更新种群。
        self.population = parents + children
    def mutation(self, rate):
        """
        变异
        对种群中的所有个体，随机改变某个个体中的某个基因
        """
        for i in range(len(self.population)):
            if random.random() < rate:
                j = random.randint(0, self.length-1)
                num = random.uniform(-0.1,0.1)
                self.population[i][j] += num


    def result(self):
        """
        获得当前代的最优值，这里取的是函数取最大值时x的值。
        """
        graded = [(self.fitness(chromosome), chromosome) for chromosome in self.population]
        graded = [x[1] for x in sorted(graded)]
        return graded[0],self.fitness(graded[0])

    def evolve(self, retain_rate=0.2, random_select_rate=0.5, mutation_rate=0.01):
        """
        进化
        对当前一代种群依次进行选择、交叉并生成新一代种群，然后对新一代种群进行变异
        """
        parents = self.selection(retain_rate, random_select_rate)
        self.crossover(parents)
        self.mutation(mutation_rate)

if __name__ == '__main__':
    ga = GA(3, 100)

    # 200次进化迭代
    for x in range(900):
        ga.evolve()

    print(ga.result())
