from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

'''
#raw data
plt.style.use('fivethirtyeight')

ages_x=[25,26,27,28,29,30,31,32,33,34,35]
x_indexes=np.array(len(ages_x))
width=0.25

dev_y = [38496, 42000, 46752, 49320, 53200,56000, 62316, 64928, 67317, 68748, 73752]

#plt.bar(ages_x,dev_y,label ='All devs',color='b')
plt.bar(x_indexes-width,dev_y,width=width,label ='All devs',color='#444444')


#print(plt.style.available)

py_dev_y = [45372, 48876, 53850, 57287, 63016,65998, 70003, 70000, 71496, 75370, 83640]
#plt.bar(ages_x,py_dev_y,label ='Python',color='b')
plt.bar(x_indexes,py_dev_y,label ='Python',color='b')


js_dev_y = [37810, 43515, 46823, 49293, 53437,56373, 62375, 66674, 68745, 68746, 74583]
#plt.bar(ages_x,js_dev_y,label='JavaScript',color='y')
plt.bar(x_indexes+width,js_dev_y,width=width,label='JavaScript',color='y')

plt.xlabel('Age') #defines what x-axis describes
plt.ylabel('Median Salary (USD)') #defines what y-axis describes
plt.title('Median Salary (USD) by Age') #to provide title to the graph


plt.legend()
plt.tight_layout()
plt.grid()
plt.show() #to show the graph plotted

'''

#stackoverflow data
plt.style.use("fivethirtyeight")
read=pd.read_csv(r'C:\Users\91834\PycharmProjects\Data Science\pandas_corey_schafer\survey_results_public.csv')
x_id= read['ResponseId'].head()
y_LanguageHaveWorkedWith= read['LanguageHaveWorkedWith'].head()

plt.barh(x_id,str(y_LanguageHaveWorkedWith))

plt.title("Most Popular Languages")
plt.xlabel("Number of People Who Use")
plt.ylabel("Programming Languages")

plt.tight_layout()

plt.show()