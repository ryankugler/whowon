# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:17:36 2023

@author: Ryan Kugler
"""

from datetime import date
import pandas
from nba_api.live.nba.endpoints import scoreboard
import json


def todaysGames():
    schedule = "{awayTeam} vs. {homeTeam} @ {gameTimeLTZ}" 
    board = scoreboard.ScoreBoard()
    games = board.games.get_dict()
    today = date.today()
    todaysGames = []
    
    #print(today.month, '/', today.day)
    for game in games:
        todaysGames.append(schedule.format(awayTeam=game['awayTeam']['teamName'], 
                              homeTeam=game['homeTeam']['teamName'], 
                              gameTimeLTZ=game['gameStatusText']))
    return todaysGames

def toJSON(schedule):
     with open('schedule.json', 'w') as f:
         json.dump(schedule, f, indent=4)
