import pandas as pd

df = pd.read_csv("archivos//2018_Central_Park_Squirrel_Census.csv")


df1 = df.groupby(['Primary Fur Color'])['Primary Fur Color'].count()
df1.to_csv('archivos//cuenta_ardillas.csv')

print(df1)