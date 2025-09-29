import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:\Software engg Professional training\Python Basics\Python Pandas\pandas plot\data1.csv')

df['Duration'].plot(kind = 'hist')

plt.show()
