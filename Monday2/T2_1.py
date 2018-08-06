import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('100 Sales Records.csv')

#a) Print the name of columns
print("\n The names of the columns are:",)
for i in list(df):
    print(i)

#b) Print 10 rows and 10 columns in the data set
print("\n The first 10 columns and rows are as follows:\n",df.iloc[0:10,0:10])

#c) Plot any graph to represent the total profit
plt.bar(df['Region'],df['Total Profit'])
plt.xticks(rotation=80)
plt.tight_layout()
plt.title("Regionwise Total Profit")
plt.show()

#d) Print the item type with total cost greater than 1000000
print("\n The following are the item names and their corresponding row number whose total cost is greater than 1000000")
for index, row in df.iterrows():
    if row['Total Cost']>1000000:
        print(index, row['Item Type'])