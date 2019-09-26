import requests
import json
import pandas as pd 
from bs4 import BeautifulSoup

data = requests.get('http://digidb.io/digimon-list/')
digi = BeautifulSoup(data.content,'html.parser')
data = digi.find('table', id='digiList')

Column = []
for i in digi.find_all('th'):
    Column.append(i.string)
# print(Column)

Digimon = []
data = data.find_all('tr')
for item in data[1:]:
    no = item.td.string
    digimon = item.a.string
    image = item.img['src']
    stage = item.center.string
    digiType = item.td.find_next_sibling().find_next_sibling().find_next_sibling()
    attribute = item.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()
    memory = attribute.find_next_sibling()
    equip = memory.find_next_sibling()
    hp = equip.find_next_sibling()
    sp = hp.find_next_sibling()
    atk = sp.find_next_sibling()
    dfs = atk.find_next_sibling()
    intl = dfs.find_next_sibling()
    spd = intl.find_next_sibling()

    x = {
        'no':int(no),
        'digimon':digimon,
        'image':image,
        'stage':stage,
        'type':digiType.string,
        'attribute':attribute.string,
        'memory':memory.string,
        'equip slots':equip.string,
        'hp':hp.string,
        'sp':sp.string,
        'atk':atk.string,
        'def':dfs.string,
        'int':intl.string,
        'spd':spd.string,
    }
    Digimon.append(x)
# print(Digimon)

## Export data to JSON ##
with open('DigiData.json','w') as x:
    x.write(str(Digimon).replace("'",'"'))