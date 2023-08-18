# -*- coding: utf-8 -*-
"""hackthonFinal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R5shadc79ASiiCRclnF750QGEhnMmrVh

Prediction for number of reverse vending machines
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import seaborn as sns
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

total_waste=pd.read_csv("final dataset 1.csv")
total_waste

df1=pd.DataFrame(total_waste)

#state wise average for machines quantity prediction
df1['Mean'] = df1.mean(axis=1)
df1

plt.style.use('fivethirtyeight')
plt.figure(figsize=(19,16))
plt.title("Plastic Bottle Waste Generation per Satate in Past decade\n")
plt.bar(x=df1['state'],
 
        height=df1['Mean'])

plt.xticks(rotation=90)
plt.rcdefaults()
plt.legend()

x = ['2011','2012','2013','2014','2015','2016','2017','2019']
y = df1['2019']

plt.style.use('fivethirtyeight')

plt.figure(figsize=(29,26))
y=mean_year
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
Years = ['2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020']
plt.title("Increase in Plastic Waste in Past decade\n")
ax.bar(Years,y,width=0.5)
plt.xlabel("Year")
plt.ylabel("Tonnes")

plt.xticks(rotation=90)

#here 1.91625 tonnes is the calculation for each machine capacity for the year
df1['Number of reverse vending machines']=df1["Mean"]//1.91625
df1

from numpy.lib.arraysetops import setdiff1d
m1=df1['2011'].mean()
m2=df1['2012'].mean()
m3=df1['2013'].mean()
m4=df1['2014'].mean()
m5=df1['2015'].mean()
m6=df1['2016'].mean()
m7=df1['2017'].mean()
m8=df1['2018'].mean()
m9=df1['2019'].mean()
sum_m=df1['Number of reverse vending machines'].sum()
mean_year=[m1,m2,m3,m4,m5,m6,m7,m8,m9]
mean_year
sum_m



x= df1.iloc[:,2:11]  
y= df1.iloc[:,-2]

plt.style.use('fivethirtyeight')
plt.figure(figsize=(19,16))
plt.title("Machines Required Per State Initially\n")
plt.bar(x=df1['state'],
 
        height=df1['Number of reverse vending machines'])

plt.xticks(rotation=90)
plt.rcdefaults()
plt.legend()

df2=pd.read_csv("rate.csv")
df2

"""Plastic Waste Generation is Increasing by 2% to 7% For first decade.
Machine Numbers Increasing by 1%-2% per Year and Machine Recycling Capacity Increasing by 3%-4% per Year respectively.
"""

plt.style.use('fivethirtyeight')

x = df2['Year']
y = df2['PlasticProductionWaste']
plt.plot(x,df2['MachineCapacity'],label="machine capacity",color='blue')
plt.plot(x, y,label="Plastic Waste",color='red')
plt.title("  Plastic Bottle Waste Generation vs Our Machine Capacity First 10 yrs results\n")

plt.rcdefaults()
plt.legend()

plt.xlabel("Years")
plt.ylabel("million Tonnes")
plt.savefig("plot.png")
plt.show()

plt.style.use('fivethirtyeight')

plt.title("  Plastic Bottle Waste Generation vs Our Machine Capacity First 10 yrs results\n")
plt.scatter(df2['Year'],df2['MachineCapacity'],label='Machine Production')
plt.scatter(df2['Year'],df2['PlasticProductionWaste'],label='Plastic Waste')
plt.xlabel("Year")
plt.ylabel("million Tonnes")
plt.rcdefaults()
plt.legend()

x = df2['Year']
y = df2['Recycle']
  
plt.style.use('fivethirtyeight')


plt.plot(x, y,color='red')
plt.title("Our machine Recycle rate first 10 Years\n")
plt.xlabel("Years")
plt.ylabel("Recycle")

plt.rcdefaults()
plt.legend()
plt.xticks(rotation=45)
plt.show()

"""Recycling Rate is negative initally since machine capacity is less then total Plastic Bottle waste generation.
Recycling Rate will increase down the decades.
"""

df3=pd.read_csv("rate1.csv")
df3

x = df3['Year']
y = df3['PlasticProductionWaste']
  
plt.style.use('fivethirtyeight')


plt.plot(x, y,label="Plastic Waste",color='red')
plt.title("  Plastic Bottle Waste Generation vs Our Machine Capacity 20 yrs results\n")
plt.plot(x,df3['MachineCapacity'],label="machine capacity",color='blue')
plt.xlabel("Years")
plt.ylabel("million Tonnes")

plt.rcdefaults()
plt.legend()
plt.xticks(rotation=45)
plt.show()

"""Here Machine Recycling Capacity has Surpassed Plastic Bottle Waste Generation."""

plt.style.use('fivethirtyeight')


plt.scatter(df3['Year'],df3['MachineCapacity'],label='Machine Production')
plt.title("  Plastic Bottle Waste Generation vs Our Machine Capacity 20 yrs results\n")
plt.scatter(df3['Year'],df3['PlasticProductionWaste'],label='Plastic Waste')
plt.xlabel("Year")
plt.ylabel("million Tonnes")

plt.rcdefaults()
plt.xticks(rotation=45)
plt.legend()

x = df3['Year']
y = df3['Recycle']
  
plt.style.use('fivethirtyeight')


plt.plot(x, y,color='red')
plt.title("Our machine Recycle rate after 20 Years\n")
plt.xlabel("Years")
plt.ylabel("Recycle")

plt.rcdefaults()
plt.legend()
plt.xticks(rotation=45)
plt.show()

df4=pd.read_csv("pollution.csv")
df4

x = df4['Year']
y = df4['TotalPlasticPollution']
  
plt.style.use('fivethirtyeight')


plt.plot(x, y,label="TotalPlasticPollution",color='red')
plt.title("  Impact of our Machines on Total Plastic Pollution in India\n")
plt.plot(x,df4['Recycled'],label="Recycled",color='blue')
plt.xlabel("Years")
plt.ylabel("million Tonnes")

plt.rcdefaults()
plt.legend()
plt.xticks(rotation=45)
plt.show()

"""As the recycling rate increases the total plastic pollution also decreases gradually."""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import seaborn as sn

X = df4[['xx', 'yy']]
y = df4['Recycled']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)
logistic_regression= LogisticRegression()
logistic_regression.fit(X_train,y_train)
y_pred=logistic_regression.predict(X_test)
print (X_test)

print (y_pred)

confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
sn.heatmap(confusion_matrix, annot=True)

import statsmodels.api as sm
x=sm.add_constant(X)
model=sm.OLS(y,X)
fitted_model=model.fit()
print(fitted_model.summary())