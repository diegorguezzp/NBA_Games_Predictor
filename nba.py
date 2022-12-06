import pickle
from audioop import lin2adpcm
from turtle import pu
from regex import P
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


model = pickle.load(open("./models/nba.pickle", 'rb'))

equipos1 = ['Nets', 'Knicks', 'Magic', 'Pacers', 'Sixers', 'Suns', 'Blazers', 'Kings', 'Spurs', 'Thunder']
equipos2 = ['Raptors', 'Jazz', 'Grizzlies', 'Wizards', 'Pistons', 'Hornets', 'Cavaliers', 'Warriors', 'Hawks', 'Celtics']
equipos3 = ['Pelicans', 'Bulls', 'Mavericks', 'Nuggets', 'Rockets', 'Clippers', 'Lakers', 'Heat', 'Bucks', 'Timberwolves']
print(equipos1)
print(equipos2)
print(equipos3)
local = input("Home Team:\n")
away = input("Away Team:\n")

driver_path = 'C:\\Users\\diego\\Downloads\\chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get('https://es.global.nba.com/teams/stats/#!/' + local)



WebDriverWait(driver, 5)\
      .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button#onetrust-accept-btn-handler')))\
      .click()
wait = WebDriverWait(driver, 10)

wait = WebDriverWait(driver, 10)
texto = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/nba-stat-table/div/div[1]/table/tbody/tr[1]')))
home_data_vector = texto.text.split()

field_goals_home = round(float(home_data_vector[2]) / 100, 3)
print("% Tiros de Campo:",field_goals_home)

free_throws_home = round(float(home_data_vector[4]) / 100, 3)
print("% Tiros Libres:",free_throws_home)

pts3_throws_home = round(float(home_data_vector[3]) / 100, 3)
print("% Tiros de 3 ptos:",pts3_throws_home)

asists_home = round(float(home_data_vector[9]))
print("Asistencias pp:",asists_home)

rebounds_home = round(float(home_data_vector[8]))
print("Rebotes pp:",rebounds_home)

#driver.close()

#driver_path1 = 'C:\\Users\\diego\\Downloads\\chromedriver.exe'
#driver1 = webdriver.Chrome(driver_path1)
driver = webdriver.Chrome(driver_path)
driver.get('https://es.global.nba.com/teams/stats/#!/' + away)
#WebDriverWait(driver1, 5)\
 #     .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button#onetrust-accept-btn-handler')))\
  #    .click()

wait = WebDriverWait(driver, 10)
texto = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/nba-stat-table/div/div[1]/table/tbody/tr[1]')))
away_data_vector = texto.text.split()

field_goals_away = round(float(away_data_vector[2]) / 100, 3)
print("% Tiros de Campo:",field_goals_away)

free_throws_away = round(float(away_data_vector[4]) / 100, 3)
print("% Tiros Libres:",free_throws_away)

pts3_throws_away = round(float(away_data_vector[3]) / 100, 3)
print("% Tiros de 3 ptos:",pts3_throws_away)

asists_away = round(float(away_data_vector[9]))
print("Asistencias pp:",asists_away)

rebounds_away = round(float(away_data_vector[8]))
print("Rebotes pp:",rebounds_away)

driver.close()

match = [[field_goals_home, free_throws_home, pts3_throws_home, asists_home, rebounds_home, field_goals_away, free_throws_away, pts3_throws_away, asists_away, rebounds_away]]
prediccion = model.predict(match)
predicciones = []
for i in range(1000):
      aux = model.predict(match)
      predicciones.append(aux[0])
if prediccion[0] == 1:
      print("Winner: Home", local)
else:
      print("Winner: Away", away)

print(predicciones)