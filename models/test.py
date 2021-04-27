import pandas as pd
input_file = "data/data_modified.csv"

df = pd.read_csv(input_file, delimiter=',')
print(df)
