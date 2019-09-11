import numpy as np
import pandas as pd


def get_data(filename='data.txt', n=10, x=9, y=9):
    df = pd.DataFrame(np.random.randint(n, size=(y, x)))
    df.to_csv(filename, index=False, sep='\t')
    print('successfully created test data:', filename)


get_data()