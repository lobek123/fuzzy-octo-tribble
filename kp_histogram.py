import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
age = pd.read_excel('https://github.com/datagy/Intro-to-Python/raw/master/sportsdata.xls', usecols=['Age'])

"""print(age)

plt.hist(age.Age, bins=range(0,50,10), align='right', color='green', edgecolor='black')
plt.xlabel('Wiek gracza')
plt.ylabel('Ilość graczy')
plt.title('Wykres zależności ilości graczy w zależności od ich wieku')

plt.show()"""

def histogram(dane,col):
    fig = plt.hist(dane[col], bins=range(0,50,10), align='right', color='green', edgecolor='black')
    plt.xlabel('Wiek gracza')
    plt.ylabel('Ilość graczy')
    plt.title('Wykres zależności ilości graczy w zależności od ich wieku')
    return(fig)

histogram(age,'Age')
plt.show()
