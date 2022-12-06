![image](https://user-images.githubusercontent.com/67483127/206028985-1be63d95-2ce0-485b-9229-c590f8cd501f.png)

A ML algorithm that predicts the winner of an NBA game

---

This algorithm has been tested on more than 100 nba games of the 2022/2023 season and betting the same amount in all the games the profit is positive. It can be checked in ```./historical/registro.csv```.

⚠⚠⚠ **Warning: betting is not recommended and the author of this algorithm cannot be held responsible for future results.**

---

## Index
- **Data Extraction and Processing**
- **Model Training**
- **Real Life Testing**
- **Usage**

---

### 1. Data Extraction and Processing

All data has been extracted from the following link https://www.kaggle.com/datasets/nathanlauga/nba-games/code where we are provided with several files, both with data of players, teams and matches. We have used data from both the ```./data/games.csv``` and the ```./data/teams.csv``` file.

Once the data to be worked with have been chosen, several operations have been carried out on them to transform them into the desired shape. Subsequently, a correlation matrix between the variables was represented in order to know which variables to continue using and which to discard.

![image](https://user-images.githubusercontent.com/67483127/206037210-4da65194-c19b-492d-a473-7d3f883c0fdc.png)

Finally, the resulting dataset with which the different models are going to be trained has been saved in the file ```./data/final_data.csv```
