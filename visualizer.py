# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
#
# import matplotlib.pyplot as plt
# import pandas as pd
#
# URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
# df1 = pd.read_csv(URL_DATASET)
#
#
# sa = df1[df1['Country'] == 'South Africa']
# print(sa.head(3))
#
#
# plt.rcParams["figure.figsize"]=20,20
#
# sa.plot(kind = 'bar', x = 'Date', y = 'Confirmed', color = 'blue')
#
# ax1 = plt.gca()
# sa.plot(kind = 'bar', x = 'Date', y = 'Deaths', color = 'red', ax = ax1)
# plt.show()


import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import matplotlib.pyplot as pl
import pandas as pd


url = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'

dataset = pd.read_csv(url)

sa = dataset[dataset['Country'] == 'South Africa']
print(sa.head(3))

pl.rcParams['figure.figsize'] = 20,20

sa.plot(kind = 'bar', x = 'Date',y = 'Confirmed', color='blue')

axis = pl.gca()

sa.plot(kind = 'bar', x = 'Date', y = 'Deaths', color = 'red', ax = axis)

pl.show()
