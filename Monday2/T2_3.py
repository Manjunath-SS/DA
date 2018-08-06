import pandas as pd

#a) Retrieve the data from file and print it

df=pd.read_csv("T2_3.csv")
print("\nData from file is as follows:\n",df)

#b) Print the students in the order of their height
print("\nPrinting in the order of heights\n:",df.sort_values('Height'))

#c) Calculate the BMI and print it by adding an extra field BMI to the table
df['BMI']=df['Weight']/pow((df['Height']*0.3048),2) #Converting feet into metres
print("\n",df)

#d) Group them by BMI
print("\nGrouping by BMI:\n",df.groupby('BMI'))

#e) Print the name of student who have 
healthy=df[(df.BMI<=25)&(df.BMI>=20)]
print("\n Healthy weight:\n",healthy['Name'].to_string(index=False))
overweight=df[(df.BMI<=30)&(df.BMI>25)]
print("\n Overweight:\n",overweight['Name'].to_string(index=False))
obese=df[(df.BMI>30)]
print("\n Obese:\n",obese['Name'].to_string(index=False))