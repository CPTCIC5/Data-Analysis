import pandas as pd
from matplotlib import pyplot as plt

data =  pd.read_csv('data-vid5.csv')

ages=data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages,dev_salaries,label='All Devs',color='#444444',linestyle='--')
#plt.bar(ages,dev_salaries,label='All Devs',color='#444444')

plt.plot(ages,py_salaries,label='Python')

median = 57287 #median Salary

plt.fill_between(ages,dev_salaries,median,
where=py_salaries >= median,interpolate=True,alpha=0.25)

plt.fill_between(ages,dev_salaries,median,
where=py_salaries < median,interpolate=True,color='red',alpha=0.25)

plt.title('Media Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.legend()
plt.grid()
plt.show()