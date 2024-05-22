import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# Add a row at index 1 with values 10 and 20 in columns A and B respectively
df.loc[1] = [10, 20]
print(df)
