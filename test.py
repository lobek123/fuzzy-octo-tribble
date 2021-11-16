import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('cars2.csv')




def pairplot(data, height, width):

    plot = sns.pairplot(data,
                        height = height,
                        aspect = width)
    return plot

plot = pairplot(data, 5, 5)
plt.show()
