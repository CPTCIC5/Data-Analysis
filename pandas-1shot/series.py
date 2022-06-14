import pandas as pd
import numpy as np

ser = pd.Series(np.random.rand(34))
#print(ser)

df=pd.DataFrame(np.random.rand(20,3),index=np.arange(1,21),columns=np.arange(1,4)) #random.rand(rows-u-want,column-u-want) is used to make dummy data,arange works same as range function
#print(df)
#print(df.head(5),df.tail(3))  
#print(df.describe()) #prints some maths function of all int val
#df[1][0] =  'change'
#print(df.dtypes) #prints the datatype
#print(df.T)  #converts rows into columns n columns into rows

#SORTING
#note- axis 0 for sorting rows , axis 1 for sorting columns
#x1=df.sort_index(axis=0 ,ascending=False)
#x1=df.sort_index(axis=0 ,ascending=True)
#print(x1)
#x1=df.sort_values(by=0)
#print(x1)

#EDIT-OPERATION/CHANGING DATA
#loc-in this we enter the data in form of its name on the dataframe[row-name,column-name]
#iloc-in this we enter the data in form of python indexing[row-index,column-index]

#df[1][1] = "testing"
#OR
#df.loc[1,1] = 'testing'  #df.loc[0,0]
#print(df)

df.columns=list("ABC")    #['A','B','C']
#df.loc[1]['A'] = 6969    #df.iloc[0][0] = 6969
print(df.head())
#print(df,df.columns)


#newdf= df.copy() #bad method/practice
#print(newdf)

#DROPPING ROWS OR COLUMNS
df = df.drop('C',axis=1) #axis=1 for dropping column
print(df.head(1))
df= df.drop(1,axis=0)
print(df.head(3))