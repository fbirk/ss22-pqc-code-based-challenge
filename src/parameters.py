import numpy as np

"""
    A class to represent the parameters of the syndrome decoding challenge.

    ...

    Attributes
    ----------
    length : int
        the length n 
    seed : int
        the random seed used to generate the challenge
    targetWeight : int
        the target weight w
    matrix : int[][]
        the matrix M, which forms the parity check matrix H of form [I | M^T]

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
"""
class Parameters:
    length = int
    seed = int
    targetWeight = int
    matrix = []
    syndrome = int

    def __init__(self, length, seed, targetWeight, matrix, syndrome):
        self.length = length
        self.seed = seed
        self.targetWeight = targetWeight
        self.matrix = self.generateParityCheckMatrix(matrix)
        self.syndrome = syndrome

    def info(self):
        print("Length: " + str(self.length))
        print("Seed: " + str(self.seed))
        print("Weight w: " + str(self.targetWeight))
        print("Syndrome s: " + str(self.syndrome))
        print("Matrix M: \n" + str(self.matrix))

    def generateParityCheckMatrix(self, matrix):
        id = np.identity(int(self.length / 2), int)
        transpose = np.matrix(matrix).T

        resultMatrix = np.concatenate((id, transpose), axis=1)
        return resultMatrix
        