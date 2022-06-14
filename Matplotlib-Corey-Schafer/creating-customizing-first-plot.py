from matplotlib import pyplot as plt

plt.xkcd()

ages_x=[25,26,27,28,29,30,31,32,33,34,35]
dev_y = [38496, 42000, 46752, 49320, 53200,56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(ages_x,dev_y, label ='All Devs',color='k',linestyle='--',marker='.') #to plot the graph
#plt.bar(ages_x,dev_y,label ='All devs',color='b')
#print(plt.style.available)
py_dev_y = [45372, 48876, 53850, 57287, 63016,65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x,py_dev_y,label ='Python',color='b',marker='o')
#plt.bar(ages_x,py_dev_y,label ='Python',color='b')

js_dev_y = [37810, 43515, 46823, 49293, 53437,56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages_x,js_dev_y,label='JavaScript',color='y',marker='X')
#plt.bar(ages_x,js_dev_y,label='JavaScript',color='y')

plt.xlabel('Age') #defines what x-axis describes
plt.ylabel('Median Salary (USD)') #defines what y-axis describes
plt.title('Median Salary (USD) by Age') #to provide title to the graph

#plt.legend(['All Devs','Python']) #to define label for all plots in graph
#OR
plt.legend()

plt.grid()
#plt.savefig('first.png')
plt.savefig('firstfinal-xkcd.png')
#plt.savefig('bar-firstfinal-xkcd.png')
plt.show() #to show the graph plotted