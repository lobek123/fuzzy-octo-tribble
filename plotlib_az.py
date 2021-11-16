import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

x = [1, 2, 3, 4, 55]
y = [1, 4, 9, 16, 30]

def xy_scatter(x, y, x_lab, y_lab, title):
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel(x_lab)
    plt.ylabel(y_lab)
    plt.legend()
    fig = plt.show()
    return(fig)

figure = xy_scatter(x, y, 'X', 'Y', 'Scatter')

def tipsy():
    tips = sns.load_dataset("tips")
    tips.head()
    sns.relplot(data=tips, x="total_bill", y="tip", hue="sex", col="day", col_wrap=2)
    fig = plt.show()
    return(fig)

figure2 = tipsy()


