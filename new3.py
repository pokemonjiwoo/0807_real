import pandas as pd
import numpy as np

my_index = np.array([1, 2, 3])
data = ['홍길동', '이관훈', '김우진']
data_2 =[10, 20, 30, 40, 50]

series_2 = pd.Series(data, index = my_index)
print(series_2)