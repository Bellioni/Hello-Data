# -*- coding: utf-8 -*-
"""numpy array

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZwZokD51kS7FjATJqduQg6VyfSncr4ZJ
"""

# import numpy
import numpy as np

# looping & printing a 1d array
arr1 = np.array([1, 2, 3, 4])
print(arr1)

#display the shape(dimensions) of the array
print(np.shape(arr1))

# loop through the 1 dimensional array
for i in range(np.shape(arr1)[0]):
    print(arr1[i])

# This is an example of a two dimensional array
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2)
print(np.shape(arr2))

# two nested loops to access all elements of
# the two dimensional array arr2
for ii in range(np.shape(arr2)[0]):
    for jj in range(np.shape(arr2)[1]):
        print(arr2[ii, jj])

# Now, create a 3-dimensional array
arr3 = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
print(arr3)
print(np.shape(arr3))  # Should print (2, 2, 3)

# three nested loops to access all elements of the 3D array arr3
for i in range(np.shape(arr3)[0]):
    for j in range(np.shape(arr3)[1]):
        for k in range(np.shape(arr3)[2]):
            print(arr3[i, j, k])

1# import matplotlib & pandas
import matplotlib.pyplot as plt
import pandas as pd

2# Read gapminder_gdp_asia.csv
data = pd.read_csv('gapminder_gdp_asia.csv', index_col= 'country')

3# Extract years from colunm
years = data.columns.str.strip('gdpPercap_')

4# Convert year values to integers, saving results back to dataframe
data.columns = years.astype(int)

5# Plot China and india GDP from 1952-2007
data.loc['China'].plot()
data.loc['India'].plot()

#6 Labelling
plt.title('GDP of China vs. India from 1952 to 2007')
plt.legend(['China', 'India'], loc='lower right')
plt.ylabel('GDP per capita')
plt.xlabel('Years')
plt.savefig('my_figure.png')

#7 Plot the results
plt.show()

1# import pandas
import pandas as pd
import matplotlib.pyplot as plt

2# Read gapminder_all.csv
data_all = pd.read_csv('gapminder_all.csv', index_col= 'country')

3# Create scatter plot for 2007 GDP per capita vs life expectancy
ax = data_all.plot(kind='scatter',
                    x='gdpPercap_2007',
                    y='lifeExp_2007',
                    s=data_all['pop_2007']/1e6, figsize=(16, 8))
4# Labelling
ax.set_xlabel('GDP per Capita in 2007')
ax.set_ylabel('Life Expectancy in 2007')
ax.set_title('Correlation between GDP per Capita and Life Expectancy (2007)\nMarker size proportional to Population')
plt.savefig('my_figure.png')

5# Plot the results
plt.show()