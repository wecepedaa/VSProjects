import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos//muestra_asc.csv")

sns.lineplot(x="fecha", y="valor", data=df)

plt.plot("10-09", 1040,"o")
plt.show()
