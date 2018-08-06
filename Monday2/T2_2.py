import pandas as pd

df=pd.read_csv('camera.csv')

#a) Print the properties of the data set
print("\nProperties of dataset:\n")
print(df.info())

#b) Print the data types of properties
print("\n\n\nDatatypes of properties:\n",df.dtypes)

#c) Print the model, release date and price of first 25 entries
print("\n\nPrinting the model, release date and price of first 25 entries\n\n",df[['Model', 'Release date','Price']].head(25))

#d) Summarise the data set
print("\n\nSummarizing data set:\n",df.describe(include='all'))

#e) Print the summary statistics for price
print("\n\n Summary statistics for price:")
print(df['Price'].describe())

#f) Plot a time series graph of release date and price > 1000
#print("\n\n\n\n",df['Price'].astype(float))