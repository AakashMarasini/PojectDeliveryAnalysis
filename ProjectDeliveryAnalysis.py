#!/usr/bin/env python
# coding: utf-8

# In[129]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


# In[72]:


data=pd.read_excel(r'C:\Users\Dell\Desktop\JDA\Aakash_Marasini_Data Analyst Assessment - Project Details.xlsx')


# In[73]:


data.head(5)


# In[74]:


#checking the dimension of the DataFrame
data.shape


# In[75]:


#displaying the data types and null counts of the DataFrame
data.info(verbose=True, null_counts=True)


# In[76]:


# checking the summary for numeric columns
data.describe()


# In[77]:


null_counts = data.isnull().sum()
null_counts


# In[78]:


#Missing percentage on each fields
null_percentage=(null_counts/len(data))*100
null_percentage.sort_values(ascending=False)


# In[79]:


# List of columns containing percentage of null values greater than 60%
null_val = data.isnull().sum().sort_values(ascending=False)
null_val = null_val[null_val.values>(0.6*len(data))]
null_val


# In[80]:


#Dropiing the columns with missing values more than 60%
del_col = (data.isnull().sum()/len(data))
del_col = list(del_col[del_col.values>=0.6].index)
# del_col
data.drop(labels=del_col, axis=1, inplace=True)
# len(del_col)


# In[81]:


# dimension of dataset after deleting the columns containing null values>60%
data.shape


# Imputing missing values on some colummn

# In[82]:


data.Country.value_counts()


# In[83]:


#AS we can see there are United States, USA, US which are same
#Similarly same scenario for United Kingdom
data['Country']=data['Country'].replace(['USA','US'],'United States')
data['Country']=data['Country'].replace(['UNITED KINGDOM'],'United Kingdom')


# In[84]:


data.Country.value_counts()


# In[85]:


data.Country.isna().sum()


# In[86]:


Country_null = pd.isnull(data["Country"]) 
data[Country_null]


# In[87]:


#Dropping the row data for which state is missing
data.dropna(subset = ['Billing State/Province'], inplace = True)  


# In[88]:


Country_null = pd.isnull(data["Country"]) 
data[Country_null]


# In[92]:


#as we can see above states belongs to US, so replace NaN with United States
data['Country'].fillna('United States',inplace=True)


# In[128]:


data.corr()


# In[130]:


dataplot = sb.heatmap(data.corr(), cmap="YlGnBu", annot=True)


# In[125]:


correlation=data['Account MRR'].corr(data['Account MRR'])


# In[126]:


correlation


# In[ ]:




