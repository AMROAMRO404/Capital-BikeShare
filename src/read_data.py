# Import libraries
import pandas as pd
input_file = "data/2018-06-capitalbikeshare-tripdata.csv"
output_file = "data/data_modified.csv"
# reading csv file
df = pd.read_csv(input_file, delimiter=',')

df.drop(["Start station number", "End station number",
         "End station", "Bike number", "Member type", "End date"], axis=1, inplace=True)
df.rename(columns={'Duration': 'number_of_bikes'}, inplace=True)
df['Start date'] = pd.to_datetime(df['Start date'], errors='coerce')
df['Start date'] = df['Start date'].dt.strftime(
    '%Y-%m-%d %H:00:00')  # 01:34:15    01:10:5

df = df.groupby(["Start date", "Start station"]).count()
df.to_csv(output_file, index=False)
print(df)
print(f'max value = ' + str(df["number_of_bikes"].max()))
