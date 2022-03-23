#LEARNING THE BASICS OF PANDAS LIBRARY
import pandas as pd
import numpy as np
#checking the version of pandas
print('Pandas version:',pd.__version__)
print("\n") #separate each output with new line

#Working with Series create, multiple, querry and delete
#creating a Series from a list
arr = [0,1,2,3,4,5]
s1 = pd.Series(arr)
print("A Series with Default Index")
print(s1) #the series is printed with zero as the first index
print("\n")

#change the index of the series
order = [1,2,3,4,5,6]
s2 = pd.Series(arr,index = order)
print("A Series with Ordered Index")
print(s2)
print("\n")

#Import some random array using numpy to use with pandas
n = np.random.rand(5) # create a random Ndarray
index = ['a','b','c','d','e']
s3 = pd.Series(n,index=index)
print("Series with non integer index")
print(s3)
print("\n")

#Creating a Series from dictionary
d = {'a':1,'b':2,'c':3,'d':4} #dictionary
s4 = pd.Series(d)
print(s4)
print("\n")

#modifying the index of a Series
s4.index = ['A','B','C','D']
print(s4)

#slicing
print(s2[:-4])

#appending series
s5 = pd.concat([s3,s4]) #we use pandas.concat instead of append
                        #since it is depreciating and won't be used in future
print(s5)

#SERIES OPERATIONS
arr1 = [0,1,2,3,4,5,7]
arr2 = [6,7,8,9,5]

s6 = pd.Series(arr1)
s7 = pd.Series(arr2)

#adding two series
print(s6.add(s7)) #adds with no error as opposed to numpy when length is not same
#Subtracting two serires
print(s7.sub(s6))
#multiplying
print(s6.mul(s7))
#dividing
print(s7.div(s6))
#median,max,min data
print('median:',s7.median())
print('max:',s7.max())
print('min:',s7.min())

#CREATING A DATAFRAME
#define time sequence as the index
dates = pd.date_range('today',periods = 6)
num_arr = np.random.randn(6,4) #import numpy random array
columns = ['A','B','C','D']    #use the table as column name
df1 = pd.DataFrame(num_arr,index=dates,columns=columns)
print(df1)
print('\n')

#creating dataframe with dictionary array
data = {'Animal':['cat','cat','snake','dog','dog','cat','snake','cat','dog','dog'],
        'Age':[2.5,3,0.5,np.nan,5,2,4.5,np.nan,7,3],
        'Visits':[1,3,2,3,2,3,1,1,2,1],
        'Priority':['yes','yes','no','yes','no','no','no','yes','no','no']}
labels = ['a','b','c','d','e','f','g','h','i','j']
df2 = pd.DataFrame(data,index=labels)
print(df2)

#check the data types of array
print(df2.dtypes)

#display a given section of the dataframe
print(df2.head(2))
print(df2.tail(3))
print(df2.index)
print(df2.columns)
print(df2.values)
print(df2.describe())

#manipulating the dataframes
print(df2.T)
print(df2.sort_values(by='Age')) #sorting
print(df2.sort_values(by='Age')[1:3]) #sorting and slicing

#query the dataframe by tag
print(df2[['Age','Visits']])
#copying dataframe
df3 = df2.copy()
print(df3)
print(df3.isnull())
print(df3.mean())