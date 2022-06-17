#Q. Why Histograms?
#Answer : If we same answers.output alot of times so we use histograms as it tells no.of answers at that particular value (somehow same  as .value_counts() in pandas)
#example : age input by 1M ppl ,ages will more likely be from 0 to 100

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

#ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

#plt.hist(ages)
#plt.hist(ages,bins=5,edgecolor = 'black')

data = pd.read_csv('data-vid6.csv')
ids = data['Responder_id']
ages = data['Age']

# median_age = 29
# color = '#fc4f30'

# plt.legend()

plt.hist(ages,edgecolor='black')    

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()