import pandas as pd
import numpy as np


class C:
    def __init__(self):
        self.df = pd.DataFrame(dict(A=[1, 2, 3]))
    
    def print_df(self):
        print(self.df)

    def print_array(self):
        a = np.array([4, 5, 6])
        print(a)

def main():
    c = C()
    c.print_df()
    c.print_array()

if __name__ == '__main__':
    main()
