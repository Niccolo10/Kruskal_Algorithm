import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib as mpl


class WeightedGraph:
    def __init__(self):
        self.arch = []
        self.matrix = []
        self.nodes = []

    def GraphGenerator_NonOriented(self, n, p):
        self.nodes = [i + 1 for i in range(0, n)]
        self.matrix = np.zeros((n, n))
        self.arch = []
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if random.random() < p:
                    self.matrix[i, j] = 1
                    self.arch.append([i + 1, j + 1])
                    self.matrix[j, i] = 1
                    self.arch.append([j + 1, i + 1])

    def randomWeight(self):
        a = 0
        archNumber = len(self.arch)
        weights = [None] * archNumber
        for i in range(0, archNumber, 2):  # generazione pesi degli archi
            weights[i] = random.randint(1, 5)
            weights[i + 1] = weights[i]

        dictionary = {}
        for e in self.arch:
            dictionary[e[0], e[1]] = weights[a]
            a = a + 1

        return dictionary

    def makeSet(self, x, S):
        for i in S:
            if x in S[i]:
                return -1

        S[x] = [x]
        return

    def find(self, x, S):
        for i in S:
            if x in S[i]:
                return i
        return -1

    def union(self, x, y, S):
        xroot = self.find(x, S)
        yroot = self.find(y, S)

        if xroot == -1 or yroot == -1:
            return -1
        for i in S[yroot]:
            S[xroot].append(i)
        del S[yroot]
        return


    def Kruskal_algo(self, S, dictionary):
        result = []
        n = 0
        for node in self.nodes:
            self.makeSet(node, S)
        sortedArchs = {k: node for k, node in sorted(dictionary.items(), key=lambda item: item[1])}
        for i in sortedArchs:
            if self.find(i[0], S) != self.find(i[1], S):
                result.append(i)
                self.union(i[0], i[1], S)
                n = n + 1
                if n == len(self.nodes) - 1:
                    break
        return result


if __name__ == '__main__':

    graphw = WeightedGraph()

    probabilities = []
    connectedNumber = []
    i = 0

    while i <= 1:
        probabilities.append(i)
        graphw.GraphGenerator_NonOriented(5, i)
        S = {}
        dictionary = graphw.randomWeight()
        result = graphw.Kruskal_algo(S, dictionary)
        connectedNumber.append(len(S))
        i = i + 0.01

    x = probabilities
    y = connectedNumber
    mpl.rcParams['lines.linewidth'] = 2
    mpl.rcParams['lines.linestyle'] = ':'
    plt.plot(x, y, color='green')
    plt.xlabel('Probabilities')
    plt.ylabel('Number of connected components')
    plt.title('5 Nodi')
    plt.savefig('5nodi.png')
    plt.close()

    probabilities = []
    connectedNumber = []
    i = 0

    while i <= 1:
        probabilities.append(i)
        graphw.GraphGenerator_NonOriented(50, i)
        S = {}
        dictionary = graphw.randomWeight()
        result = graphw.Kruskal_algo(S, dictionary)
        connectedNumber.append(len(S))
        i = i + 0.01

    x = probabilities
    y = connectedNumber
    mpl.rcParams['lines.linewidth'] = 2
    mpl.rcParams['lines.linestyle'] = ':'
    plt.plot(x, y, color='blue')
    plt.xlabel('Probabilities')
    plt.ylabel('Number of connected components')
    plt.title('50 Nodi')
    plt.savefig('50nodi.png')
    plt.close()
    xzoom = []
    yzoom = []
    for j in range(0,15):
        xzoom.append(probabilities[j])
        yzoom.append(connectedNumber[j])

    mpl.rcParams['lines.linewidth'] = 2
    mpl.rcParams['lines.linestyle'] = ':'
    plt.plot(xzoom, yzoom, color='blue')
    plt.xlabel('Probabilities')
    plt.ylabel('Number of connected components')
    plt.title('50 Nodi - zoom')
    plt.savefig('50nodizoom.png')
    plt.close()

    probabilities = []
    connectedNumber = []
    i = 0

    while i <= 1:
        probabilities.append(i)
        graphw.GraphGenerator_NonOriented(500, i)
        S = {}
        dictionary = graphw.randomWeight()
        result = graphw.Kruskal_algo(S, dictionary)
        connectedNumber.append(len(S))
        i = i + 0.01

    x = probabilities
    y = connectedNumber
    mpl.rcParams['lines.linewidth'] = 2
    mpl.rcParams['lines.linestyle'] = ':'
    plt.plot(x, y, color='red')
    plt.xlabel('Probabilities')
    plt.ylabel('Number of connected components')
    plt.title('500 Nodi')
    plt.savefig('500nodi.png')
    plt.close()
    xzoom = []
    yzoom = []
    for j in range(0, 3):
        xzoom.append(probabilities[j])
        yzoom.append(connectedNumber[j])

    mpl.rcParams['lines.linewidth'] = 2
    mpl.rcParams['lines.linestyle'] = ':'
    plt.plot(xzoom, yzoom, color='red')
    plt.xlabel('Probabilities')
    plt.ylabel('Number of connected components')
    plt.title('500 Nodi - zoom')
    plt.savefig('500nodizoom.png')
    plt.close()
