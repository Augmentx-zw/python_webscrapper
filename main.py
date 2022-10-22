from ast import For
from msilib.schema import tables
from re import S
import requests
from bs4 import BeautifulSoup
import json


responce = requests.get('https://en.m.wikipedia.org/wiki/Khabib_Nurmagomedov')

print(responce.status_code)
soup = BeautifulSoup(responce.text, 'html.parser')
print(soup.title.string)

tables = soup.find_all("table", attrs={'class': 'wikitable'})

matches = tables[1]
opponents = []
trs = matches.find_all("tr")
for tr in trs:
    tds = tr.find_all("td")
    if not tds:
        continue

    opponent_node = tds[2]
    opponent_name = opponent_node.string
    if opponent_name is None:
        opponent_name = opponent_node.a.string
        
        continue
        
    opponents.append(opponent_name.strip('\n'))

j_dumps = json.dumps(opponents)
print(j_dumps)
     


with open('khabib_2.json', 'w', encoding='utf-8') as f:
    f.write(j_dumps)