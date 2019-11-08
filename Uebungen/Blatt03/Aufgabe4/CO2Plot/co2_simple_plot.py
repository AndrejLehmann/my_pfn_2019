#!/usr/bin/env python3
# Lehmann.Music
# Bearbeitungszeit: 1h

import matplotlib.pyplot as plt
import sys
plt.switch_backend('agg') # to allow remote use

# Plot for the emission of CO2 for different countries over the years
jahre = [1971,1975,1980,1985,1990,1995,2000,2005,2010,2016]
laender = []
data_lists=[]

# upload the tsv file
datafilename = 'data.tsv'
print('open"{}"'.format(datafilename))

try:
    data_stream= open(datafilename, 'r')
except IOError as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0], err))
    exit(1)

# store the data in separate lists
for line in data_stream:
    print('Country:\n{}'.format(line),end=' ')
    split_line = line.rstrip()
    split_line = split_line.split('\t')
    laender.append(str(split_line[0]))
    data_lists.append(split_line[1::])
print('Laender',laender)
print('data lists', data_lists)
data_stream.close()


# make the plot

fig, ax = plt.subplots(figsize=(10,8))
ax.set_xlabel('Jahr')
ax.set_ylabel('CO2 Emissionen/Person (t)')
ax.set_title('Entwicklung der CO2 Emission fuer einige Industrielaender')
ax.set_xticks(jahre)
for i in range(len(jahre)):
    ax.plot(jahre[i], data_lists[i], label=laender[i])
fig.savefig('plot.pdf')
