#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importing the necessary libraries
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[9]:


#Checking working folder
os.getcwd()


# In[10]:


#Changing the working directory
os.chdir("C://Users//Dell//OneDrive//Desktop//FOLDERS//Datascience//My Project")


# In[11]:


os.getcwd()


# In[12]:


#Importing the dataset
DATA=pd.read_csv('Iris.csv')
DATA


# In[13]:


#Checking the first 70 observations
DATA.head(70)


# In[15]:


#Checking the last 30 observations
DATA.tail(30)


# In[16]:


#Understanding the data
DATA.info()


# In[18]:


#The data has no null values.
#Other ways or methods of checking for null values
DATA.isnull().sum()


# In[19]:


#NUMERICAL SUMMARY FOR THE DATASET
DATA.describe()


# In[21]:


DATA.describe().T


# In[22]:


DATA.describe()


# In[29]:


#CORRELATION of the variables in the dataset
DATA[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']].corr()


# In[31]:


#COLUMNS OR VARIABLE NAMES
DATA.columns


# In[33]:


DATA['Species']


# In[35]:


#Finding mean of the variables by species
DATA.groupby('Species').mean()


# In[38]:


#DISTRIBUTION PLOTS FOR THE DATA
sns.distplot(DATA[['SepalLengthCm','SepalWidthCm']])


# In[42]:


#Stripplot to show values of SepalLength over IRIS specie
PLOT=sns.stripplot(y='SepalLengthCm',x='Species',data=DATA)
PLOT


# In[ ]:




