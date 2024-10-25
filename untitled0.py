# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C6L1dc5Gd-RizpHJGJkdvO8lXR5AspMQ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

data=pd.read_csv('/content/train[1].csv')
print(data.head)

#sales_data=data['Item_Outlet/-Sales'].dropped()
#print(sales_data)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

data=pd.read_csv('/content/train[1].csv')
print(data.head)

sales_data=data['Item_Outlet_Sales'].dropna()
print(sales_data)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

data=pd.read_csv('/content/train[1].csv')
print(data.head)

sales_data=data['Item_Outlet_Sales'].dropna()
print(sales_data)

mean=np.mean(sales_data)
print(f'Mean: {mean}')

max=np.max(sales_data)
print(f'Max: {max}')

min=np.min(sales_data)
print(f'Min: {min}')

median=np.median(sales_data)
(print(f'Median: {median}'))

mode=stats.mode(sales_data)
print(f'Mode: {mode}')
var=np.var(sales_data)
print(f'Variance: {var}')

std=np.std(sales_data)
print(f'Standard deviation: {std}')

skewness=stats.skew(sales_data)
print(f'Skewness: {skewness}')

kurtosis=stats.kurtosis(sales_data)
print(f'Kurtosis: {kurtosis}')

if skewness > 0:
  print('The distribution is positively skewed')
elif skewness < 0:
  print('The distribution is negatively skewed')
else:
  print('The distribution is symmetric')

if kurtosis > 0:
  print('The distribution is positve kurtosis')
elif kurtosis < 0:
  print('The distribution is negative kurtosis')
else:
  print('The distribution is zero kurtosis')

range=np.max(sales_data)-np.min(sales_data)
print(f'Range: {range}')

plt.hist(sales_data, bins=10)
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.title('Histogram of Sales Data')
plt.show()

plt.boxplot(sales_data)
plt.ylabel('Sales')
plt.xlabel('Sales')
plt.title('Boxplot of Sales Data')
plt.show()

plt.scatter(np.arange(len(sales_data)), sales_data)
plt.xlabel('Index')
plt.ylabel('Sales')
plt.title('Scatter Plot of Sales Data')
plt.show()

plt.axvline(mean,color='r',linestyle='dashed',linewidth=1)
plt.axvline(median,color='g',linestyle='dashed',linewidth=1)
plt.show()

results=pd.DataFrame()
results['Mean']=mean
results['Max']=max
results['Min']=min
results['Median']=median
results['Mode']=mode
results['Variance']=var
results['Standard Deviation']=std
results['Skewness']=skewness
results['Kurtosis']=kurtosis
results['Range']=range
print(results)

results.to_csv('results.csv', index=False)
results.to_excel('results.xlsx', index=False)