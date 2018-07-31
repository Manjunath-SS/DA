import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

labels='Cars','Motorbikes','Vans','Buses'
sizes=[140,70,55,5]
explode=(0,0,0,0.2)

fig1,ax1=plt.subplots()
ax1.pie(sizes,explode=explode,shadow=True, labels=labels, autopct='%.2f%%', startangle=90)
ax1.axis('equal')