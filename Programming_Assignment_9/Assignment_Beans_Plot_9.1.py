import pandas as pd
import plotly.express as px
Col_Names = ["Price", "Date", "Time"]
df =pd.read_csv("C:/Users/Srivaishnavi/PycharmProjects/pythonProject/Beans_Lab9_Assignment_9.csv", names=Col_Names)
df=df.sort_values(by=['Price'], ascending=True)
fig = px.line(df, x='Time', y='Price', title = 'Price vs Time for the beans')
fig.show()


