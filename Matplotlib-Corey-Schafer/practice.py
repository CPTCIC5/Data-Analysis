from matplotlib import pyplot as plt
import pandas as pd

'''
plt.xkcd()

read= pd.read_csv('data-vid5.csv')

overall_age = read['Age']
all_devs= read['All_Devs']

plt.plot(overall_age,all_devs,label='All Devs',
color='#444444',marker='o',linestyle='--'
)
py_devs= read['Python']
plt.plot(overall_age,all_devs,label='Python',
color='red',marker='X',linestyle='--'
)

js_devs= read['JavaScript']
plt.plot(overall_age,js_devs,label='JavaScript',color='blue')

#plt.bar(overall_age,all_devs,label='All Devs')

plt.legend()
plt.grid()

#plt.savefig('practice-plot.png')
plt.savefig('practice-plot-xkcd.png')
plt.show()
'''

#-------------------------------------------------------------------------
'''
read= pd.read_csv('data-vid5.csv')
overall_age = read['Age']

all_devs= read['All_Devs']
plt.bar(overall_age,all_devs,label='All Devs',color='#444444')

py_devs= read['Python']
plt.bar(overall_age,py_devs,label='Python',color='blue')

js_devs= read['JavaScript']
plt.bar(overall_age,js_devs,label='JavaScript')

plt.legend()
plt.savefig('practice-bar.png')
plt.show()
'''
#-------------------------------------------------------------------------

read = pd.read_csv('data-vid5.csv')
py_devs= read['Python']
js_devs= read['JavaScript']

plt.pie(py_devs)

plt.show()
#-------------------------------------------------------------------------
'''
read=pd.read_csv('data-vid6.csv')
overall_age = read['Age']
plt.hist(overall_age)

plt.savefig('practice-histogram.png')
plt.show()
'''
#------------------------------------------------------------------------