import re

monate = ['Januar', 'Februar', 'Maerz', 'April', 'Mai', 'Juni', 'Juli', 'August',
          'September', 'Oktober', 'November', 'Dezember']

def date_reformat_g2intl(gdatestring):
    m = re.search(r'(\d{2})[.]\s*(\w+)\s*(\d{4})', gdatestring)
    DD = m.group(1)
    Monat = m.group(2)
    for n,monat in enumerate(monate):
        if monat == Monat:
            if n+1 < 10:
                MM = '0{}'.format(n+1)
            else:
                MM = '{}'.format(n+1)
    YYYY = m.group(3)
    #print(DD, Monat, YYYY)
    return '{}-{}-{}'.format(YYYY, MM, DD)

for datestring in ['24.Dezember 2017', '31.  Januar2018', '01. April   2018']:
    print('{}'.format(date_reformat_g2intl(datestring)))
