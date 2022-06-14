import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.rand(3,2),index=np.arange(1,4),columns=np.arange(1,3))
#print(df.count())
df.columns = ['A','B'] # list('ABC')
#print(df)
df.to_csv('quiz.csv',index=False)

read=pd.read_csv('quiz.csv')
#print(read.info())
#print(read.describe())
read.loc[1,'A'] = 696969   #read.iloc[0,0] = 696969

#print(read)
#print(read.T)
#print(df.dtypes)
#print(read.head())

#read= read.drop('A',axis=1)
#print(read)