# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:02:48 2023

@author: Ryan Kugler
"""

from nba_api.stats.endpoints import Scoreboard
from datetime import datetime, timedelta
from nba_api.stats.endpoints import BoxScoreTraditionalV2
from tabulate import tabulate

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
        players_stats = boxscore.player_stats.get_data_frame()
        
        selected_columns = ['PLAYER_NAME', 'PTS', 'REB', 'AST']
        players_stats = players_stats.loc[:,selected_columns]
        headers = players_stats.columns.values.tolist()
        rows = players_stats.values.tolist()
        print(tabulate(rows,headers=headers))



# MAIN

gameids = getYesterdaysGameIDs()
getUnformattedBoxScore(gameids)


