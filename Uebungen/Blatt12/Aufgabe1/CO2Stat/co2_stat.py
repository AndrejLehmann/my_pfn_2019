import sys
import re
from bs4 import BeautifulSoup

def convert_table_headers(h_list):
    return [re.sub(r'\'', '19', date_short) for date_short in h_list]


def co2_stat_table_line_get(co2_stat_html):
    soup = BeautifulSoup(co2_stat_html, features='html.parser')
    table = soup.find('table')
    assert table
    thead = table.find('thead')
    tr = thead.find('tr')
    h_list = [th.text for th in tr.find_all('th')]
    tbody = table.find('tbody')
    print(tbody)
    sys.exit()
    gb_stat_table_lines = ['\t'.join(h_list)]
    for six_tup in tbody.find_all('tr'):
      data_fields = [td.text for td in six_tup.find_all('td')]
      assert len(data_fields) == 6
      gb_stat_table_lines.append('\t'.join(data_fields))
    return gb_stat_table_lines


with open('CO2ausstoss.html') as stream:
    co2_stat_html = stream.read()

co2_stat_table_line_get(co2_stat_html)
