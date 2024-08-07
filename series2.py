import pandas as pd

data = pd.Series([10, 20, 30, 40, 50], index = ["A", "B", "C", "D", "E"])
print(data, '/n', data['B'])
