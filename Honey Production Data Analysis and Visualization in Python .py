#!/usr/bin/env python
# coding: utf-8

# In[53]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[54]:


df = pd.read_csv("honeyproduction 1998-2021.csv")
df.head()


# In[55]:


df.count()


# In[56]:


df.describe()


# In[57]:


df.isnull().sum()


# In[58]:


df.duplicated().sum()


# In[59]:


df.dtypes


# How has honey production yield changed from 
# 1998 to 2021 ?

# In[60]:


plt.figure(figsize=(12, 6))
plt.plot(df['year'],df['yieldpercol'],marker = 'o')
plt.title("How has honey production yield changed from 1998 to 2021 ?")
plt.xlabel('year' ,color = 'g' ,size = 20)
plt.ylabel('year per count' ,color = 'g' ,size = 20)
plt.grid(color = 'black')
plt.show()


# Over time , what are the major production 
# trends across the states?

# In[61]:


states = df.groupby('State')
plt.figure(figsize = (15,6))

labels = ['Number of Colonies', 'Yield per Colony', 'Total Production', 'Stocks', 'Price per Pound', 'Production Value']
for state in states:
    plt.plot(df['year'],df['numcol']  ,marker = 'o')
    plt.plot(df['year'],df['yieldpercol'] ,marker = 'o')
    plt.plot(df['year'],df['totalprod'] ,marker = 'o')
    plt.plot(df['year'],df['stocks'],marker = 'o')
    plt.plot(df['year'],df['priceperlb'],marker = 'o')
    plt.plot(df['year'],df['prodvalue'] , marker = 'o')
plt.title("Honey production trend acrross the states (1998 -2021)",color = 'g', size = 20)
plt.xlabel('year',color = 'c',size = 20)
plt.ylabel('total producation' ,color = 'c',size = 20)
plt.grid(color = 'black')
plt.legend(labels ,loc = 'upper left')
plt.show()


# Does the data show any trends in terms of the number of honey -
# producing colonies and yield per colony before 2006 , which was when 
# concern over Colony Collapse Disorder spread nation wide 

# In[73]:


date_before_2006 = df[df['year']<2006]

plt.figure(figsize = (15,6))
plt.subplot(1,2,1)
plt.plot(date_before_2006['year'],date_before_2006['numcol'],marker ='o')
plt.title('number_of_honey_production_colonies (before 2006)' ,size =20)
plt.xlabel('year',color = 'g',size = 20)
plt.ylabel('numberof colonies',color = 'c' ,size = 20)
plt.grid(color = 'black')
plt.show()

plt.figure(figsize = (15,6))
plt.subplot(1,2,1)
plt.plot(date_before_2006['year'],date_before_2006['yieldpercol'],marker='o')
plt.title('number of yield per count',size = 20)
plt.xlabel('year',color = 'c',size = 20)
plt.ylabel('yield per count',color ='c',size =20)
plt.grid(color = 'black')
plt.show()


# Are there any patterns that can be observed between 
# total honey production and the value of production every 
# year ?
# 

# In[76]:


plt.figure(figsize = (15,6))
plt.scatter(df['totalprod'],df['prodvalue'],marker = 'o')
plt.title('total honey production vs value of production',color = 'g',size = 15)
plt.xlabel('total honey production ',color = 'c',size =20)
plt.ylabel('value of production',color = 'c',size = 20)
plt.grid(color = 'black')
plt.show()


# How has the value of production , which in some 
# sense could be tied to demand , changed every year 

# In[77]:


plt.figure(figsize = (15,6))
plt.plot(df['year'],df['prodvalue'],marker = 'o')
plt.title('value of production')
plt.xlabel('year')
plt.ylabel('value of production')
plt.grid(color = 'black')
plt.show()


# In[ ]:




