import scipy.stats as stats
import numpy as np
import statsmodels.stats.multicomp as multi
import pandas as pd
import matplotlib.pyplot as plt


def example_summary_stats():
    # Read your data from file
    file = "data.csv"
    df = pd.read_csv(file, sep=",", header=None, names=['Chrome','Explorer','Firefox'])

    print(df.mean())

    print(df.std())


example_summary_stats()
