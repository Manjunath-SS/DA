import pandas as pd

f=pd.read_csv("boston.csv")
cols=list(f)
print("The first two column names are as follows:\n",cols[0]," and ",cols[1])

print("\n\nDatatypes:\n",f.dtypes)
print("Enter a column number to display maximum and minimum: Range of column is:",1,"-",len(cols))
s=int(input())
s+=1
print("Max:",f[cols[s]].max())
print("Min:",f[cols[s]].min())