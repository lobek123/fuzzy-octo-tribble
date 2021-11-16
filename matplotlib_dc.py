import matplotlib.pyplot as plt
import numpy as np

x = np.arange(100)
y = np.random.randn(100)

tytul = 'Zaleznosc x od y'

def scatter_plot(x = np.arange(1000),y = np.random.randn(1000), z = np.random.randn(1000), tytul = 'Zaleznosc x od y'):

    plt.scatter(x,y,c = z, cmap = 'inferno')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(tytul)
    return plt.show()

scatter_plot()