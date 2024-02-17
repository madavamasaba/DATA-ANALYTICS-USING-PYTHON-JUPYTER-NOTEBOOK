# DATA-ANALYTICS-USING-PYTHON-JUPYTER-NOTEBOOK
Data importation, Cleaning and analysis of Iris Dataset utilizing Python3 (Jupiter notebook)-Anaconda.
#Importing the necessary libraries
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Checking working folder
os.getcwd()

#Changing the working directory
os.chdir("C://Users//Dell//OneDrive//Desktop//FOLDERS//Datascience//My Project")

os.getcwd()

#Importing the dataset
DATA=pd.read_csv('Iris.csv')
DATA

#Checking the first 70 observations
DATA.head(70)

#Checking the last 30 observations
DATA.tail(30)

#Understanding the data
DATA.info()

#The data has no null values.
#Other ways or methods of checking for null values
DATA.isnull().sum()


#NUMERICAL SUMMARY FOR THE DATASET
DATA.describe()

DATA.describe().T

DATA.describe()

#CORRELATION of the variables in the dataset
DATA[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']].corr()

#COLUMNS OR VARIABLE NAMES
DATA.columns

DATA['Species']

#Finding mean of the variables by species
DATA.groupby('Species').mean()

#DISTRIBUTION PLOTS FOR THE DATA
sns.distplot(DATA[['SepalLengthCm','SepalWidthCm']])

#Stripplot to show values of SepalLength over IRIS specie
PLOT=sns.stripplot(y='SepalLengthCm',x='Species',data=DATA)
PLOT

