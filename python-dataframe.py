import pandas as pd

### Add a row at an index, index starts from 0 in dataframe
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df.loc[index] = [10, 20]
print(df)
