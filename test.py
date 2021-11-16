import matplotlib.pyplot as plt
import seaborn as sb

x=[2,4,5,6,7]
y=[3,4,6,8,9]

def liniowy(x,y):
    plt.plot(x,y)
    plt.title('Wykres liniowy')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    fig = plt.show()
    return(fig)

figure = liniowy (x, y)

import seaborn as sns
from matplotlib import pyplot as plt

def seaborn_dd(x='iris',set_style="ticks"):
    df = sns.load_dataset(x)
    sns.set_style(set_style)
    sns.pairplot(df,hue = 'species',diag_kind = "kde",kind = "scatter",palette = "husl")
    fig = plt.show()
    return(fig)

figure1=seaborn_dd()

def seaborn2_dd(x='tips'):
    tips = sns.load_dataset(x)
    g = sns.FacetGrid(tips, col="time")
    g.map(sns.scatterplot, "total_bill", "tip")
    fig = plt.show()
    return(fig)

figure2=seaborn2_dd()


