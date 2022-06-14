'''
from pandas import DataFrame

data = {
    'name' : ['aryan','priyansh','mridul'],
    'age' : [16,17,18]   
}

#print(data['name'])

x1=DataFrame(data)
print(x1)
'''

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

data = {
    'name' : ['aryan','priyansh','mridul'],
    'age' : [16,17,18]   
}

#RAW DATA TO PROPER DATA FRAME ,TO CSV
df= pd.DataFrame(data)
#print(df)
#print(df.info(),df.shape) #used to know total rows and columns at the db
#print(df.dtypes)
#df.to_csv('raw-data-2-csv.csv',index=False)

#df.to_csv('df-2-csv-indexing.csv')
#df.to_csv('df-2-csv.csv',index=False)

#print(df.head(),df.head(2))
#print(df.tail(),df.tail(2))
#print(df.describe())


#READ/FILTER-READ OPERATIONS ON A DATASET
#read_operation=pd.read_csv('df-2-csv-indexing.csv')
#print(read_operation)
#print(read_operation['name'])


#ALTERING DATA /UPDATE OPERATION ON A DATASET
selection=pd.read_csv('df-2-csv-indexing.csv')
selection['name'][0] = 'altered' #selection.loc['name'][0] = 'altered'
selection.to_csv('altered-data.csv')

#CHECKIN'
#check=pd.read_csv('altered-data.csv')
#print(check)

#PLAYING WITH INDEXING ROWS AND COLUMN
selection.index=['first','second','third']
print(selection)