# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:02:48 2023

@author: Ryan Kugler
"""

from nba_api.stats.endpoints import Scoreboard
from datetime import datetime, timedelta
from nba_api.stats.endpoints import BoxScoreTraditionalV2
import json
import csv

def getYesterdaysGameIDs():
    today = datetime.today()
    yesterday = today - timedelta(days=1) #TODO: Change this back to 1 
    yesterday_date = yesterday.strftime('%m/%d/%Y')
    scoreboard = Scoreboard(game_date=yesterday_date)
    yesterday_games = scoreboard.game_header.get_data_frame()
    game_ids = yesterday_games['GAME_ID'].tolist()
    return game_ids

def getUnformattedBoxScore(game_id):
    boxscore = BoxScoreTraditionalV2(game_id=game_id)
    players_stats = boxscore.player_stats.get_data_frame()
    selected_columns = ['TEAM_ABBREVIATION', 'PLAYER_NAME', 'MIN', 'PTS', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FTM', 'FTA', 'REB', 'AST', 'STL', 'BLK', 'TO']
    players_stats = players_stats.loc[:,selected_columns]
    headers = players_stats.columns.values.tolist()
    rows = players_stats.values.tolist()
    merged_boxscore = [dict(zip(headers, row)) for row in rows]
    return merged_boxscore

def toCSV(boxscore):
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(boxscore)

def removeNaN():
    with open('output_uncleaned.json', 'r') as f:
        data = f.read()
    data = data.replace('NaN', '0')
    json_data = json.loads(data)
    with open('../frontend/public/output.json', 'w') as f:
        json.dump(json_data,f,indent=4)

def toJSON(boxscore):
    with open('output_uncleaned.json', 'w') as file:
        json.dump(boxscore, file, indent=4)
    removeNaN()

def getBoxScores():
    createFile = True
    game_ids = getYesterdaysGameIDs()
    boxscore = []
    for game in game_ids:
        boxscore = boxscore + getUnformattedBoxScore(game)
    toJSON(boxscore)
    

getBoxScores()