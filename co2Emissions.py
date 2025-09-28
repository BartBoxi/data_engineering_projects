from unittest.mock import inplace

import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
import plotly.express as px
from IPython.display import display, Markdown

sns.set_style("darkgrid")
sns.set(rc={'axes.facecolor':'lightsteelblue', 'figure.facecolor':'white'})

input_dir = '/Users/bartoszpudlo/PycharmProjects/data_engineering_projects/rawdata/CO2_Emissions_1960-2018.csv'
data = pd.read_csv(input_dir, index_col='Country Name')

data = data.transpose()
data.index = pd.to_datetime(data.index).year

data.dropna(axis=1, inplace= True)
print(data.head())


### Creating a plot for world data
plt.figure(figsize=(12,6))

sns.lineplot(x=data.index, y=data['World'])

plt.title('Total World CO2 Emission')
plt.xlabel('Year')
plt.ylabel('CO2 Emission (Million tonnes)')
plt.grid(True)

plt.savefig('world_co2_emissions.png')

# plotting the graph comparing a couple of interesting countries

countires_to_plot = ['China', 'United States','India', 'Poland']

sns.lineplot(data=data[countires_to_plot], dashes=False, marker='o')

plt.title('CO2 Emissions Comparison for Selected Countries')
plt.xlabel('Year')
plt.ylabel('CO2 Emission (Million tonnes)')
plt.grid(True)
plt.savefig('country_comparison_plot.png')

## Based on the data we can try to do some prediction of the co2 emission

