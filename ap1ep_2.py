import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

labels='Beast Animals','Other Land Animals','Birds','Water Animals','Reptiles'
sizes=[150,400,225,175,50]
explode=(0,0,0,0,0.2)

fig1,ax1=plt.subplots()
ax1.pie(sizes,explode=explode,shadow=True, labels=labels, autopct='%.2f%%', startangle=270)
ax1.axis('equal')
