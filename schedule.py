# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:17:36 2023

@author: Ryan Kugler
"""

from datetime import date
from nba_api.live.nba.endpoints import scoreboard

def todaysGames():
    schedule = "{awayTeam} vs. {homeTeam} @ {gameTimeLTZ}" 
    board = scoreboard.ScoreBoard()
    games = board.games.get_dict()
    today = date.today()
    
    print(today.month, '/', today.day)
    for game in games:
        print(schedule.format(awayTeam=game['awayTeam']['teamName'], 
                              homeTeam=game['homeTeam']['teamName'], 
                              gameTimeLTZ=game['gameStatusText']))
        
