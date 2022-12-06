import pandas as pd
from tabulate import tabulate
from collections import Counter

df = pd.read_csv('registro.csv', delimiter = ',')

equipos = ['Nets', 'Knicks', 'Magic', 'Pacers', 'Sixers', 'Suns', 'Blazers', 'Kings', 
            'Spurs', 'Thunder','Raptors', 'Jazz', 'Grizzlies', 'Wizards', 'Pistons', 
            'Hornets', 'Cavaliers', 'Warriors', 'Hawks', 'Celtics','Pelicans', 'Bulls', 
            'Mavericks', 'Nuggets', 'Rockets', 'Clippers', 'Lakers', 'Heat', 'Bucks', 'Timberwolves']

suma = 0
banco = 30

for index, row in df.iterrows():
  if row['Correct'] == 1:
    suma = suma + (row['Quota'] - 1) 
  elif row['Correct'] == 0:
    banco = banco - 1
veces = []

a = df.HomeTeam.value_counts().to_dict()
b = df.AwayTeam.value_counts().to_dict()

total = 0
tuple = ()
for equipo in equipos:
  counterHome, counterAway, cH, cA, iH, iA = 0, 0, 0, 0, 0, 0
  for index, row in df.iterrows():
    if row.HomeTeam == equipo:
      counterHome += 1
      if row.Correct == 1:
        cH += 1
      else:
        iH += 1
    if row.AwayTeam == equipo:
      counterAway += 1
      if row.Correct == 1:
        cA += 1
      else:
        iA += 1
  total += cH + iH + cA + iA
  aux1 = 'Home: ' + str(cH) + '/' + str(counterHome)
  aux2 = 'Away: ' + str(cA) + '/' + str(counterAway)
  tuple += (equipo, aux1, aux2)

for x in tuple:
  print(x)

print('Beneficio: ',  suma + banco)
