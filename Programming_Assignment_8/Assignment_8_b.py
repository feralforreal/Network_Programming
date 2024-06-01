
import pandas as pd
import plotly_express as px
def main():
    df = pd.read_csv("C:/Users/Srivaishnavi/PycharmProjects/pythonProject/statepop.csv")
    print(df)
    #print("Input file is not correct")
    df=df.sort_values(by=df.columns[1],ascending=False)
    fig = px.bar(df, x=df.columns[0], y=df.columns[1], text_auto='.2s',title="State vs Population Data using plotly (Assignment_8_2-NetProgramming) by Srivaishnavi G")
    fig.show()

if __name__ == "__main__":
    main()