import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def pairplot(data, height, width):

    plot = sns.pairplot(data,
                        height = height,
                        aspect = width)
    return plot
