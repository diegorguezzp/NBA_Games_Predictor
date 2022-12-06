import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas_profiling
import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split
import time
from sklearn.metrics import classification_report, confusion_matrix, plot_confusion_matrix, roc_curve, auc, accuracy_score
from humanfriendly import format_timespan
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import plot_roc_curve
import pickle

df_games = pd.read_csv('./data/games.csv')
pd.set_option('display.max_columns', None)


#Conversion de la variable 'GAME_DATE_EST' a formato fecha
df_games['GAME_DATE_EST'] = pd.to_datetime(df_games['GAME_DATE_EST'])
df_games = df_games.sort_values(by='GAME_DATE_EST', ascending=False)
df_teams = pd.read_csv('./data/teams.csv')
df_names = df_teams[['TEAM_ID', 'NICKNAME']]

#Sustitución del ID local por el nickname del equipo
home_names = df_names.copy()
home_names.columns = ['HOME_TEAM_ID', 'NICKNAME']
merge_1 = pd.merge(df_games['HOME_TEAM_ID'], home_names, how ="left", on="HOME_TEAM_ID")  
df_games['HOME_TEAM_ID'] = merge_1['NICKNAME']

#Sustitución del ID visitante por el nickname del equipo
visitor_names = df_names.copy()
visitor_names.columns = ['VISITOR_TEAM_ID', 'NICKNAME']
merge_2 = pd.merge(df_games['VISITOR_TEAM_ID'], visitor_names, how = "left", on="VISITOR_TEAM_ID")
df_games['VISITOR_TEAM_ID'] = merge_2['NICKNAME']

#Eliminación de las columnas redundantes con anterioridad
df_games = df_games.drop(['GAME_STATUS_TEXT', 'TEAM_ID_home', 'TEAM_ID_away'], axis=1)

#Se crean tres nuevas variables a partir de la variable GAME_DATE_EST
df_games['GAME_YEAR'] = pd.to_datetime(df_games['GAME_DATE_EST']).dt.year.apply(str)
df_games['GAME_MONTH'] = pd.to_datetime(df_games['GAME_DATE_EST']).dt.month.apply(str)
df_games['GAME_DAY'] = pd.to_datetime(df_games['GAME_DATE_EST']).dt.day.apply(str)
df_games['GAME_YEAR'] = pd.to_numeric(df_games['GAME_YEAR'])
df_games['GAME_MONTH'] = pd.to_numeric(df_games['GAME_MONTH'])
df_games['GAME_DAY'] = pd.to_numeric(df_games['GAME_DAY'])

#Eliminación de las columnas GAME_DATE_EST
df_games.drop(['GAME_DATE_EST', 'SEASON'], axis=1, inplace=True)

c=['HOME_TEAM_ID','VISITOR_TEAM_ID']
for i in c:
  freq=df_games[i].value_counts().to_dict()
  df_games[i]=df_games[i].map(freq)

df_games = df_games.dropna()
print(df_games)
#Eliminación de las variables 'PTS_home' y 'PTS_away'
df_games.drop(['PTS_home', 'PTS_away', 'GAME_YEAR','GAME_MONTH','GAME_DAY','HOME_TEAM_ID','VISITOR_TEAM_ID'], axis=1, inplace=True)
#Eliminación de filas duplicadas
df_games = df_games.drop_duplicates(subset=['GAME_ID'], ignore_index=False)
df_games = df_games.set_index('GAME_ID')


df_games.to_csv('./data/final_data.csv', encoding='utf-8', index=False)
df_names.to_csv('./data/final_teams.csv', encoding='utf-8', index=False)
X = df_games.drop(['HOME_TEAM_WINS'], axis=1)
Y = df_games['HOME_TEAM_WINS']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#Regresión Logística
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)
tiempo_inicio = time.time()
print("REGRESIÓN Logística, puntuación en test:" + str(model.score(X_test, Y_test)))
print("REGRESIÓN Logística, puntuación en train:" + str(model.score(X_train, Y_train)))
tiempo_fin = time.time() - tiempo_inicio
print("REGRESIÓN Logística, tiempo de ejecución", format_timespan(tiempo_fin))

pickle.dump(model,open("./models/nba.pickle", 'wb'))




