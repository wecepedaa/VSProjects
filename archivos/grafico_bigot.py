import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos//ingresos.csv")

sns.boxplot(x="fuente", y="ingresos", data=df)

total_ingresos=df["ingresos"].sum()

plt.plot("trabajo", total_ingresos,"*")
plt.show()