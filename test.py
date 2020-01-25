import pandas as pd
import numpy as np


class C:
    def __init__(self):
        self.df = pd.DataFrame(dict(A=[1, 2, 3]))
    
    def print_df(self):
        print(self.df)

    @staticmethod
    def print_array():
        a = np.array([4, 5, 6])
        print(a)

    @staticmethod
    def print_list():
        l = [1, 2, 3, 4]
        print(2 * l)
        print([2 * i for i in l])
        b = 2 * np.array(l)
        print(b.tolist())

def main():
    c = C()
    c.print_df()
    c.print_array()
    c.print_list()

if __name__ == '__main__':
    main()
