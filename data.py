import pandas as pd
import matplotlib.pyplot as plt


col_names = ['preg', 'plas', 'pres', 'skin', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv', names = col_names)


plt.clf()
plt.hist(data['age'])
plt.show()
data.describe().to_csv('./results/describe.csv')
