from this import d
import numpy as np
from parameters import Parameters


class McEliece:

    def __init__(self, params):
        self.params = params

    def key_generation(self):
        n = 7
        k = 4
        d = 3

        g = self.get_generator_matrix(d, k)
        s = self.get_scramble_matrix(k, k)
        p = self.get_permutation_matrix(n, n)

        big_g = self.generate_big_g(g, s, p)
        t = self.get_max_errors_from_distance(d)

        return big_g, t

    def encryption(big_g, z, m):
        # c = mG + z

        cipher = np.matmul(m, big_g)
        return cipher + z

    def decryption(cipher, p, s, g):
        # c' = c * P^-1 --> undo permutation
        cipher_prime = np.matmul(cipher, p.I)

        # decode hamming-code
        # calculate hamming-code for each line of g
        d       # todo
        m_prime # todo

        # m = m' * S^-1 --> get clear message
        m = np.matmul(m_prime, s.I)
        return m


    def generate_random_matrix(i, j):
        return np.random.randint(2, size=(int(i), int(j)))

    def get_max_errors_from_distance(self, d):
        # when hamming distance d = 2*t + 1
        # then the number of errors t = (d - 1) / 2
        return int((int(d) - 1) / 2)

    def get_generator_matrix(self, d, k):
        mat = self.generate_random_matrix(k, d)
        id = np.identity(int(d), int(d))

        return np.concatenate((id, mat), axis=1)

    def get_scramble_matrix(self, k):
        return self.generate_random_matrix(k, k)

    def get_permutation_matrix(self, n):
        return self.generate_random_matrix(n, n)

    def generate_big_g(self, g, s, p):
        return np.matmul(np.matmul(g, s), p)
