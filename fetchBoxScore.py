# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:02:48 2023

@author: Ryan Kugler
"""

from nba_api.stats.endpoints import Scoreboard
from datetime import datetime, timedelta
from nba_api.stats.endpoints import BoxScoreTraditionalV2
from tabulate import tabulate
import json
import csv

def getYesterdaysGameIDs():
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    yesterday_date = yesterday.strftime('%m/%d/%Y')
    scoreboard = Scoreboard(game_date=yesterday_date)
    yesterday_games = scoreboard.game_header.get_data_frame()
    game_ids = yesterday_games['GAME_ID'].tolist()
    return game_ids

def getUnformattedBoxScore(game_ids):

    for game_id in game_ids:
        boxscore = BoxScoreTraditionalV2(game_id=game_id)
        team_stats = boxscore.team_stats.get_data_frame()
        players_stats = boxscore.player_stats.get_data_frame()
        

        selected_columns = ['TEAM_ABBREVIATION', 'PLAYER_NAME', 'MIN', 'PTS', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FTM', 'FTA', 'REB', 'AST', 'STL', 'BLK', 'TO']
        players_stats = players_stats.loc[:,selected_columns]
        headers = players_stats.columns.values.tolist()
        rows = players_stats.values.tolist()
        
        merged_boxscore = [headers, rows]

        return merged_boxscore
        # with open('data.csv', 'w', newline='') as f:
            
        #     writer = csv.writer(f)
        #     writer.writerows(merged_boxscore)
        
        # csv_data = tabulate(rows,headers=headers, tablefmt='csv')
        # reader = csv.DictReader(csv_data.splitlines())
        # json_data = json.dumps([row for row in reader], indent=4)
        
        # with open ('data.json', 'w') as f:
        #     f.write(json_data)
        
        
        # print(tabulate(rows,headers=headers, tablefmt="grid"))


def toCSV(boxscore):
    with open('data.csv', 'w', newline='') as f:
        
        writer = csv.writer(f)
        writer.writerows(boxscore)

def toJSON(boxscore):
    return



gameids = getYesterdaysGameIDs()
getUnformattedBoxScore(gameids)
