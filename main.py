import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp
from time import sleep, perf_counter
import sys

class C:
    def __init__(self):
        self.df = pd.DataFrame(dict(A=[1, 2, 3], B=['a', 'b', 'c']))
    
    def print_df(self):
        print(self.df)

    @staticmethod
    def print_array():
        a = np.array([4, 5, 6, 7])
        print(a)

    @staticmethod
    def print_list(c=4):
        l = [1, 2, 3, c]
        print(2 * l)
        print([2 * i for i in l])
        d = 2 * np.array(l)
        print(d.sum())

def main():
    c = C()
    c.print_df()
    c.print_array()
    c.print_list(5)
    print('c.df.iloc[0:2]:')
    print(c.df.iloc[0:2])
    print('c.df.loc[0:2]:')
    print(c.df.loc[0:2])
    plt.plot(c.df['A'])
    plt.show()

def f(x):
    sleep(0.1)
    return 2 * x

def multi(ncpus=2, n=100, how='star'):
    with mp.Pool(ncpus) as p:
        t = perf_counter()
        if how == 'starmap':
            j = ((i,) for i in range(n))
            g = p.starmap(f, j)
        elif how == 'map':
            g = p.map(f, range(n))
        else:
            g = [f(i) for i in range(n)]
        print(perf_counter() - t)
    return g


if __name__ == '__main__':
    try:
        for how in ['starmap', 'map', 'else']:
            multi(ncpus=4, n=12, how=how)
    except KeyboardInterrupt as e:
        sys.exit('Jammer!')
