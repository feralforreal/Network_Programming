import matplotlib.pyplot as plt
#import plotly_express as px
import pandas as pd

df = pd.read_csv("C:/Users/Srivaishnavi/PycharmProjects/pythonProject/cartheft.csv")
df = df.sort_values(df.columns[2], ascending=False)
df= df.head(10)
print(df)
df.plot(x=1, y=2, kind='bar', color = "g", label = "Count of Thefts per model")
plt.ylabel("Number of Thefts in the year 2012", color = "b")
plt.xlabel("Car Models", color="b")
plt.title ("Count of Top 10 Car Thefts in the year 2012 by Car Model", color = "r")
plt.show()
