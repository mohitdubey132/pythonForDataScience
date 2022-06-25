import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
data1 = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Advertising.csv")
print(data1.head())
#print (data1.head('Tv'))
data = [12 , 3  , 5,  64 , 32 ,43]
plt.bar(range(len(data)), data)
plt.show()