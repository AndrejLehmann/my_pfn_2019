#!/usr/bin/env python3

import re
import matplotlib.pyplot as plt
plt.switch_backend('agg') # to allow remote use
from data_matrix_class import DataMatrix

stream = open('gapminder_all.csv')
key_col = 1 # Column with countries
gdp = DataMatrix(stream,1,',')
attributes = gdp.attribute_list()
gdp_keys = [a for a in attributes if re.search(r'gdpPercap_',a)]
#print('gdp_keys={}'.format(gdp_keys))
au_data = list(gdp.matrix_select(gdp_keys,['Australia']))
years = [int(re.sub(r'^gdpPercap_','',a)) \
         for k, a, value in au_data]
gdp_australia = [int(re.sub(r'\.\d+$','',value)) for k, a, value in au_data]
stream.close()
#print(years)
#print(gdp_australia)
fig, ax = plt.subplots()
ax.plot(years, gdp_australia, 'b-', label='Australia')
ax.legend(loc='upper left')
ax.set_xlabel('Year')
ax.set_ylabel('GDP per capita ($)')
fig.savefig('gdpAustralia.pdf')
